---
title: "Bước 3 — Vòng lặp"
linkTitle: "Step 3 — The loop"
weight: 3
description: Bước 2 đặt trong một vòng while — bốn tool, gọi song song, lỗi là quan sát, và một cái phanh.
---

Một [agent]({{< relref "agents.md" >}}) chính là bước 2 đặt trong một vòng `while`.

Đến cuối bước này bạn phải trả lời được: **ai quyết định việc đã xong, và ai quyết định nó phải
dừng?**

## Xây dựng

Bắt đầu `agent.py` với bốn tool và vòng lặp:

```python
# agent.py
import json, os, pathlib, re, subprocess, threading
from concurrent.futures import ThreadPoolExecutor
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
WORKDIR = pathlib.Path(os.environ.get("WORKDIR", "sandbox")).resolve()

SYSTEM = """You are a coding agent working in a small project.
Inspect before you change anything, and verify your work by running the tests before you finish.
Prefer `grep -n` and `sed -n` through run_bash over reading whole large files."""

def text_of(r):
    return "".join(b.text for b in r.content if b.type == "text")

def list_files(path):
    root = WORKDIR / path
    return "\n".join(sorted(str(p.relative_to(WORKDIR)) for p in root.rglob("*") if p.is_file()))

def read_file(path):
    return (WORKDIR / path).read_text()

def write_file(path, content):
    (WORKDIR / path).write_text(content)
    return f"wrote {len(content)} chars to {path}"

def run_bash(command):
    p = subprocess.run(command, shell=True, cwd=WORKDIR, capture_output=True, text=True, timeout=60)
    return f"exit={p.returncode}\n{p.stdout}{p.stderr}"

def tool(fn, description, **params):
    return {"name": fn.__name__, "description": description,
            "input_schema": {"type": "object",
                             "properties": {k: {"type": "string", "description": v}
                                            for k, v in params.items()},
                             "required": list(params)}}

TOOLS = [
    tool(list_files, "List every file under a directory of the project.",
         path="Directory relative to the project root; use . for the root"),
    tool(read_file, "Read a whole text file. For large files prefer run_bash with grep or sed -n.",
         path="File path relative to the project root"),
    tool(write_file, "Create or overwrite a file with the given content.",
         path="File path relative to the project root", content="The complete new file content"),
    tool(run_bash, "Run a shell command in the project root and return exit code, stdout and stderr.",
         command="The command, for example: python -m pytest -q"),
]
FUNCS = {"list_files": list_files, "read_file": read_file,
         "write_file": write_file, "run_bash": run_bash}

def execute(call):
    try:
        out, failed = FUNCS[call.name](**call.input), False
    except Exception as e:                   # lỗi là quan sát, không phải crash
        out, failed = f"{type(e).__name__}: {e}", True
    return {"type": "tool_result", "tool_use_id": call.id,
            "content": out or "(empty)", "is_error": failed}

def run(task, tools=TOOLS, model=MODEL, max_turns=25):
    msgs = [{"role": "user", "content": task}]
    for turn in range(max_turns):                         # cái phanh
        r = client.messages.create(model=model, max_tokens=16000, system=SYSTEM,
                                   tools=tools, messages=msgs)
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":                   # end_turn, max_tokens, refusal...
            return text_of(r)
        calls = [b for b in r.content if b.type == "tool_use"]     # có thể có nhiều cái
        msgs.append({"role": "user", "content": [execute(c) for c in calls]})
    return f"Stopped after max_turns={max_turns} without finishing."

if __name__ == "__main__":
    import sys
    print(run(" ".join(sys.argv[1:]) or "Make the tests pass. Run them with: python -m pytest -q"))
```

Ba chi tiết gánh phần lớn sức nặng ở đây:

- Một response có thể chứa **nhiều** block `tool_use`. Toàn bộ kết quả của chúng quay về trong
  **một** user message.
- Một tool bị lỗi trả về `is_error: true` cùng nội dung lỗi thay vì làm sập chương trình. Model
  đọc lỗi và điều chỉnh.
- `max_turns` là cái phanh. Model quyết định khi nào nó *xong*. Harness quyết định khi nào nó
  *phải dừng*.

## Kiểm tra

Chạy `python agent.py`. Agent chạy test, đọc `calc.py`, viết lại nó, chạy test lần nữa rồi dừng
khi cả hai test đều pass. Không dòng code nào của bạn biết trước các bước đó.

## Xem trong Claude Code

Thêm một hook `PostToolUse` vào `.claude/settings.json` để ghi log mọi tool call (cần `jq`), rồi
`tail -f ~/claude-tool-log.jsonl` trong lúc làm việc:

```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "*",
        "hooks": [{ "type": "command", "command": "jq -c . >> \"$HOME/claude-tool-log.jsonl\"" }] }
    ]
  }
}
```

Mỗi dòng có `tool_name`, `tool_input` và `tool_response`. Đó chính là `execute()` của bạn, nhìn
từ bên ngoài. Để xem cả vòng lặp dưới dạng một luồng sự kiện, chạy
`claude -p "make the tests pass" --output-format stream-json --verbose`.

## Làm hỏng nó

Giao cho nó một task bất khả (`"make test_empty_list_is_zero pass without editing calc.py"`) với
`max_turns=100`, và xem nó đi vòng vòng. Sau đó raise exception bên trong `execute()` thay vì trả
lỗi về, và xem cả lượt chạy chết ngay ở sai lầm đầu tiên.

## Đáp án

Model quyết định việc đã xong bằng cách không yêu cầu tool nữa (`end_turn`). Harness quyết định
nó phải dừng bằng `max_turns` và các ngân sách. Bạn cần cả hai: không có phanh, một model không
bao giờ nói "xong" sẽ chạy mãi.

**Tiếp theo:** [Bước 4 — Quản lý context]({{< relref "/hands-on/lab-agent-harness/step-4-context-management" >}})
