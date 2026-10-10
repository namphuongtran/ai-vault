"""Offline checks for agent.py and mcp_bridge.py.

A scripted fake client stands in for the Messages API, so these tests need no API key and no
network. They check the harness, not the model: the loop, tool results, permissions and hooks,
clipping, compaction, sessions, subagents, and the MCP bridge (which starts a real server).
"""
import asyncio, copy, itertools, json, os, pathlib, shutil, sys, threading

import pytest
from anthropic.types import Message

LAB = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))
os.environ.setdefault("ANTHROPIC_API_KEY", "offline")

import agent  # noqa: E402

ids = itertools.count()
FIXED = "def average(xs):\n    return sum(xs) / len(xs) if xs else 0\n"


# --- a fake Messages API ----------------------------------------------------
def msg(*blocks, ctx=1000):
    """An assistant response: an empty thinking block (as current models send) plus `blocks`."""
    content = [{"type": "thinking", "thinking": "", "signature": "sig"}, *blocks]
    stop = "tool_use" if any(b["type"] == "tool_use" for b in blocks) else "end_turn"
    return Message.model_validate({
        "id": f"msg_{next(ids)}", "type": "message", "role": "assistant", "model": "fake",
        "content": content, "stop_reason": stop, "stop_sequence": None,
        "usage": {"input_tokens": ctx, "output_tokens": 50,
                  "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}})

def use(name, **tool_input):
    return {"type": "tool_use", "id": f"toolu_{next(ids)}", "name": name, "input": tool_input}

def txt(text):
    return {"type": "text", "text": text}

def as_dicts(content):
    if isinstance(content, str):
        return content
    return [b if isinstance(b, dict) else b.model_dump(exclude_none=True) for b in content]

class FakeClient:
    """Plays back a script of responses and records every request the harness sends.

    A script entry is a Message, or a function that receives the request and returns one.
    Requests made with the subagent system prompt go to `sub` instead of the script.
    """
    def __init__(self, script, sub=None):
        self.script, self.sub, self.calls, self.lock = list(script), sub, [], threading.Lock()
        self.messages = self

    def create(self, **kw):
        kw = {**kw, "messages": [{"role": m["role"], "content": as_dicts(m["content"])}
                                 for m in kw["messages"]]}
        check_request(kw)
        with self.lock:
            self.calls.append(copy.deepcopy(kw))
        if self.sub and kw["system"] == agent.SUB_SYSTEM:
            return self.sub(kw)
        with self.lock:
            step = self.script.pop(0)
        return step(kw) if callable(step) else step

def check_request(kw):
    """What the real API would reject: a non-user first turn, or a tool_use with no result."""
    msgs = kw["messages"]
    assert msgs[0]["role"] == "user"
    for prev, nxt in zip(msgs, msgs[1:]):
        if prev["role"] == "assistant":
            asked = {b["id"] for b in prev["content"] if b["type"] == "tool_use"}
            answered = {b["tool_use_id"] for b in nxt["content"]
                        if isinstance(nxt["content"], list) and b.get("type") == "tool_result"}
            assert asked <= answered, f"tool_use without a tool_result: {asked - answered}"
    assert kw.get("cache_control") == {"type": "ephemeral"}


# --- fixtures ----------------------------------------------------------------
@pytest.fixture
def lab(tmp_path, monkeypatch):
    """A private copy of the sandbox; traces, audit and sessions land next to it."""
    shutil.copytree(LAB / "sandbox", tmp_path / "sandbox",
                    ignore=shutil.ignore_patterns(".tool-results", ".pytest_cache", "__pycache__"))
    monkeypatch.setattr(agent, "WORKDIR", tmp_path / "sandbox")
    monkeypatch.setattr("builtins.input", lambda prompt="": "y")       # approve every ask
    monkeypatch.setenv("PATH", f"{pathlib.Path(sys.executable).parent}{os.pathsep}{os.environ['PATH']}")
    return tmp_path

def use_client(monkeypatch, client):
    monkeypatch.setattr(agent, "client", client)
    return client

def lines(path):
    return path.read_text().splitlines() if path.exists() else []


# --- step 3: the loop ----------------------------------------------------------
def test_the_loop_fixes_the_bug(lab, monkeypatch):
    fake = use_client(monkeypatch, FakeClient([
        msg(use("run_bash", command="python -m pytest -q")),
        msg(use("read_file", path="calc.py")),
        msg(use("write_file", path="calc.py", content=FIXED)),
        msg(use("run_bash", command="python -m pytest -q")),
        msg(txt("Fixed both bugs; 2 tests pass.")),
    ]))
    assert agent.run("Make the tests pass.") == "Fixed both bugs; 2 tests pass."

    first = fake.calls[1]["messages"][-1]["content"][0]["content"]
    last = fake.calls[4]["messages"][-1]["content"][0]["content"]
    assert "failed" in first and "2 passed" in last
    assert (lab / "sandbox/calc.py").read_text() == FIXED
    assert len({c["system"] for c in fake.calls}) == 1, "the system prompt must stay frozen"
    assert len(lines(lab / "audit.jsonl")) == 4 and len(lines(lab / "trace.jsonl")) == 5

def test_max_turns_is_the_brake(lab, monkeypatch):
    use_client(monkeypatch, FakeClient([msg(use("list_files", path="."))] * 3))
    assert agent.run("Never finish.", max_turns=3).startswith("Stopped after max_turns=3")


# --- steps 3, 4, 7: errors, denials, clipping ----------------------------------
def test_errors_denials_and_clipping_come_back_as_tool_results(lab, monkeypatch):
    fake = use_client(monkeypatch, FakeClient([
        msg(use("read_file", path="missing.py"),
            use("run_bash", command="rm -rf calc.py"),
            use("run_bash", command="python -c \"print('x' * 10000)\"")),
        msg(txt("done")),
    ]))
    agent.run("Probe the harness.")
    missing, denied, big = fake.calls[1]["messages"][-1]["content"]
    assert missing["is_error"] and "FileNotFoundError" in missing["content"]
    assert denied["is_error"] and "Denied" in denied["content"]
    assert (lab / "sandbox/calc.py").exists()
    assert len(big["content"]) < agent.CLIP_AT + 300 and ".tool-results/" in big["content"]
    assert list((lab / "sandbox/.tool-results").iterdir())

def test_a_pre_hook_can_block_a_call(lab, monkeypatch):
    monkeypatch.setitem(agent.HOOKS, "pre", [lambda call: "frozen" if call.name == "write_file" else None])
    fake = use_client(monkeypatch, FakeClient([
        msg(use("write_file", path="calc.py", content=FIXED)), msg(txt("ok"))]))
    agent.run("Edit calc.py.")
    blocked = fake.calls[1]["messages"][-1]["content"][0]
    assert blocked["is_error"] and "Blocked by a hook: frozen" in blocked["content"]
    assert (lab / "sandbox/calc.py").read_text() != FIXED


# --- step 4: compaction --------------------------------------------------------
def test_compaction_replaces_the_whole_history_with_one_summary(lab, monkeypatch):
    monkeypatch.setattr(agent, "COMPACT_AT", 5_000)

    def summarize(kw):
        last = kw["messages"][-1]["content"]
        assert last[0]["type"] == "tool_result", "the summary request follows a complete tool round"
        assert last[-1]["type"] == "text" and "Do not call any tools" in last[-1]["text"]
        return msg(txt("Task: X. Listed the files. Next: read calc.py."))

    def after(kw):
        assert len(kw["messages"]) == 1 and "Progress so far" in kw["messages"][0]["content"]
        return msg(txt("finished"))

    fake = use_client(monkeypatch, FakeClient([msg(use("list_files", path="."), ctx=9_000), summarize, after]))
    assert agent.run("X") == "finished"
    loop_call, summary_call = fake.calls[0], fake.calls[1]
    assert summary_call["tools"] == loop_call["tools"] and summary_call["system"] == loop_call["system"]


# --- step 7: sessions ------------------------------------------------------------
def test_sessions_are_append_only_and_resume(lab, monkeypatch):
    def resumed(kw):
        assert [m["role"] for m in kw["messages"]] == ["user", "assistant", "user", "assistant", "user"]
        assert kw["messages"][1]["content"][0]["type"] == "thinking"   # blocks round-trip unchanged
        return msg(txt("calc.py and test_calc.py"))

    use_client(monkeypatch, FakeClient([msg(use("list_files", path=".")), msg(txt("Two files.")), resumed]))
    agent.run("How many files?", session="s1")
    agent.run("Name them.", session="s1")
    saved = [json.loads(line) for line in lines(lab / "sessions/s1.jsonl")]
    assert [m["role"] for m in saved] == ["user", "assistant", "user", "assistant", "user", "assistant"]


# --- step 5: subagents -------------------------------------------------------------
def test_subagents_get_a_fresh_context_fewer_tools_and_the_cheaper_model(lab, monkeypatch):
    seen = []

    def sub(kw):
        seen.append((kw["model"], {t["name"] for t in kw["tools"]}))
        if len(kw["messages"]) == 1:                      # fresh context: only the task
            return msg(use("list_files", path="."))
        return msg(txt("report: calc.py, test_calc.py"))

    fake = use_client(monkeypatch, FakeClient(
        [msg(use("delegate", task="List the files"), use("delegate", task="Find the tests")),
         msg(txt("Both reports are in."))], sub=sub))
    assert agent.run("Survey the project with two subagents.") == "Both reports are in."
    assert len(seen) == 4
    assert all(model == agent.MODELS["sub"] and tools == {"list_files", "read_file"} for model, tools in seen)
    reports = [r["content"] for r in fake.calls[-1]["messages"][-1]["content"]]
    assert reports == ["report: calc.py, test_calc.py"] * 2


# --- step 8: MCP -----------------------------------------------------------------
@pytest.fixture
def mcp_bridge(lab, monkeypatch):
    monkeypatch.chdir(LAB)                       # the bridge starts notes_server.py from here
    tools, funcs = len(agent.TOOLS), dict(agent.FUNCS)
    notes = LAB / "notes.md"
    notes.unlink(missing_ok=True)
    import mcp_bridge
    yield mcp_bridge
    del agent.TOOLS[tools:]                      # the bridge registers tools globally
    agent.FUNCS.clear()
    agent.FUNCS.update(funcs)
    notes.unlink(missing_ok=True)

def test_mcp_tools_plug_into_the_unchanged_loop(mcp_bridge, monkeypatch):
    fake = use_client(monkeypatch, FakeClient([
        msg(use("add_note", text="tests pass")), msg(use("read_notes")), msg(txt("Notes listed."))]))
    asyncio.run(mcp_bridge.main("Save a note, then list the notes."))
    assert {"add_note", "read_notes"} <= {t["name"] for t in fake.calls[0]["tools"]}
    assert (LAB / "notes.md").read_text() == "- tests pass\n"
    assert "tests pass" in fake.calls[2]["messages"][-1]["content"][0]["content"]
