---
title: "Bước 4 — Quản lý context"
linkTitle: "Step 4 — Context management"
weight: 4
description: Cắt bớt, truy xuất đúng lúc, ghi nhớ, cache, compact — và vì sao lịch sử phải chỉ được nối thêm.
---

Mỗi lượt lại thêm vào `msgs`, và chẳng có gì rời đi. [Context
engineering]({{< relref "context-engineering.md" >}}) là việc giữ cho window đó gọn và hữu ích.

Đến cuối bước này bạn phải trả lời được: **vì sao *nhiều* context hơn có thể làm agent *tệ*
hơn, và vì sao lịch sử phải là append-only?**

## Xây dựng

Thêm bốn kỹ thuật:

```python
CLIP_AT = 4_000          # số ký tự tối đa một kết quả tool được đưa vào context
COMPACT_AT = 60_000      # số token context kích hoạt compaction

def clip(call_id, out):
    if len(out) <= CLIP_AT:
        return out
    spill = WORKDIR / ".tool-results" / f"{call_id}.txt"
    spill.parent.mkdir(exist_ok=True)
    spill.write_text(out)
    return (out[:CLIP_AT] + f"\n[... {len(out) - CLIP_AT} more characters. Full output saved to "
            f".tool-results/{call_id}.txt; search it with run_bash grep instead of reading it whole.]")

def system_prompt():
    notes = WORKDIR / "AGENT.md"           # memory của dự án, nạp một lần mỗi session
    return SYSTEM + (f"\n\n# Project notes\n{notes.read_text()}" if notes.exists() else "")

def context_size(u):
    return u.input_tokens + (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0)

SUMMARIZE = """Summarize this session so a fresh context can continue it without redoing work:
the task, decisions and constraints, what was tried and what failed, the current state of the
files, and what is left to do. Keep names, paths, numbers and error messages exact.
Do not call any tools; respond with text only."""

def compact(task, msgs, system, tools, model):
    # Chỉ gọi ngay sau một vòng tool trọn vẹn, nên không còn tool_use nào chờ kết quả.
    ask = msgs[:-1] + [{"role": "user", "content": msgs[-1]["content"] + [{"type": "text", "text": SUMMARIZE}]}]
    r = client.messages.create(model=model, max_tokens=16000, system=system, tools=tools,
                               messages=ask, cache_control={"type": "ephemeral"})  # cùng prefix: trúng cache
    return {"role": "user", "content": f"{task}\n\n# Progress so far\n{text_of(r)}\n\nContinue from here."}
```

Trong `execute()`, cho output đi qua `clip()` trước khi trả về. Sau đó sửa `run()`:

```python
def run(task, tools=TOOLS, model=MODEL, max_turns=25):
    system = system_prompt()                              # dựng một lần: đóng băng cho cả session
    msgs = [{"role": "user", "content": task}]
    for turn in range(max_turns):
        r = client.messages.create(model=model, max_tokens=16000, system=system, tools=tools,
                                   messages=msgs, cache_control={"type": "ephemeral"})
        print(f"turn {turn}: context={context_size(r.usage)} cached={r.usage.cache_read_input_tokens}")
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return text_of(r)
        calls = [b for b in r.content if b.type == "tool_use"]
        msgs.append({"role": "user", "content": [execute(c) for c in calls]})
        if context_size(r.usage) > COMPACT_AT:
            msgs = [compact(task, msgs, system, tools, model)]
    return f"Stopped after max_turns={max_turns} without finishing."
```

Mỗi kỹ thuật giải một vấn đề khác nhau:

