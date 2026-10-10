# Lab 2 — Build Your Own Agent Harness: example code

The finished code for [Lab 2](../../content/en/hands-on/lab-agent-harness/_index.md). It is a
reference. Write your own version step by step first, then compare.

Each step's page shows only what that step adds. This folder holds the assembled result.

## Files

| File | Step | What it is |
| --- | --- | --- |
| [`step1.py`](step1.py) | [1 — A stateless call](../../content/en/hands-on/lab-agent-harness/step-1-stateless-call.md) | A chat loop over a message list you keep |
| [`step2.py`](step2.py) | [2 — One tool](../../content/en/hands-on/lab-agent-harness/step-2-one-tool.md) | One `tool_use` → `tool_result` round trip, by hand |
| [`agent.py`](agent.py) | [3](../../content/en/hands-on/lab-agent-harness/step-3-the-loop.md)–[7](../../content/en/hands-on/lab-agent-harness/step-7-harness-controls.md) | The harness after step 7: tools, loop, context management, subagents, permissions, hooks, sessions |
| [`bench.py`](bench.py) | [6 — A model per role](../../content/en/hands-on/lab-agent-harness/step-6-model-per-role.md) | The same tasks across models and effort levels, with computed ground truth |
| [`notes_server.py`](notes_server.py) | [8 — Plug-ins, and the real thing](../../content/en/hands-on/lab-agent-harness/step-8-mcp-and-agent-sdk.md) | A complete MCP server with two tools |
| [`mcp_bridge.py`](mcp_bridge.py) | 8 | Plugs the MCP server's tools into `agent.py`. The loop does not change |
| [`sdk_agent.py`](sdk_agent.py) | 8 | The same agent on the Claude Agent SDK |
| [`sandbox/`](sandbox) | 3 onward | The project the agent works on: two files with two bugs, on purpose |
| [`tests/test_offline.py`](tests/test_offline.py) | — | Offline checks of the harness against a scripted fake client |

## Setup

Run everything from this folder. The code uses paths relative to it.

```bash
cd labs/agent-harness
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # not needed for the offline tests
```

Keep the virtual environment activated. The agent runs `python -m pytest` in its own shell and
needs to find the same `python`.

## Run it

```bash
python step1.py                     # step 1: chat, and watch input_tokens grow
python step2.py                     # step 2: one tool call, driven by hand
python agent.py                     # steps 3–7: the agent fixes sandbox/calc.py
git checkout -- sandbox/            # put the bugs back for the next run

cp -R ../../content/en vault        # step 6: a corpus to benchmark on
WORKDIR=vault python bench.py

python mcp_bridge.py                # step 8: MCP tools inside your own harness
python sdk_agent.py                 # step 8: the same agent on the Agent SDK
claude mcp add notes -- python "$PWD/notes_server.py"   # step 8: the same server in Claude Code
```

`agent.py` asks before it runs an unlisted shell command or writes a file, and it refuses
commands like `rm`. While it runs, it writes `trace.jsonl` (one line per model call),
`audit.jsonl` (one line per tool call), `sessions/` and `sandbox/.tool-results/`. All of them
are git-ignored.

## Offline tests

```bash
python -m pytest tests -q
```

These tests need no API key and no network. A fake client plays back scripted model responses,
so the tests exercise the **harness**, not the model:

- the loop and its `max_turns` brake
- errors, denials and hook blocks returned as tool results
- output clipping
- compaction into a single summary
- append-only sessions that resume
- subagents with a fresh context, read-only tools and the cheaper model
- the MCP bridge, which starts the real `notes_server.py`

Every fake request is also checked for what the real API would reject: a first turn that is
not from the user, or a `tool_use` with no matching `tool_result`.

## Notes

- **Models:** `claude-opus-5-5` for the main agent and `claude-haiku-5-5` for subagents. Change
  `MODELS` in `agent.py`.
- **Tested with:** `anthropic` 1.13, `mcp` 2.3 (the server uses `MCPServer`, which replaced
  `FastMCP` in 2.x), `claude-agent-sdk` 0.2.165, and Python 3.12.
- **Safety:** the regex permission rules are a lesson, not a sandbox. `run_bash` executes real
  shell commands in `WORKDIR`. Run the agent in a container for anything you don't fully trust.
