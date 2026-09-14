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
    A[AI system design] --> S[Scaling to production] --> V[Serving models] --> B[Building a RAG system]
    B --> C[Agentic RAG] --> D[The agent harness] --> E[Loop engineering]
    E --> F[From prompts to graphs] --> G[AI code structure] --> H[Tooling and frameworks]
```

## In this section

1. [AI system design]({{< relref "/building/ai-system-design" >}}) — the standard shape of an AI app.
2. [Scaling to production]({{< relref "/building/scaling-to-production" >}}) — gateway, caching, serving, queues, reliability, cost at scale.
3. [Serving models]({{< relref "/building/serving-models" >}}) — the inference layer: self-hosting, quantization, engines, queuing, routing.
4. [Building a RAG system]({{< relref "/building/building-rag" >}}) — end-to-end reference architecture.
5. [Agentic RAG]({{< relref "/building/agentic-rag" >}}) — retrieval driven by an agent, not a fixed pipeline.
6. [The agent harness]({{< relref "/building/agent-harness" >}}) — the loop, context, tools, memory, guardrails.
7. [Loop engineering]({{< relref "/building/loop-engineering" >}}) — designing the loops themselves: closed loops, validators, orchestration.
8. [From prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) — the five engineering disciplines as one evolution.
9. [AI code structure]({{< relref "/building/ai-code-structure" >}}) — how to organize an AI app codebase.
10. [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) — SDKs, frameworks, MCP, deployment.

## Prerequisites

Work through [Stage 0 — Foundations]({{< relref "/foundations" >}}) and
[Stage 1 — Deep Dives]({{< relref "/deep-dives" >}}) first — Stage 2 builds directly on both.
