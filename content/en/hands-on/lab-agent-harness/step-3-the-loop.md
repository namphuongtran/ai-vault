---
title: "Step 3 — The loop"
weight: 3
description: Step 2 in a while loop — four tools, parallel calls, errors as observations, and a brake.
---

An [agent]({{< relref "agents.md" >}}) is step 2 in a `while` loop.

By the end of this step you should be able to answer: **who decides that the work is finished,
and who decides that it must stop?**

## Build

Start `agent.py` with four tools and the loop:

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
    except Exception as e:                   # errors are observations, not crashes
        out, failed = f"{type(e).__name__}: {e}", True
    return {"type": "tool_result", "tool_use_id": call.id,
            "content": out or "(empty)", "is_error": failed}

def run(task, tools=TOOLS, model=MODEL, max_turns=25):
    msgs = [{"role": "user", "content": task}]
    for turn in range(max_turns):                         # the brake
        r = client.messages.create(model=model, max_tokens=16000, system=SYSTEM,
                                   tools=tools, messages=msgs)
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":                   # end_turn, max_tokens, refusal...
            return text_of(r)
        calls = [b for b in r.content if b.type == "tool_use"]     # may be several
        msgs.append({"role": "user", "content": [execute(c) for c in calls]})
    return f"Stopped after max_turns={max_turns} without finishing."

if __name__ == "__main__":
    import sys
    print(run(" ".join(sys.argv[1:]) or "Make the tests pass. Run them with: python -m pytest -q"))
```

Three details carry most of the weight here:

- One response can hold **several** `tool_use` blocks. All their results go back in **one**
  user message.
- A failing tool returns `is_error: true` and the error text instead of crashing the program.
  The model reads the error and adapts.
- `max_turns` is the brake. The model decides when it is *done*. The harness decides when it
  *must stop*.

## Check

Run `python agent.py`. The agent runs the tests, reads `calc.py`, rewrites it, runs the
tests again and stops with both passing. No line of your code knew the steps in advance.

## See it in Claude Code

Add a `PostToolUse` hook to `.claude/settings.json` that logs every
tool call (it needs `jq`), then `tail -f ~/claude-tool-log.jsonl` while you work:

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

Each line has `tool_name`, `tool_input` and `tool_response`. It is your `execute()`, seen from
the outside. For the whole loop as a stream of events, run
`claude -p "make the tests pass" --output-format stream-json --verbose`.

## Break it

Give it an impossible task (`"make test_empty_list_is_zero pass without editing
calc.py"`) with `max_turns=100`, and watch it go round in circles. Then raise an exception
inside `execute()` instead of returning it, and see the whole run die on the first mistake.

## Answer

The model decides it is finished by not asking for a tool (`end_turn`). The harness decides it
must stop with `max_turns` and budgets. You need both: without the brake, a model that never
says it is done runs for ever.

**Next:** [Step 4 — Context management]({{< relref "/hands-on/lab-agent-harness/step-4-context-management" >}})
