---
title: "Step 2 — One tool"
weight: 2
description: A tool is a name, a description and a schema; the model asks, your code acts.
---

A [tool]({{< relref "tool-function-calling.md" >}}) is a name, a description and a JSON
schema. The model never runs anything. It *asks*, and your code decides what happens.

By the end of this step you should be able to answer: **who executes the tool, and what is a
tool description really?**

## Build

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
print(r.stop_reason)                                  # tool_use: the model is asking
call = next(b for b in r.content if b.type == "tool_use")
print(call.name, call.input)                          # read_file {'path': 'sandbox/calc.py'}

output = pathlib.Path(call.input["path"]).read_text()  # YOUR code runs the tool
msgs += [{"role": "assistant", "content": r.content},
         {"role": "user", "content": [{"type": "tool_result", "tool_use_id": call.id,
                                       "content": output}]}]
r = client.messages.create(model=MODEL, max_tokens=16000, tools=TOOLS, messages=msgs)
print("".join(b.text for b in r.content if b.type == "text"))
```

## Check

The first response stops with `tool_use` and has no answer in it. The second one
finds the off-by-one bug, using text that only your code could have read.

## See it in Claude Code

Every tool definition is part of the prompt on every turn. Run
`/context` to see what is using the window before you have typed anything, then connect one more
MCP server and run it again.

## Break it

Change the description to `"Reads stuff"` and ask questions that need two files,
and watch it guess instead of reading. Then return `"Error: no such file"` for a real path and
watch it recover, or give up.

## Answer

Your code executes the tool, every time. A tool description is prompt text, and the model
decides whether and how to call the tool from that text alone.

**Next:** [Step 3 — The loop]({{< relref "/hands-on/lab-agent-harness/step-3-the-loop" >}})
