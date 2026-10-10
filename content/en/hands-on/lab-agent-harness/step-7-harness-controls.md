---
title: "Step 7 — Harness controls"
weight: 7
description: Permission rules, hooks and saved sessions — guardrails that live in code, not in the prompt.
---

So far the model can run any shell command. A harness is defined by what it **refuses** to do,
and those [guardrails]({{< relref "guardrails.md" >}}) must live in code, not in the prompt.

By the end of this step you should be able to answer: **why must the rule live in the harness
and not in the prompt?**

## Build

Add permission rules, hooks and saved sessions:

```python
RULES = [  # first match wins: (tool name or *, regex on the arguments, decision)
    ("run_bash", r"\brm\b|-delete|\bsudo\b|\bcurl\b|git\s+push", "deny"),
    ("run_bash", r"^(python -m pytest|ls|cat|grep|sed -n|wc)\b", "allow"),
    ("run_bash", r".*", "ask"),
    ("write_file", r".*", "ask"),
    ("*", r".*", "allow"),
]
ASK = threading.Lock()

def permit(call):
    args = " ".join(str(v) for v in call.input.values())
    for name, pattern, decision in RULES:
        if name in (call.name, "*") and re.search(pattern, args):
            if decision == "ask":
                with ASK:
                    return input(f"\nallow {call.name}: {args[:200]!r}? [y/N] ").strip().lower() == "y"
            return decision == "allow"
    return False

def audit(call, out):                      # a post-hook: one line per tool call
    with open(WORKDIR.parent / "audit.jsonl", "a") as f:
        f.write(json.dumps({"tool": call.name, "input": call.input, "chars": len(out)}) + "\n")

HOOKS = {"pre": [], "post": [audit]}       # a pre-hook returns a reason string to block

def result(call, content, is_error=False):
    return {"type": "tool_result", "tool_use_id": call.id,
            "content": content or "(empty)", "is_error": is_error}

def execute(call):
    if not permit(call):
        return result(call, "Denied by the harness permission rules. Choose another way.", True)
    for hook in HOOKS["pre"]:
        if reason := hook(call):
            return result(call, f"Blocked by a hook: {reason}", True)
    try:
        out, failed = FUNCS[call.name](**call.input), False
    except Exception as e:
        out, failed = f"{type(e).__name__}: {e}", True
    out = clip(call.id, out)
    for hook in HOOKS["post"]:
        hook(call, out)
    return result(call, out, failed)
```

A denial goes back to the model as an ordinary error result, so the model can choose another
way. For sessions, store every message the moment it is appended, one per line, which is the
same shape as Claude Code's JSONL:

```python
def load(session):                         # resume from the last compaction boundary
    path = WORKDIR.parent / "sessions" / f"{session}.jsonl"
    lines = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
    start = max([i for i, m in enumerate(lines) if m["compacted"]], default=0)
    return [{"role": m["role"], "content": m["content"]} for m in lines[start:]]

def save(session, msg, compacted):         # append-only, one message per line
    path = WORKDIR.parent / "sessions" / f"{session}.jsonl"
    path.parent.mkdir(exist_ok=True)
    content = msg["content"]
    if not isinstance(content, str):
        content = [b if isinstance(b, dict) else b.model_dump(mode="json", exclude_none=True) for b in content]
    with open(path, "a") as f:
        f.write(json.dumps({"role": msg["role"], "content": content, "compacted": compacted}) + "\n")
```

In `run()`, add a `session=None` parameter. Start from `msgs = load(session) if session else []`,
and route every append through one helper that also saves. A compaction becomes a boundary
instead of a rewrite:

```python
    def push(msg, compacted=False):
        msgs.append(msg)
        if session:
            save(session, msg, compacted)
    # ...append with push(...) everywhere, and on compaction:
            summary = compact(task, msgs, system, tools, model)
            msgs.clear()
            push(summary, compacted=True)
```

## Check

Ask the agent to *"delete the test file"*. The `rm` is denied and the model reads the
denial. Ask it to edit `calc.py` and you get a prompt. `audit.jsonl` has one line per call. Run
`run("How many files?", session="s1")`, then `run("Name them.", session="s1")`. The second run
knows what the first one found.

## See it in Claude Code

- Permissions live in `settings.json` as `allow`, `ask` and `deny` rules such as
  `Bash(npm run test *)` or `Bash(rm *)`.
- The permission modes are `default`, `acceptEdits`, `plan`, `auto`, `dontAsk` and
  `bypassPermissions`.
- A `PreToolUse` hook that exits with code 2 blocks the call, and its stderr goes back to the
  model, just like your pre-hooks.
- `claude --continue` and `claude --resume` are your `load()`.

The docs say it directly: permission rules are enforced by Claude Code, not by the model.

## Break it

1. Remove the `rm` rule and write *"never delete files"* in `SYSTEM` instead. Then hand the
   agent a task where deleting looks helpful.
2. Get past your own regex with
   `python -c "import shutil; shutil.rmtree('x')"` or `python -m pytest && <anything>`.
   Prefix rules match text, not intent. That is why real harnesses split compound commands and
   still run inside a sandbox.
3. Claude Code evaluates **deny, then ask, then allow**, so an allow can never carve an exception
   out of a deny. Move your broad `("*", r".*", "allow")` to the top of `RULES` and see why that
   precedence exists.

## Answer

The model follows instructions most of the time, and a guardrail has to hold all of the time,
including when a tool result carries a prompt injection. Only code can enforce that.

**Next:** [Step 8 — Plug-ins, and the real thing]({{< relref "/hands-on/lab-agent-harness/step-8-mcp-and-agent-sdk" >}})
