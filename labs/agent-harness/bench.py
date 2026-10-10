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
