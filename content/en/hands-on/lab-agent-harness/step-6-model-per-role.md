---
title: "Step 6 — A model per role"
weight: 6
description: Measure cost per finished task across models and effort levels, with computed ground truth.
---

[Choosing a model]({{< relref "choosing-a-model.md" >}}) is a measurement, not a feeling. The
honest unit is **cost per finished task**, not price per token. A cheap model that needs three
times the turns, or a second attempt, is not cheap.

By the end of this step you should be able to answer: **when does the smaller model win
overall?**

## Build

Add a trace line, and call `log(agent, turn, r.usage)` right after each `create()` in
`run()`:

```python
def log(agent, turn, u):
    with open(WORKDIR.parent / "trace.jsonl", "a") as f:
        f.write(json.dumps({"agent": agent, "turn": turn, "context": context_size(u),
                            "cached": u.cache_read_input_tokens or 0, "output": u.output_tokens}) + "\n")
```

Then measure the same tasks across models and effort levels. The ground truth is computed from
the files, never typed in by hand. The benchmark gives the agent only the read-only tools, so it
cannot change anything, and the grading is strict on purpose: following the requested format is
part of the job.

```python
# bench.py — run with WORKDIR=vault (a copy of this vault's content/en)
import itertools, json, re, time
import agent

ROOT = agent.WORKDIR
def front(path, key):
    return re.search(rf"^{key}:\s*\"?(.+?)\"?$", (ROOT / path).read_text(), re.M).group(1)

TASKS = [
    ("How many .md files are under deep-dives/, including subfolders? Reply with the number only.",
     str(len(list((ROOT / "deep-dives").rglob("*.md"))))),
    ("What is the front-matter weight of building/agent-harness.md? Reply with the number only.",
     front("building/agent-harness.md", "weight")),
    ("What is the title of building/loop-engineering/levels.md? Reply with the title only.",
     front("building/loop-engineering/levels.md", "title")),
    ("Which page under deep-dives/ has the most lines? Reply with its path only.",
     str(max((ROOT / "deep-dives").rglob("*.md"), key=lambda p: len(p.read_text().splitlines())).relative_to(ROOT))),
]

for model, effort in itertools.product(["claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"],
                                       ["low", "medium"]):
    tag, ok, t0 = f"{model}/{effort}", 0, time.time()
    for i, (q, expected) in enumerate(TASKS):
        answer = agent.run(q, tools=agent.READ_ONLY, model=model, effort=effort,
                           max_turns=15, agent=f"{tag}#{i}")
        ok += answer.strip().strip("`'\".").lower() == expected.lower()   # strict on purpose
    rows = [json.loads(l) for l in open(ROOT.parent / "trace.jsonl") if tag in l]
    print(f"{tag:26} solved {ok}/{len(TASKS)}  turns {len(rows):3}  "
          f"context tokens {sum(r['context'] for r in rows):8}  output {sum(r['output'] for r in rows):6}  "
          f"{time.time() - t0:5.0f}s")
```

## Check

You get a table of your own numbers: success, turns, tokens and seconds per model and
effort. Multiply the tokens by the prices on the pricing page. No numbers are printed here on
purpose. Yours are the ones that count, and they change with every model release.

## See it in Claude Code

`/model sonnet` switches mid-session. The `model:` line in a
subagent file is your `MODELS["sub"]`.

## Break it

Add a task that needs several hops, such as *"which page links to the page with
the most headings?"* Watch the smallest model at `low` effort answer quickly and wrongly. Then
check whether the biggest model at `low` effort beats the middle one at `medium`.

## Answer

The small model wins on narrow, well-specified, high-volume work with checkable outputs, where
it finishes in a similar number of turns. Measure cost per *finished* task.

**Next:** [Step 7 — Harness controls]({{< relref "/hands-on/lab-agent-harness/step-7-harness-controls" >}})
