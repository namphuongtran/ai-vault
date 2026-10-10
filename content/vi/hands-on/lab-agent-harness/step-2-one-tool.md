---
title: "Bước 2 — Một tool"
linkTitle: "Step 2 — One tool"
weight: 2
description: Một tool là một cái tên, một description và một schema; model yêu cầu, code của bạn hành động.
---

Một [tool]({{< relref "tool-function-calling.md" >}}) là một cái tên, một description và một
JSON schema. Model không bao giờ tự chạy thứ gì. Nó *yêu cầu*, còn code của bạn quyết định điều
gì xảy ra.

Đến cuối bước này bạn phải trả lời được: **ai thực thi tool, và rốt cuộc tool description là
gì?**

## Xây dựng

```python
# step2.py
import pathlib
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
TOOLS = [{
    "name": "read_file",
    "description": "Read a text file from the project and return its full contents. "
                   "Use it before answering any question about what a file contains.",
    "input_schema": {"type": "object",
                     "properties": {"path": {"type": "string",
                                             "description": "Path relative to the project root"}},
                     "required": ["path"]},
}]

msgs = [{"role": "user", "content": "What does sandbox/calc.py do? Is it correct?"}]
r = client.messages.create(model=MODEL, max_tokens=16000, tools=TOOLS, messages=msgs)
print(r.stop_reason)                                  # tool_use: model đang yêu cầu
call = next(b for b in r.content if b.type == "tool_use")
print(call.name, call.input)                          # read_file {'path': 'sandbox/calc.py'}

output = pathlib.Path(call.input["path"]).read_text()  # code CỦA BẠN chạy tool
msgs += [{"role": "assistant", "content": r.content},
         {"role": "user", "content": [{"type": "tool_result", "tool_use_id": call.id,
                                       "content": output}]}]
r = client.messages.create(model=MODEL, max_tokens=16000, tools=TOOLS, messages=msgs)
print("".join(b.text for b in r.content if b.type == "text"))
```

## Kiểm tra

Response đầu tiên dừng với `tool_use` và không có câu trả lời nào trong đó. Response thứ hai tìm
ra bug lệch một đơn vị, dựa trên nội dung mà chỉ code của bạn mới đọc được.

## Xem trong Claude Code

Mọi định nghĩa tool đều là một phần của prompt ở mọi lượt. Chạy `/context` để xem window đã bị
chiếm những gì trước khi bạn gõ chữ nào, rồi kết nối thêm một MCP server và chạy lại.

## Làm hỏng nó

Đổi description thành `"Reads stuff"` rồi hỏi những câu cần đọc hai file, và xem nó đoán thay vì
đọc. Sau đó trả về `"Error: no such file"` cho một đường dẫn có thật, và xem nó tự gỡ, hay bỏ
cuộc.

## Đáp án

Code của bạn thực thi tool, lần nào cũng vậy. Tool description là văn bản prompt, và model quyết
định có gọi tool hay không, gọi thế nào, chỉ dựa vào văn bản đó.

**Tiếp theo:** [Bước 3 — Vòng lặp]({{< relref "/hands-on/lab-agent-harness/step-3-the-loop" >}})
