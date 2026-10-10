# agent.py — the harness as it stands after step 7
import json, os, pathlib, re, subprocess, threading
from concurrent.futures import ThreadPoolExecutor
import anthropic

client = anthropic.Anthropic()
MODELS = {"main": "claude-opus-5-5", "sub": "claude-haiku-5-5"}
WORKDIR = pathlib.Path(os.environ.get("WORKDIR", "sandbox")).resolve()

SYSTEM = """You are a coding agent working in a small project.
Inspect before you change anything, and verify your work by running the tests before you finish.
Prefer `grep -n` and `sed -n` through run_bash over reading whole large files."""


def text_of(r):
    return "".join(b.text for b in r.content if b.type == "text")


# --- step 3: tools --------------------------------------------------------
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


# --- step 4: context management -------------------------------------------
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


# --- step 7: permissions and hooks -----------------------------------------
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
    except Exception as e:                   # errors are observations, not crashes
        out, failed = f"{type(e).__name__}: {e}", True
    out = clip(call.id, out)
    for hook in HOOKS["post"]:
        hook(call, out)
    return result(call, out, failed)


# --- traces and sessions ---------------------------------------------------
def log(agent, turn, u):
    with open(WORKDIR.parent / "trace.jsonl", "a") as f:
        f.write(json.dumps({"agent": agent, "turn": turn, "context": context_size(u),
                            "cached": u.cache_read_input_tokens or 0, "output": u.output_tokens}) + "\n")

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


# --- the loop --------------------------------------------------------------
def run(task, tools=TOOLS, model=MODELS["main"], effort="medium", max_turns=25,
        agent="main", system=None, session=None):
    system = system or system_prompt()              # built once: frozen for the whole session
    msgs = load(session) if session else []
    def push(msg, compacted=False):
        msgs.append(msg)
        if session:
            save(session, msg, compacted)
    push({"role": "user", "content": task})
    for turn in range(max_turns):
        r = client.messages.create(model=model, max_tokens=16000, system=system, tools=tools,
                                   messages=msgs, output_config={"effort": effort},
                                   cache_control={"type": "ephemeral"})
        log(agent, turn, r.usage)
        push({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return text_of(r)
        calls = [b for b in r.content if b.type == "tool_use"]
        with ThreadPoolExecutor() as pool:          # parallel tool calls run concurrently
            push({"role": "user", "content": list(pool.map(execute, calls))})
        if context_size(r.usage) > COMPACT_AT:
            summary = compact(task, msgs, system, tools, model)
            msgs.clear()
            push(summary, compacted=True)
    return f"Stopped after max_turns={max_turns} without finishing."


# --- step 5: subagents -----------------------------------------------------
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


if __name__ == "__main__":
    import sys
    print(run(" ".join(sys.argv[1:]) or "Make the tests pass. Run them with: python -m pytest -q"))
