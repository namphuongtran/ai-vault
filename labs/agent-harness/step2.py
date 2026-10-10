# step2.py — one tool, one round trip, driven by hand
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
