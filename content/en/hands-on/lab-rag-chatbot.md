---
title: "Lab 1 — RAG Chatbot on Your Own Documents"
linkTitle: "Lab 1 — RAG chatbot"
weight: 1
description: Build a working RAG chatbot in seven incremental steps — each one runs before the next begins.
---

## Goal

Build the system from [Building a RAG system]({{< relref "/building/building-rag" >}}) for
real: a chatbot that answers from *your* documents, with citations. Seven steps, each
verifiable before the next — the same order a production system grows in.

The stack follows this vault's own advice (*the right stack, not the biggest*): **Postgres
does both keyword and vector search** (no separate search engine), a **local embedding
model** (no second API key), and **Claude** generates. Roughly 200 lines of Python.

```mermaid
flowchart LR
    S1[1 Infra] --> S2[2 Ingest] --> S3[3 Keyword search] --> S4[4 Hybrid]
    S4 --> S5[5 Full RAG] --> S6[6 Monitoring and cache] --> S7[7 Agentic upgrade]
```

**Prerequisites:** Docker, Python 3.11+, an Anthropic API key, and a folder of markdown files
to search (this vault's `content/` works nicely).

## Step 1 — Infrastructure

One container: Postgres with the [pgvector]({{< relref "/deep-dives/vector-databases" >}})
extension already built in.

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

**Check:** `docker exec -it $(docker ps -q) psql -U postgres -c "SELECT 1"` returns a row.

## Step 2 — Ingestion

Parse → chunk → store. Chunk by paragraphs up to ~1,200 characters with a one-paragraph
overlap, and keep the source path — that's your citation later.

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
            out.append("\n\n".join(buf)); buf = buf[-1:]  # overlap 1 paragraph
        buf.append(p)
    return out + ["\n\n".join(buf)] if buf else out

with psycopg.connect("postgresql://postgres:rag@localhost/postgres") as con:
    con.execute(DDL)
    for f in pathlib.Path("docs").rglob("*.md"):
        for c in chunk(f.read_text()):
            con.execute("INSERT INTO chunks(doc, content) VALUES (%s, %s)", (str(f), c))
```

**Check:** `SELECT count(*) FROM chunks;` shows your corpus, in pieces.

## Step 3 — Keyword search

Exact terms first — the underrated baseline. Postgres full-text search ranks with `ts_rank`
(not true BM25, but the same idea: exact-term matching; if you outgrow it, that's when a real
search engine earns its place).

```python
def search_keyword(con, q, k=10):
    return con.execute("""
      SELECT id, doc, content FROM chunks
      WHERE tsv @@ websearch_to_tsquery('english', %s)
      ORDER BY ts_rank(tsv, websearch_to_tsquery('english', %s)) DESC LIMIT %s""",
      (q, q, k)).fetchall()
```

**Check:** search for an exact string you know exists (an error code, a function name) — it
should be hit #1.

## Step 4 — Hybrid retrieval

Add meaning. Embed every chunk with a local model, search by cosine distance, and fuse both
rankings with **Reciprocal Rank Fusion** — each list covers the other's
[blind spots]({{< relref "/deep-dives/advanced-rag" >}}).

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")   # 384-dim, runs locally

# once: ALTER TABLE chunks ADD COLUMN embedding vector(384);
# then: UPDATE each row with model.encode(content).tolist()

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

**Check:** ask a *paraphrased* question (no shared keywords with the doc). Vector search
finds it; keyword alone didn't. Fused, exact-term queries still work too.

## Step 5 — Full RAG

Retrieve → augment → generate, behind an API. Numbered context makes citations checkable.

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

**Check:** `uvicorn app:app` then ask something your docs answer — the reply cites [n] and
the facts exist in those chunks. Ask something they *don't* answer — it should say so
instead of inventing (that's your grounding prompt working).

## Step 6 — Monitoring and caching

You can't improve what you can't see — capture a
[trace]({{< relref "observability.md" >}}) per request, and stop paying twice for
the same question.

```python
import time, json, hashlib

CACHE = {}

def traced_ask(q):
    key = hashlib.sha256(q.strip().lower().encode()).hexdigest()
    if key in CACHE:
        return CACHE[key] | {"cached": True}
    t0 = time.time()
    out = ask(q)                        # step-5 logic
    trace = {"q": q, "sources": out["sources"], "ms": int((time.time() - t0) * 1000),
             "in_tokens": out["usage"].input_tokens, "out_tokens": out["usage"].output_tokens}
    with open("traces.jsonl", "a") as f:
        f.write(json.dumps(trace) + "\n")
    CACHE[key] = out
    return out
```

**Check:** the same question twice — second answer is instant and `traces.jsonl` shows
latency, sources, and token counts per request (multiply by price = cost per question).

## Step 7 — Agentic upgrade

Retrieval stops being a fixed first step and becomes a
[tool the model calls]({{< relref "/building/agentic-rag" >}}) — it decides *whether*, *what*,
and *how many times* to search. Note the stop condition: agents need brakes, not just engines.

```python
TOOLS = [{"name": "search_docs",
          "description": "Search the document base. Returns numbered passages.",
          "input_schema": {"type": "object",
                           "properties": {"query": {"type": "string"}},
                           "required": ["query"]}}]

def agentic_ask(q, max_rounds=5):
    msgs = [{"role": "user", "content": q}]
    for _ in range(max_rounds):                      # stop condition
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

**Check:** ask a [multi-hop question]({{< relref "/building/agentic-rag" >}}) that needs two
different lookups — the traces show two `search_docs` calls with *different* queries the
model wrote itself. Ask "hello" — it answers with zero searches. That's the difference
between a pipeline and an agent.

## Where this setup tops out

- Postgres FTS is not true BM25; pgvector fits millions, not billions — the
  [store table]({{< relref "/deep-dives/vector-databases" >}}) says when to move.
- The in-process cache dies with the process — Redis is the production answer.
- Quality is unmeasured so far: no eval set, no faithfulness score. That's **Lab 3**.

## Sources

- [pgvector — vector similarity for Postgres](https://github.com/pgvector/pgvector)
- [PostgreSQL — Full Text Search](https://www.postgresql.org/docs/current/textsearch.html)
- Cormack et al., *Reciprocal Rank Fusion outperforms Condorcet and individual rank learning methods* (SIGIR 2009) — [PDF](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)
- Reimers & Gurevych, *Sentence-BERT* (2019) — [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- [Anthropic — Working with messages](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) · [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
