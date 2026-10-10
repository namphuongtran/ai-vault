# step1.py — a stateless call; the "conversation" is a list you keep
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
