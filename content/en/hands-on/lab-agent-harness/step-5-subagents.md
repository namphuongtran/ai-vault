---
title: "Step 5 — Subagents"
weight: 5
description: Your run() called again with a fresh context, fewer tools and a cheaper model.
---

A subagent is not a new kind of thing. It is **your `run()` called again** with a fresh
`msgs`, its own system prompt, fewer tools, and often a cheaper model. Only its final report
comes back. The main reason to use one is to **isolate context**. Parallelism comes second.

By the end of this step you should be able to answer: **when should you *not* use a subagent?**

## Build

```python
MODELS = {"main": "claude-opus-5-5", "sub": "claude-haiku-5-5"}
READ_ONLY = [t for t in TOOLS if t["name"] in ("list_files", "read_file")]
SUB_SYSTEM = "You are a research subagent. Read only what the task needs, then report briefly."

def delegate(task):
    return run(task + "\n\nEnd with a short report: findings and file paths only.",
               tools=READ_ONLY, model=MODELS["sub"], effort="low", max_turns=15,
               agent="sub", system=SUB_SYSTEM)

TOOLS.append(tool(delegate,
    "Hand a self-contained, read-only research subtask to a subagent with a fresh context. "
    "It returns only a short report. Call it several times in one turn to run subtasks in parallel.",
    task="Complete instructions. The subagent sees nothing of this conversation."))
FUNCS["delegate"] = delegate
```

`run()` grows `effort`, `agent` and `system` parameters: use `system = system or system_prompt()`,
and `effort` goes in as `output_config={"effort": effort}`. Then make one change so that parallel
calls really run at the same time:

```python
        with ThreadPoolExecutor() as pool:          # parallel tool calls run concurrently
            msgs.append({"role": "user", "content": list(pool.map(execute, calls))})
```

Note that `READ_ONLY` is taken **before** `delegate` is added, so subagents cannot spawn
subagents.

## Check

With `WORKDIR` on the vault copy, ask *"Which pages discuss subagents, and what does
each say about when to use them? Use one subagent per top-level section."* The main agent's
context stays small. The subagents read the pages. Then add up the tokens of every call:
the **total is higher** than the same question answered by one agent. Anthropic reports that, in its
data, multi-agent systems use about 15× the tokens of a chat. Isolation costs money.

## See it in Claude Code

Create `.claude/agents/reviewer.md`:

```markdown
---
name: reviewer
description: Reviews a diff for bugs. Use after code changes.
tools: Read, Grep, Glob
model: haiku
---
You review code changes for correctness bugs. Report file:line and one sentence per finding.
```

The frontmatter is your `delegate()` signature, and the body is its `SUB_SYSTEM`. Each
subagent runs in its own context window. Its transcript lands in
`~/.claude/projects/<project>/<session-id>/subagents/`.

## Break it

Let two subagents edit the same file at once. One overwrites the other. Then give a
subagent the task *"fix it"* with no context. It has never seen the conversation, so it has no
idea what "it" is.

## Answer

Don't use a subagent when the subtasks share state or must happen in sequence, when they write
to the same files, or when the task is small enough that the extra tokens buy nothing.

**Next:** [Step 6 — A model per role]({{< relref "/hands-on/lab-agent-harness/step-6-model-per-role" >}})
