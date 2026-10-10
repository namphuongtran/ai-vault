# mcp_bridge.py — plug an MCP server's tools into agent.py; the loop does not change
import asyncio, sys
from mcp import Client, StdioServerParameters
import agent

async def main(task):
    server = StdioServerParameters(command=sys.executable, args=["notes_server.py"])
    async with Client(server) as mcp:
        loop = asyncio.get_running_loop()
        for t in (await mcp.list_tools()).tools:          # MCP schema -> API tool schema
            agent.TOOLS.append({"name": t.name, "description": t.description or "",
                                "input_schema": t.input_schema})
            def call(_name=t.name, **args):                # runs in a worker thread
                res = asyncio.run_coroutine_threadsafe(mcp.call_tool(_name, args), loop).result()
                return "\n".join(c.text for c in res.content if c.type == "text")
            agent.FUNCS[t.name] = call
        print(await asyncio.to_thread(agent.run, task))

if __name__ == "__main__":
    asyncio.run(main("Run the tests, save a one-line note with the result, then list all notes."))
