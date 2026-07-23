---
title: "Tool & Function Calling"
weight: 11
description: The primitive under agents, skills, plugins, and MCP — letting a model call functions you define.
---

This is the primitive that turns a text generator into something that can *act*. Agents,
skills, plugins, and MCP are all built on it.

## The idea

You give the model a list of **tools** (functions) it's allowed to call. When answering would
need one, the model doesn't run it — it returns a structured request to call it, with
arguments. **Your code runs the function** and hands the result back. The model then continues
with that result in hand.

## The loop

1. You send the prompt **plus** tool definitions.
2. The model replies either with an answer, or with a **tool call** (name + arguments).
3. Your code executes the tool and returns the **result**.
4. The model uses the result to answer — or calls another tool. Repeat until done.

This request → call → result → continue cycle is exactly what an
[agent]({{< relref "/foundations/agents" >}}) automates.

## Defining a tool

A tool is declared with a **name**, a **description** (the model uses this to decide when to
call it), and an **input schema** (typed parameters). Clear names and descriptions matter more
than anything — they're how the model picks the right tool.

## Key points

- **The model never executes anything** — it only *requests* calls; your side runs them and is
  the security boundary.
- **Parallel calls** — a model may request several tools at once; return all results together.
- **Validate inputs and gate risky actions** (see [Guardrails]({{< relref "/foundations/guardrails" >}}));
  the model's requested arguments are untrusted.
- **Structured output** is the sibling idea: constrain the *answer* to a schema, the same way
  tool arguments are constrained.

> Skills, plugins, and [MCP]({{< relref "/foundations/mcp" >}}) are all ways to *supply* tools
> (and context) to a model — the calling mechanism underneath is this.
