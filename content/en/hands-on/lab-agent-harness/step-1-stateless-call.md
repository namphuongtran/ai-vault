---
title: "Step 1 — A stateless call"
weight: 1
description: One API call and a list of messages you keep — why a stateless model seems to remember.
---

Start with no tools and no loop: a [single API call]({{< relref "the-ai-api.md" >}}) with a
list of messages that *you* keep.

By the end of this step you should be able to answer: **the API stores nothing between calls,
so why does the model seem to remember?**

## Build

```python
# step1.py
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"

def text_of(r):                       # content can also hold thinking blocks: keep only text
    return "".join(b.text for b in r.content if b.type == "text")

msgs = []
while True:
    msgs.append({"role": "user", "content": input("you> ")})
    r = client.messages.create(model=MODEL, max_tokens=16000, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})   # all blocks, unchanged
    print(text_of(r), f"\n[input_tokens={r.usage.input_tokens}]")
```

## Check

Tell it your name, then ask for it back. `input_tokens` grows every turn, because
every turn sends the whole conversation again.

## See it in Claude Code

Your sessions are stored as JSONL at
`~/.claude/projects/<project>/<session-id>.jsonl`, where `<project>` is the working directory
with every non-alphanumeric character replaced by `-`. Lines of type `user` and `assistant`
carry a `message` with the same `role` and `content` shape you just built. Read one session top
to bottom. The format is internal and changes between versions, so read it but don't build on it.

## Break it

Send only the last message instead of `msgs`. The "memory" disappears at once.

## Answer

It doesn't remember. Your code sends the whole conversation every time, and the context window
is all the model knows on that turn.

**Next:** [Step 2 — One tool]({{< relref "/hands-on/lab-agent-harness/step-2-one-tool" >}})
