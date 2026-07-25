---
title: "Building with AI (Stage 2)"
linkTitle: "Building with AI"
weight: 4
type: docs
no_list: true
menu:
  main:
    weight: 4
description: >
  Hands-on architecture for building AI systems.
---

Where [Foundations]({{< relref "/foundations" >}}) explains the pieces and
[Deep Dives]({{< relref "/deep-dives" >}}) go deeper, **Stage 2** is about assembling them into
real systems — with diagrams for the architecture.

## Roadmap

```mermaid
flowchart LR
    A[AI system design] --> S[Scaling to production] --> B[Building a RAG system] --> C[Agentic RAG]
    C --> D[The agent harness] --> E[Loop engineering] --> F[From prompts to graphs] --> G[AI code structure] --> H[Tooling and frameworks]
```

## In this section

1. [AI system design]({{< relref "/building/ai-system-design" >}}) — the standard shape of an AI app.
2. [Scaling to production]({{< relref "/building/scaling-to-production" >}}) — gateway, caching, serving, queues, reliability, cost at scale.
3. [Building a RAG system]({{< relref "/building/building-rag" >}}) — end-to-end reference architecture.
4. [Agentic RAG]({{< relref "/building/agentic-rag" >}}) — retrieval driven by an agent, not a fixed pipeline.
5. [The agent harness]({{< relref "/building/agent-harness" >}}) — the loop, context, tools, memory, guardrails.
6. [Loop engineering]({{< relref "/building/loop-engineering" >}}) — designing the loops themselves: closed loops, validators, orchestration.
7. [From prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) — the five engineering disciplines as one evolution.
8. [AI code structure]({{< relref "/building/ai-code-structure" >}}) — how to organize an AI app codebase.
9. [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) — SDKs, frameworks, MCP, deployment.

## Prerequisites

Work through [Stage 0 — Foundations]({{< relref "/foundations" >}}) and
[Stage 1 — Deep Dives]({{< relref "/deep-dives" >}}) first — Stage 2 builds directly on both.
