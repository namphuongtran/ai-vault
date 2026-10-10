# sdk_agent.py — the same agent on the Claude Agent SDK (the Claude Code harness as a library)
import asyncio, pathlib, sys
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

async def main():
    options = ClaudeAgentOptions(
        cwd="sandbox",
        model="claude-opus-5-5",
        allowed_tools=["Read", "Grep", "Glob", "Edit", "Bash(python -m pytest *)"],  # pre-approved
        disallowed_tools=["Bash(rm *)", "WebFetch"],
        permission_mode="default",
        max_turns=25,
        mcp_servers={"notes": {"command": sys.executable,
                               "args": [str(pathlib.Path("notes_server.py").resolve())]}},
    )
    prompt = "Make the tests pass, then save a one-line note about the fix."
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            print(message.subtype, message.num_turns, message.total_cost_usd)
            print(message.result)

asyncio.run(main())
