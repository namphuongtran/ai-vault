---
title: "Bước 6 — Mỗi vai một model"
linkTitle: "Step 6 — A model per role"
weight: 6
description: Đo chi phí trên mỗi task hoàn thành qua các model và mức effort, với đáp án đúng được tính ra từ dữ liệu.
---

[Chọn model]({{< relref "choosing-a-model.md" >}}) là một phép đo, không phải cảm giác. Đơn vị
trung thực là **chi phí trên mỗi task hoàn thành**, không phải giá mỗi token. Một model rẻ mà
cần gấp ba số lượt, hoặc phải làm lại lần hai, thì không hề rẻ.

Đến cuối bước này bạn phải trả lời được: **khi nào model nhỏ hơn thắng xét trên tổng thể?**

## Xây dựng

Thêm một dòng trace, và gọi `log(agent, turn, r.usage)` ngay sau mỗi `create()` trong `run()`:

```python
def log(agent, turn, u):
    with open(WORKDIR.parent / "trace.jsonl", "a") as f:
        f.write(json.dumps({"agent": agent, "turn": turn, "context": context_size(u),
                            "cached": u.cache_read_input_tokens or 0, "output": u.output_tokens}) + "\n")
```

Rồi đo cùng một bộ task qua các model và mức effort. Đáp án đúng được tính ra từ chính các file,
không bao giờ gõ tay. Benchmark chỉ cho agent các tool chỉ-đọc nên nó không thay đổi được gì, và
việc chấm điểm cố ý chặt: làm đúng định dạng được yêu cầu cũng là một phần của công việc.

```python
# bench.py — chạy với WORKDIR=vault (bản sao content/en của vault này)
import itertools, json, re, time
import agent

ROOT = agent.WORKDIR
def front(path, key):
    return re.search(rf"^{key}:\s*\"?(.+?)\"?$", (ROOT / path).read_text(), re.M).group(1)

TASKS = [
    ("How many .md files are under deep-dives/, including subfolders? Reply with the number only.",
     str(len(list((ROOT / "deep-dives").rglob("*.md"))))),
    ("What is the front-matter weight of building/agent-harness.md? Reply with the number only.",
     front("building/agent-harness.md", "weight")),
    ("What is the title of building/loop-engineering/levels.md? Reply with the title only.",
     front("building/loop-engineering/levels.md", "title")),
    ("Which page under deep-dives/ has the most lines? Reply with its path only.",
     str(max((ROOT / "deep-dives").rglob("*.md"), key=lambda p: len(p.read_text().splitlines())).relative_to(ROOT))),
]

for model, effort in itertools.product(["claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"],
                                       ["low", "medium"]):
    tag, ok, t0 = f"{model}/{effort}", 0, time.time()
    for i, (q, expected) in enumerate(TASKS):
        answer = agent.run(q, tools=agent.READ_ONLY, model=model, effort=effort,
                           max_turns=15, agent=f"{tag}#{i}")
        ok += answer.strip().strip("`'\".").lower() == expected.lower()   # cố ý chấm chặt
    rows = [json.loads(l) for l in open(ROOT.parent / "trace.jsonl") if tag in l]
    print(f"{tag:26} solved {ok}/{len(TASKS)}  turns {len(rows):3}  "
          f"context tokens {sum(r['context'] for r in rows):8}  output {sum(r['output'] for r in rows):6}  "
          f"{time.time() - t0:5.0f}s")
```

## Kiểm tra

Bạn nhận được một bảng số liệu của riêng bạn: tỷ lệ thành công, số lượt, token và số giây cho
mỗi model và mức effort. Nhân số token với đơn giá trên trang pricing. Trang này cố ý không in
con số nào. Số của bạn mới là số đáng tin, và nó thay đổi theo mỗi lần ra model mới.

## Xem trong Claude Code

`/model sonnet` đổi model ngay giữa session. Dòng `model:` trong một file subagent chính là
`MODELS["sub"]` của bạn.

## Làm hỏng nó

Thêm một task cần nhiều bước suy luận, như *"which page links to the page with the most
headings?"* Xem model nhỏ nhất ở effort `low` trả lời nhanh và sai. Rồi kiểm tra xem model lớn
nhất ở effort `low` có thắng model tầm trung ở `medium` hay không.

## Đáp án

Model nhỏ thắng ở những việc hẹp, mô tả rõ, khối lượng lớn, có đầu ra kiểm tra được, và khi nó
xong việc với số lượt tương đương. Hãy đo chi phí trên mỗi task *hoàn thành*.

**Tiếp theo:** [Bước 7 — Kiểm soát của harness]({{< relref "/hands-on/lab-agent-harness/step-7-harness-controls" >}})
