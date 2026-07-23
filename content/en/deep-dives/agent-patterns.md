---
title: "Agent Patterns"
weight: 2
description: The ReAct loop, tool design, memory, multi-agent, and reflection.
---

Builds on [Agents in Foundations]({{< relref "/foundations/agents" >}}). Patterns for making
agents reliable rather than just capable.

## The ReAct loop

Most agents run a **Reason → Act → Observe** loop: the model reasons about the next step,
calls a tool (act), reads the result (observe), and repeats until done. Explicit reasoning
between actions improves tool choice and makes traces debuggable.

## Tool design

Tools are the agent's API to the world — design them like a good API.

- **Few, well-named tools** beat many overlapping ones.
- Clear descriptions and typed parameters; the model picks tools from these.
- Return concise, structured results; trim noise before it re-enters context.
- Make tools **idempotent** where possible, and validate inputs (see
  [Guardrails]({{< relref "/foundations/guardrails" >}})).

## Planning

- **Decomposition** — break a goal into ordered sub-tasks before acting.
- **Plan-and-execute** — plan once, then execute steps (cheaper, more predictable) vs.
  re-planning every step (more adaptive).

## Memory

- **Short-term** — the working context for the current task (recent steps, scratchpad).
- **Long-term** — facts persisted across sessions, usually retrieved via RAG.
- Summarize or evict old steps so context stays within the window.

## Multi-agent

Split work across specialized agents when one context can't hold it all:

- **Orchestrator–worker** — a coordinator delegates sub-tasks to focused workers.
- **Review/critique** — one agent produces, another checks.

More agents means more coordination cost — use it only when a single agent genuinely struggles.

## Reflection

Have the agent evaluate its own output against the goal and retry if it falls short. Cheap
and effective for tasks with a checkable result (tests pass, schema valid, sources cited).

## Common failure modes

- **Loops** — repeating the same action; add step limits and loop detection.
- **Hallucinated tools/args** — constrain with schemas and validate calls.
- **Context bloat** — summarize; don't append everything forever.
- **No stopping condition** — define explicit success criteria.
