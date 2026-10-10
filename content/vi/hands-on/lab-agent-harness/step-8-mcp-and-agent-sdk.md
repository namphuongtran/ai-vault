---
title: "Bước 8 — Plug-in, và hàng thật"
linkTitle: "Step 8 — Plug-ins, and the real thing"
weight: 8
description: Một MCP server tự viết, rồi cùng agent đó trên Claude Agent SDK, đối chiếu từng dòng.
---

[MCP]({{< relref "mcp.md" >}}) là một kho đăng ký tool nằm ở đầu bên kia của một đường ống. Giao
thức này không đổi vòng lặp của bạn. Nó chỉ đổi nơi định nghĩa tool đến từ đâu và lời gọi đi về
đâu.

Đến cuối bước này bạn phải trả lời được: **SDK làm gì thay bạn, và việc gì vẫn là của bạn?**

## Xây dựng

Đây là một server hoàn chỉnh:

```python
# notes_server.py
import pathlib
from mcp.server.mcpserver import MCPServer

NOTES = pathlib.Path(__file__).with_name("notes.md")
server = MCPServer("notes")

@server.tool()
def add_note(text: str) -> str:
    """Append one note to the shared notes file."""
    with NOTES.open("a") as f:
        f.write(f"- {text}\n")
    return "saved"

@server.tool()
def read_notes() -> str:
    """Return every saved note."""
    return NOTES.read_text() if NOTES.exists() else "(no notes yet)"

if __name__ == "__main__":
    server.run()                       # mặc định là stdio
```

Cắm nó vào harness của bạn. `list_tools` đưa cho bạn các schema, còn `call_tool` chạy chúng. Vòng
lặp không thay đổi chút nào:

```python
# mcp_bridge.py
import asyncio, sys
from mcp import Client, StdioServerParameters
import agent

async def main(task):
    server = StdioServerParameters(command=sys.executable, args=["notes_server.py"])
    async with Client(server) as mcp:
        loop = asyncio.get_running_loop()
        for t in (await mcp.list_tools()).tools:          # schema MCP -> schema tool của API
            agent.TOOLS.append({"name": t.name, "description": t.description or "",
                                "input_schema": t.input_schema})
            def call(_name=t.name, **args):                # chạy trong một worker thread
                res = asyncio.run_coroutine_threadsafe(mcp.call_tool(_name, args), loop).result()
                return "\n".join(c.text for c in res.content if c.type == "text")
            agent.FUNCS[t.name] = call
        print(await asyncio.to_thread(agent.run, task))

asyncio.run(main("Run the tests, save a one-line note with the result, then list all notes."))
```

Giờ dựng lại toàn bộ agent trên **Claude Agent SDK**, tức chính harness của Claude Code được
đóng gói thành thư viện:

```python
# sdk_agent.py
import asyncio, pathlib, sys
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

async def main():
    options = ClaudeAgentOptions(
        cwd="sandbox",
        model="claude-opus-5-5",
        allowed_tools=["Read", "Grep", "Glob", "Edit", "Bash(python -m pytest *)"],  # duyệt sẵn
        disallowed_tools=["Bash(rm *)", "WebFetch"],
        permission_mode="default",
        max_turns=25,
        mcp_servers={"notes": {"command": sys.executable,
                               "args": [str(pathlib.Path("notes_server.py").resolve())]}},
    )
    prompt = "Make the tests pass, then save a one-line note about the fix."
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            print(message.subtype, message.num_turns, message.total_cost_usd)
            print(message.result)

asyncio.run(main())
```

`allowed_tools` duyệt sẵn các tool. Nó **không** giới hạn agent chỉ dùng những tool đó; việc đó
là của `disallowed_tools` và permission mode.

## Kiểm tra

Đặt `calc.py` về lại bản có bug rồi chạy cả hai phiên bản trên cùng một task. Sau đó tự điền bảng
này từ chính code của bạn:

| Cơ chế | `agent.py` của bạn | Claude Code | Agent SDK |
| --- | --- | --- | --- |
| Vòng lặp | `run()` | có sẵn | `query()` |
| Tool | `TOOLS` + `FUNCS` | Read, Edit, Bash, Grep, Glob... | `allowed_tools`, `disallowed_tools` |
| Context | `clip()`, `compact()`, `AGENT.md`, `cache_control` | `tool-results/`, `/compact`, CLAUDE.md, caching tự động | có sẵn |
| Subagent | `delegate()` | `.claude/agents/*.md` | `agents=` |
| Model theo vai | `MODELS` | `/model`, `model:` trong file subagent | `model=`, `model` riêng cho từng agent |
| Permission | `RULES` + `permit()` | luật `allow` / `ask` / `deny`, permission mode | `permission_mode`, `can_use_tool` |
| Hook | `HOOKS` | `PreToolUse`, `PostToolUse`... | `hooks=` |
| Session | `sessions/*.jsonl` | `~/.claude/projects/...jsonl`, `--resume` | `resume=` |
| Plug-in | `mcp_bridge.py` | `claude mcp add` | `mcp_servers=` |

## Xem trong Claude Code

Cùng server đó chạy nguyên vẹn trong Claude Code:

```bash
claude mcp add notes -- python /absolute/path/to/notes_server.py
```

Dấu `--` tách các option của chính Claude Code khỏi lệnh khởi động server. Chạy `/mcp` trong một
session để xem server và các tool của nó. Chúng hiện ra với tên server làm tiền tố,
`mcp__notes__add_note`, cũng là cái tên bạn dùng trong luật permission.

## Làm hỏng nó

Thêm `print("saving", text)` vào trong `add_note` rồi chạy lại bridge. Qua stdio, **stdout chính
là kênh giao thức**. Dòng print của bạn đến nơi như một dòng không phải JSON-RPC, và client báo
lỗi `Invalid JSON` cho nó. Python SDK bỏ qua dòng đó và chạy tiếp, nhưng một client chặt hơn có
thể ngắt kết nối. Hãy ghi log ra stderr. Rồi đổi docstring của `add_note` thành
`"Does notes stuff"` và xem agent còn biết khi nào nên gọi nó không. Description của MCP tool
cũng là prompt, y như ở bước 2.

## Đáp án

SDK cho bạn vòng lặp, các tool có sẵn, quản lý context, subagent, permission, hook và session.
Thứ vẫn thuộc về bạn là task, các tool riêng cho lĩnh vực của bạn, chính sách permission, và việc
phán xét kết quả có đúng hay không.

**Tiếp theo:** quay về [trang tổng quan của lab]({{< relref "/hands-on/lab-agent-harness" >}}) và
[bốn câu hỏi debug]({{< relref "/hands-on/lab-agent-harness#debug-mọi-agent-bằng-bốn-câu-hỏi" >}}).
