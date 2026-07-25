---
title: "Lab 1 — RAG Chatbot trên tài liệu của chính bạn"
linkTitle: "Lab 1 — RAG chatbot"
weight: 1
description: Xây một RAG chatbot chạy được qua bảy bước tăng dần — mỗi bước chạy xong mới sang bước sau.
---

## Mục tiêu

Xây thật hệ thống trong [Building a RAG system]({{< relref "/building/building-rag" >}}):
một chatbot trả lời từ tài liệu *của bạn*, có trích dẫn. Bảy bước, mỗi bước kiểm chứng được
trước khi sang bước sau — đúng thứ tự một hệ thống production lớn lên.

Stack đi theo chính lời khuyên của vault này (*stack phù hợp, không phải stack to nhất*):
**Postgres lo cả keyword lẫn vector search** (không cần search engine riêng), một **embedding
model chạy local** (không cần API key thứ hai), và **Claude** sinh câu trả lời. Tổng cộng
khoảng 200 dòng Python.

```mermaid
flowchart LR
    S1[1 Infra] --> S2[2 Ingest] --> S3[3 Keyword search] --> S4[4 Hybrid]
    S4 --> S5[5 Full RAG] --> S6[6 Monitoring and cache] --> S7[7 Agentic upgrade]
```

**Yêu cầu trước:** Docker, Python 3.11+, một Anthropic API key, và một thư mục file markdown
để tìm kiếm (`content/` của chính vault này là ứng viên đẹp).

## Bước 1 — Hạ tầng

Một container duy nhất: Postgres với extension
[pgvector]({{< relref "/deep-dives/vector-databases" >}}) build sẵn.

```yaml
# docker-compose.yml
services:
  db:
    image: pgvector/pgvector:pg17
    environment:
      POSTGRES_PASSWORD: rag
    ports: ["5432:5432"]
```

```bash
docker compose up -d
python -m venv .venv && source .venv/bin/activate
pip install psycopg anthropic sentence-transformers fastapi uvicorn
```

**Kiểm tra:** `docker exec -it $(docker ps -q) psql -U postgres -c "SELECT 1"` trả về một hàng.

## Bước 2 — Ingestion

Parse → chunk → lưu. Chunk theo đoạn văn tới ~1.200 ký tự, chồng lấn một đoạn, và giữ đường
dẫn nguồn — đó chính là trích dẫn sau này.

```python
# ingest.py
import pathlib, psycopg

DDL = """
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS chunks(
  id bigserial PRIMARY KEY, doc text, content text,
  tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED);
CREATE INDEX IF NOT EXISTS chunks_tsv ON chunks USING gin(tsv);
"""

def chunk(text, size=1200):
    paras, buf, out = text.split("\n\n"), [], []
    for p in paras:
        if sum(map(len, buf)) + len(p) > size and buf:
            out.append("\n\n".join(buf)); buf = buf[-1:]  # chồng lấn 1 đoạn
        buf.append(p)
    return out + ["\n\n".join(buf)] if buf else out

with psycopg.connect("postgresql://postgres:rag@localhost/postgres") as con:
    con.execute(DDL)
    for f in pathlib.Path("docs").rglob("*.md"):
        for c in chunk(f.read_text()):
            con.execute("INSERT INTO chunks(doc, content) VALUES (%s, %s)", (str(f), c))
```

**Kiểm tra:** `SELECT count(*) FROM chunks;` cho thấy kho tài liệu của bạn, đã thành mảnh.

## Bước 3 — Keyword search

Term chính xác trước — baseline bị đánh giá thấp. Full-text search của Postgres xếp hạng bằng
`ts_rank` (không phải BM25 thật, nhưng cùng ý tưởng: khớp term chính xác; khi nào vượt quá nó,
đó là lúc một search engine thật xứng đáng có mặt).

```python
def search_keyword(con, q, k=10):
    return con.execute("""
      SELECT id, doc, content FROM chunks
      WHERE tsv @@ websearch_to_tsquery('english', %s)
      ORDER BY ts_rank(tsv, websearch_to_tsquery('english', %s)) DESC LIMIT %s""",
      (q, q, k)).fetchall()
```

**Kiểm tra:** tìm một chuỗi chính xác bạn biết chắc tồn tại (mã lỗi, tên hàm) — nó phải là
kết quả #1.

## Bước 4 — Hybrid retrieval

Thêm phần ngữ nghĩa. Embed mọi chunk bằng model local, tìm theo khoảng cách cosine, rồi hợp
nhất hai bảng xếp hạng bằng **Reciprocal Rank Fusion** — mỗi danh sách bù
[điểm mù]({{< relref "/deep-dives/advanced-rag" >}}) cho bên kia.

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")   # 384 chiều, chạy local

# một lần: ALTER TABLE chunks ADD COLUMN embedding vector(384);
# rồi: UPDATE từng hàng với model.encode(content).tolist()

def search_vector(con, q, k=10):
    return con.execute(
      "SELECT id, doc, content FROM chunks ORDER BY embedding <=> %s::vector LIMIT %s",
      (model.encode(q).tolist(), k)).fetchall()

def rrf(*rankings, k=60):
    scores = {}
    for ranking in rankings:
        for rank, row in enumerate(ranking):
            scores[row[0]] = scores.get(row[0], 0) + 1 / (k + rank + 1)
    best = sorted(scores, key=scores.get, reverse=True)
    rows = {r[0]: r for ranking in rankings for r in ranking}
    return [rows[i] for i in best]
