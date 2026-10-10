---
title: "Step 4 — Context management"
weight: 4
description: Clip, retrieve just in time, remember, cache, compact — and why history must be append-only.
---

Every turn adds to `msgs`, and nothing ever leaves. [Context
engineering]({{< relref "context-engineering.md" >}}) is the work of keeping that window small
and useful.

By the end of this step you should be able to answer: **why can *more* context make an agent
*worse*, and why must the history be append-only?**

## Build

Add four techniques:

```python
CLIP_AT = 4_000          # characters one tool result may put into the context
COMPACT_AT = 60_000      # tokens of context that trigger compaction

def clip(call_id, out):
    if len(out) <= CLIP_AT:
        return out
    spill = WORKDIR / ".tool-results" / f"{call_id}.txt"
    spill.parent.mkdir(exist_ok=True)
    spill.write_text(out)
    return (out[:CLIP_AT] + f"\n[... {len(out) - CLIP_AT} more characters. Full output saved to "
            f".tool-results/{call_id}.txt; search it with run_bash grep instead of reading it whole.]")

def system_prompt():
    notes = WORKDIR / "AGENT.md"           # project memory, loaded once per session
    return SYSTEM + (f"\n\n# Project notes\n{notes.read_text()}" if notes.exists() else "")

def context_size(u):
    return u.input_tokens + (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0)

SUMMARIZE = """Summarize this session so a fresh context can continue it without redoing work:
the task, decisions and constraints, what was tried and what failed, the current state of the
files, and what is left to do. Keep names, paths, numbers and error messages exact.
Do not call any tools; respond with text only."""

def compact(task, msgs, system, tools, model):
    # Only called right after a full tool round, so no tool_use is left waiting for its result.
    ask = msgs[:-1] + [{"role": "user", "content": msgs[-1]["content"] + [{"type": "text", "text": SUMMARIZE}]}]
    r = client.messages.create(model=model, max_tokens=16000, system=system, tools=tools,
                               messages=ask, cache_control={"type": "ephemeral"})  # same prefix: cache hit
    return {"role": "user", "content": f"{task}\n\n# Progress so far\n{text_of(r)}\n\nContinue from here."}
```

In `execute()`, pass the output through `clip()` before you return it. Then change `run()`:

```python
def run(task, tools=TOOLS, model=MODEL, max_turns=25):
    system = system_prompt()                              # built once: frozen for the session
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

Each technique answers a different problem:

| Technique | Problem it solves |
| --- | --- |
| `clip()` + spill to a file | One huge tool output swamps the window. Keep a preview and a pointer to the rest. |
| `grep` and `sed -n` in the system prompt | *Just-in-time* retrieval: fetch the three lines you need, not the whole file. |
| `AGENT.md` | Knowledge that should survive between sessions: memory loaded once at the start. |
| `cache_control` | The repeated prefix is billed and processed again every turn. Caching makes re-reading it cheap and fast. |
| `compact()` | The history outgrows the window. Replace all of it with a summary and start clean. |

Caching only works if the prefix stays **byte-identical**: the same `system`, the same `tools`,
and earlier messages left alone. So the harness builds the system prompt once and only ever
*appends* to `msgs`. The compaction shape follows the same rule. It replaces the **whole**
history with one summary and replays nothing older. On current models a thinking block is valid
only in the conversation that produced it, so "summarize the old turns but keep the recent ones
verbatim" can be rejected outright.

## Check

Run the agent with `WORKDIR` pointing at a copy of this vault's `content/` and a
question that needs several big files. From the second turn on, `cached` should cover most of
`context`. Lower `COMPACT_AT` to 8,000 and watch `context` drop back after a compaction while the
agent carries on.

## See it in Claude Code

- `/context` shows what is using the window, including which CLAUDE.md files loaded.
  CLAUDE.md is your `AGENT.md`.
- `/compact focus on the failing test` is your `compact()`, with instructions. Claude Code also
  compacts automatically as the window fills.
- Large tool outputs are spilled into `~/.claude/projects/<project>/<session-id>/tool-results/`,
  which is your `clip()`.
- Claude Code handles prompt caching for you. You can measure it from your own transcripts:

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

(A response with several content blocks shows up as several lines.)

## Break it

1. Put `datetime.now()` into `SYSTEM` and rebuild it on every turn. `cached` drops to zero.
   On newer API accounts the request can be rejected outright, because changing the system prompt
   is an edit to history. The fix is to append a `{"role": "system", "content": "..."}` message
   at the point where the instruction changes, instead of rewriting the top.
2. "Compact" by deleting the oldest five messages. The first `tool_result` left in the list now
   answers a `tool_use` that no longer exists, and the API returns an error.

## Answer

Attention is finite. Irrelevant tokens dilute the relevant ones, and facts in the middle of a
long context get used less well. Append-only keeps the cache warm and keeps the conversation
valid on models that bind their thinking to the exact history.

**Next:** [Step 5 — Subagents]({{< relref "/hands-on/lab-agent-harness/step-5-subagents" >}})
