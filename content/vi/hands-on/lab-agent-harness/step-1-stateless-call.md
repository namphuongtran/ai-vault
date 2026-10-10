---
title: "Bước 1 — Một lời gọi stateless"
linkTitle: "Step 1 — A stateless call"
weight: 1
description: Một lời gọi API và một danh sách message do bạn giữ — vì sao một model stateless lại có vẻ nhớ.
---

Bắt đầu khi chưa có tool, chưa có vòng lặp: một [lời gọi API đơn lẻ]({{< relref "the-ai-api.md" >}})
với một danh sách message do *chính bạn* giữ.

Đến cuối bước này bạn phải trả lời được: **API không lưu gì giữa các lần gọi, vậy vì sao model
có vẻ nhớ?**

## Xây dựng

```python
# step1.py
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"

def text_of(r):                       # content có thể chứa cả thinking block: chỉ lấy text
    return "".join(b.text for b in r.content if b.type == "text")

msgs = []
while True:
    msgs.append({"role": "user", "content": input("you> ")})
    r = client.messages.create(model=MODEL, max_tokens=16000, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})   # mọi block, giữ nguyên
    print(text_of(r), f"\n[input_tokens={r.usage.input_tokens}]")
```

## Kiểm tra

Nói cho nó biết tên bạn, rồi hỏi lại. `input_tokens` tăng sau mỗi lượt, vì mỗi lượt đều gửi
lại toàn bộ hội thoại.

## Xem trong Claude Code

Các session của bạn được lưu dạng JSONL tại `~/.claude/projects/<project>/<session-id>.jsonl`,
trong đó `<project>` là thư mục làm việc với mọi ký tự không phải chữ hay số được thay bằng
`-`. Các dòng có type `user` và `assistant` mang một `message` có đúng cấu trúc `role` và
`content` mà bạn vừa dựng. Đọc một session từ đầu đến cuối. Định dạng này là nội bộ và thay đổi
giữa các phiên bản, nên hãy đọc nó nhưng đừng xây gì dựa trên nó.

## Làm hỏng nó

Chỉ gửi message cuối cùng thay vì `msgs`. "Trí nhớ" biến mất ngay lập tức.

## Đáp án

Nó không nhớ. Code của bạn gửi toàn bộ hội thoại mỗi lần, và context window là tất cả những gì
model biết trong lượt đó.

**Tiếp theo:** [Bước 2 — Một tool]({{< relref "/hands-on/lab-agent-harness/step-2-one-tool" >}})