```

**Kiểm tra:** hỏi một câu *diễn đạt khác hẳn* (không chung keyword với tài liệu). Vector tìm
ra; keyword một mình thì không. Hợp nhất xong, truy vấn term chính xác vẫn chạy tốt.

## Bước 5 — Full RAG

Retrieve → augment → generate, đứng sau một API. Context đánh số làm trích dẫn kiểm tra được.

```python
# app.py
import anthropic, psycopg
from fastapi import FastAPI

app, claude = FastAPI(), anthropic.Anthropic()

PROMPT = """Answer using ONLY the numbered context. Cite like [1].
If the context doesn't contain the answer, say so.

{context}

Question: {q}"""

@app.get("/ask")
def ask(q: str):
    with psycopg.connect("postgresql://postgres:rag@localhost/postgres") as con:
        top = rrf(search_keyword(con, q), search_vector(con, q))[:5]
    ctx = "\n\n".join(f"[{i+1}] ({d}) {c}" for i, (_, d, c) in enumerate(top))
    msg = claude.messages.create(
        model="claude-sonnet-5", max_tokens=1024,
        messages=[{"role": "user", "content": PROMPT.format(context=ctx, q=q)}])
    return {"answer": msg.content[0].text, "sources": [d for _, d, _ in top],
            "usage": msg.usage}
```

**Kiểm tra:** `uvicorn app:app` rồi hỏi điều tài liệu của bạn trả lời được — câu trả lời
trích [n] và dữ kiện tồn tại trong đúng các chunk đó. Hỏi điều tài liệu *không* trả lời được
— nó phải nói thẳng thay vì bịa (đó là prompt grounding đang làm việc).

## Bước 6 — Monitoring và caching

Không thấy thì không cải thiện được — ghi một
[trace]({{< relref "/foundations/observability" >}}) mỗi request, và đừng trả tiền hai lần
cho cùng một câu hỏi.

```python
import time, json, hashlib

CACHE = {}

def traced_ask(q):
    key = hashlib.sha256(q.strip().lower().encode()).hexdigest()
    if key in CACHE:
        return CACHE[key] | {"cached": True}
    t0 = time.time()
    out = ask(q)                        # logic của bước 5
    trace = {"q": q, "sources": out["sources"], "ms": int((time.time() - t0) * 1000),
             "in_tokens": out["usage"].input_tokens, "out_tokens": out["usage"].output_tokens}
    with open("traces.jsonl", "a") as f:
        f.write(json.dumps(trace) + "\n")
    CACHE[key] = out
    return out
```

**Kiểm tra:** cùng một câu hỏi hai lần — lần hai trả lời tức thì, và `traces.jsonl` cho thấy
độ trễ, nguồn, số token mỗi request (nhân với đơn giá = chi phí mỗi câu hỏi).

## Bước 7 — Nâng cấp agentic

Truy xuất thôi là bước đầu cố định và trở thành
[tool mà model gọi]({{< relref "/building/agentic-rag" >}}) — nó tự quyết *có tìm không*,
*tìm gì*, và *tìm bao nhiêu lần*. Chú ý điều kiện dừng: agent cần phanh, không chỉ cần động cơ.

```python
TOOLS = [{"name": "search_docs",
          "description": "Search the document base. Returns numbered passages.",
          "input_schema": {"type": "object",
                           "properties": {"query": {"type": "string"}},
                           "required": ["query"]}}]

def agentic_ask(q, max_rounds=5):
    msgs = [{"role": "user", "content": q}]
    for _ in range(max_rounds):                      # điều kiện dừng
        r = claude.messages.create(model="claude-sonnet-5", max_tokens=1024,
                                   tools=TOOLS, messages=msgs)
        if r.stop_reason != "tool_use":
            return r.content[0].text
        call = next(b for b in r.content if b.type == "tool_use")
        with psycopg.connect("postgresql://postgres:rag@localhost/postgres") as con:
            top = rrf(search_keyword(con, call.input["query"]),
                      search_vector(con, call.input["query"]))[:5]
        result = "\n\n".join(f"[{i+1}] ({d}) {c}" for i, (_, d, c) in enumerate(top))
        msgs += [{"role": "assistant", "content": r.content},
                 {"role": "user", "content": [{"type": "tool_result",
                   "tool_use_id": call.id, "content": result}]}]
    return "Stopped after max search rounds."
```

**Kiểm tra:** hỏi một [câu hỏi multi-hop]({{< relref "/building/agentic-rag" >}}) cần hai lần
tra cứu khác nhau — trace cho thấy hai lần gọi `search_docs` với truy vấn *khác nhau* do
chính model viết. Hỏi "hello" — nó trả lời với số lần tìm bằng không. Đó chính là khác biệt
giữa một pipeline và một agent.

## Setup này chạm trần ở đâu

- Postgres FTS không phải BM25 thật; pgvector hợp hàng triệu, không phải hàng tỷ —
  [bảng chọn store]({{< relref "/deep-dives/vector-databases" >}}) nói khi nào nên chuyển.
- Cache trong process chết cùng process — Redis là câu trả lời production.
- Chất lượng vẫn chưa được đo: chưa có bộ eval, chưa có điểm faithfulness. Đó là **Lab 3**.

## Nguồn

- [pgvector — vector similarity cho Postgres](https://github.com/pgvector/pgvector)
- [PostgreSQL — Full Text Search](https://www.postgresql.org/docs/current/textsearch.html)
- Cormack et al., *Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods* (SIGIR 2009) — [PDF](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)
- Reimers & Gurevych, *Sentence-BERT* (2019) — [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- [Anthropic — Working with messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) · [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
