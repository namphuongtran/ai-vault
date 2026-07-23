---
title: "MCP (Model Context Protocol)"
weight: 13
description: The open standard for connecting tools and data to models — what it is and why it exists.
---

**MCP (Model Context Protocol)** is an open standard for connecting models to external tools
and data. Think of it as a common plug: instead of hand-wiring every integration, you connect
to MCP servers that expose capabilities in a standard shape.

## The problem it solves

Before MCP, every app wired up [tools]({{< relref "/foundations/tool-function-calling" >}}) and
data sources in its own bespoke way. N apps × M integrations meant rebuilding the same
connectors over and over. MCP standardizes the interface so an integration is written **once**
and reused by any MCP-compatible app.

## How it fits together

- **MCP server** — exposes capabilities (a GitHub server, a database server, a filesystem
  server, …).
- **MCP client / host** — the app or agent that connects to servers and makes their
  capabilities available to the model.

A server can expose three things:

- **Tools** — functions the model can call (see [Tool & function calling]({{< relref "/foundations/tool-function-calling" >}})).
- **Resources** — data/context the model can read (files, records).
- **Prompts** — reusable prompt templates.

## Why it matters to you

- **Reuse over rebuild** — connect to an existing server instead of writing a connector.
- **Portability** — the same server works across any MCP-compatible client.
- **It's the backbone of the ecosystem** — many "connectors", "skills", and "plugins" are MCP
  servers under the hood.

> *What* MCP is belongs in foundations. *Building* an MCP server is a build-stage topic — later.
