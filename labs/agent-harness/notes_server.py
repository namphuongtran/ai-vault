# notes_server.py — a whole MCP server: two tools behind a stdio pipe
import pathlib
from mcp.server.mcpserver import MCPServer

NOTES = pathlib.Path(__file__).with_name("notes.md")
server = MCPServer("notes")

@server.tool()
def add_note(text: str) -> str:
    """Append one note to the shared notes file."""
    with NOTES.open("a") as f:
        f.write(f"- {text}\n")
    return "saved"

@server.tool()
def read_notes() -> str:
    """Return every saved note."""
    return NOTES.read_text() if NOTES.exists() else "(no notes yet)"

if __name__ == "__main__":
    server.run()                       # stdio by default
