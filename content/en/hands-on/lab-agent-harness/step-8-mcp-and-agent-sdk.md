---
title: "Step 8 — Plug-ins, and the real thing"
weight: 8
description: A hand-written MCP server, then the same agent on the Claude Agent SDK, compared line by line.
---

[MCP]({{< relref "mcp.md" >}}) is a tool registry at the other end of a pipe. The protocol
does not change your loop. It only changes where the tool definitions come from and where the
calls go.

By the end of this step you should be able to answer: **what does the SDK do for you, and what
is still your job?**

## Build

Here is a complete server:

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
    server.run()                       # stdio by default
```

Plug it into your harness. `list_tools` gives you the schemas and `call_tool` runs them. The loop
does not change at all:

```python
# mcp_bridge.py
import asyncio, sys
from mcp import Client, StdioServerParameters
import agent

async def main(task):
    server = StdioServerParameters(command=sys.executable, args=["notes_server.py"])
    async with Client(server) as mcp:
        loop = asyncio.get_running_loop()
        for t in (await mcp.list_tools()).tools:          # MCP schema -> API tool schema
            agent.TOOLS.append({"name": t.name, "description": t.description or "",
                                "input_schema": t.input_schema})
            def call(_name=t.name, **args):                # runs in a worker thread
                res = asyncio.run_coroutine_threadsafe(mcp.call_tool(_name, args), loop).result()
                return "\n".join(c.text for c in res.content if c.type == "text")
            agent.FUNCS[t.name] = call
        print(await asyncio.to_thread(agent.run, task))

asyncio.run(main("Run the tests, save a one-line note with the result, then list all notes."))
```

Now rebuild the whole agent on the **Claude Agent SDK**, which is the Claude Code harness
packaged as a library:

```python
# sdk_agent.py
import asyncio, pathlib, sys
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

async def main():
    options = ClaudeAgentOptions(
        cwd="sandbox",
        model="claude-opus-5-5",
        allowed_tools=["Read", "Grep", "Glob", "Edit", "Bash(python -m pytest *)"],  # pre-approved
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

`allowed_tools` pre-approves tools. It does **not** restrict the agent to them, which is what
`disallowed_tools` and the permission mode are for.

## Check

Reset `calc.py` to the buggy version and run both versions on the same task. Then fill in this
table from your own code:

| Mechanism | Your `agent.py` | Claude Code | Agent SDK |
| --- | --- | --- | --- |
| Loop | `run()` | built in | `query()` |
| Tools | `TOOLS` + `FUNCS` | Read, Edit, Bash, Grep, Glob... | `allowed_tools`, `disallowed_tools` |
| Context | `clip()`, `compact()`, `AGENT.md`, `cache_control` | `tool-results/`, `/compact`, CLAUDE.md, automatic caching | built in |
| Subagents | `delegate()` | `.claude/agents/*.md` | `agents=` |
| Model per role | `MODELS` | `/model`, `model:` in subagent files | `model=`, per-agent `model` |
| Permissions | `RULES` + `permit()` | `allow` / `ask` / `deny` rules, permission modes | `permission_mode`, `can_use_tool` |
| Hooks | `HOOKS` | `PreToolUse`, `PostToolUse`... | `hooks=` |
| Sessions | `sessions/*.jsonl` | `~/.claude/projects/...jsonl`, `--resume` | `resume=` |
| Plug-ins | `mcp_bridge.py` | `claude mcp add` | `mcp_servers=` |

## See it in Claude Code

The same server works unchanged in Claude Code:

```bash
claude mcp add notes -- python /absolute/path/to/notes_server.py
```

The `--` separates Claude Code's own options from the command that starts the server. Run
`/mcp` inside a session to see the server and its tools. They appear with the server name as a
prefix, `mcp__notes__add_note`, which is also the name you use in permission rules.

## Break it

Add `print("saving", text)` inside `add_note` and run the bridge again. Over stdio, **stdout is
the protocol channel**. Your print arrives as a line that is not JSON-RPC, and the client
reports an `Invalid JSON` error for it. The Python SDK skips the line and carries on, but a
stricter client could drop the connection. Log to stderr instead. Then give `add_note` the
docstring `"Does notes stuff"` and see whether the agent still knows when to call it. MCP tool
descriptions are prompts, exactly like the ones in step 2.

## Answer

The SDK gives you the loop, the built-in tools, context management, subagents, permissions,
hooks and sessions. What you still own is the task, the tools specific to your domain, the
permission policy, and deciding whether the result is right.

**Next:** back to the [lab overview]({{< relref "/hands-on/lab-agent-harness" >}}) and its
[four debugging questions]({{< relref "/hands-on/lab-agent-harness#debug-any-agent-with-four-questions" >}}).