| Kỹ thuật | Vấn đề nó giải |
| --- | --- |
| `clip()` + đổ ra file | Một output tool khổng lồ nhấn chìm window. Giữ một đoạn xem trước và con trỏ tới phần còn lại. |
| `grep` và `sed -n` trong system prompt | Truy xuất *đúng lúc*: lấy đúng ba dòng bạn cần, không phải cả file. |
| `AGENT.md` | Kiến thức cần sống qua các session: memory nạp một lần lúc bắt đầu. |
| `cache_control` | Phần prefix lặp lại bị tính tiền và xử lý lại ở mỗi lượt. Caching làm việc đọc lại nó rẻ và nhanh. |
| `compact()` | Lịch sử phình to hơn window. Thay toàn bộ bằng một bản tóm tắt và bắt đầu sạch. |

Caching chỉ hoạt động khi prefix giữ **giống hệt từng byte**: cùng `system`, cùng `tools`, và
các message trước đó không bị đụng tới. Vì vậy harness dựng system prompt một lần và chỉ *nối
thêm* vào `msgs`. Cách compaction cũng theo cùng luật đó: nó thay **toàn bộ** lịch sử bằng một
bản tóm tắt và không phát lại thứ gì cũ hơn. Trên các model hiện tại, một thinking block chỉ hợp
lệ trong đúng hội thoại đã sinh ra nó, nên kiểu "tóm tắt các lượt cũ nhưng giữ nguyên văn các
lượt gần đây" có thể bị từ chối thẳng.

## Kiểm tra

Chạy agent với `WORKDIR` trỏ tới một bản sao `content/` của vault này và một câu hỏi cần đọc vài
file lớn. Từ lượt thứ hai trở đi, `cached` phải chiếm phần lớn `context`. Hạ `COMPACT_AT` xuống
8.000 và xem `context` tụt lại sau một lần compaction trong khi agent vẫn làm tiếp.

## Xem trong Claude Code

- `/context` cho thấy window đang bị chiếm bởi những gì, kể cả những file CLAUDE.md nào đã được
  nạp. CLAUDE.md chính là `AGENT.md` của bạn.
- `/compact focus on the failing test` là `compact()` của bạn, kèm chỉ dẫn. Claude Code cũng tự
  compact khi window đầy dần.
- Output tool lớn được đổ vào `~/.claude/projects/<project>/<session-id>/tool-results/`, chính
  là `clip()` của bạn.
- Claude Code tự lo prompt caching cho bạn. Bạn có thể đo nó từ chính transcript của mình:

```bash
python3 - ~/.claude/projects/<project>/<session-id>.jsonl <<'EOF'
import json, sys
for line in open(sys.argv[1]):
    e = json.loads(line)
    if e.get("type") == "assistant" and "usage" in e["message"]:
        u = e["message"]["usage"]
        cached = u.get("cache_read_input_tokens") or 0
        print("context", u["input_tokens"] + cached + (u.get("cache_creation_input_tokens") or 0), "cached", cached)
EOF
```

(Một response có nhiều content block sẽ hiện thành nhiều dòng.)

## Làm hỏng nó

1. Đưa `datetime.now()` vào `SYSTEM` và dựng lại nó ở mỗi lượt. `cached` rơi về 0. Với các tài
   khoản API mới hơn, request có thể bị từ chối thẳng, vì đổi system prompt là sửa lịch sử. Cách
   sửa là nối thêm một message `{"role": "system", "content": "..."}` tại thời điểm chỉ dẫn thay
   đổi, thay vì viết lại phần đầu.
2. "Compact" bằng cách xoá năm message cũ nhất. `tool_result` đầu tiên còn lại trong danh sách
   giờ trả lời cho một `tool_use` không còn tồn tại, và API trả về lỗi.

## Đáp án

Sự chú ý là hữu hạn. Token không liên quan làm loãng token liên quan, và dữ kiện nằm giữa một
context dài được dùng kém hơn. Append-only giữ cache luôn ấm, và giữ hội thoại hợp lệ trên những
model gắn thinking của chúng với đúng lịch sử đã có.

**Tiếp theo:** [Bước 5 — Subagent]({{< relref "/hands-on/lab-agent-harness/step-5-subagents" >}})
