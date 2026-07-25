---
title: "Deep Dives (Stage 1)"
linkTitle: "Deep Dives"
weight: 3
type: docs
no_list: true
menu:
  main:
    weight: 3
description: >
  One level deeper on the core Stage 0 topics — the parts that pay off in real systems.
---

**Stage 1** goes deeper on the topics introduced in
[Foundations]({{< relref "/foundations" >}}). Where Stage 0 answered *what* and *when*,
Stage 1 answers *how* — the strategies, patterns, and trade-offs that show up when you
build real systems.

## Roadmap

The dives follow the same spine as the Stage 0 modules — prompts, then data, then agents,
then operating:

```mermaid
flowchart LR
    A[Prompt patterns] --> B[Vector databases] --> C[Types of RAG] --> D[Advanced RAG]
    D --> E[Agent patterns] --> F[Agent memory] --> G[Adaptation] --> H[Evaluation in practice]
```

## In this section

1. [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) — reasoning techniques,
   structured output, decomposition, optimization.
2. [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) — ANN indexes (HNSW,
   IVF, PQ), metadata filtering, choosing a store.
3. [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) — the RAG family; which is an
   architecture vs a technique.
4. [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) — chunking, hybrid retrieval,
   re-ranking, query transforms.
5. [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) — the ReAct loop, tool
   design, multi-agent, reflection.
6. [Agent memory]({{< relref "/deep-dives/agent-memory" >}}) — the memory types, and when
   each one earns its place.
7. [Adaptation]({{< relref "/deep-dives/adaptation" >}}) — choosing between prompting, RAG,
   and fine-tuning.
8. [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) — eval sets,
   LLM-as-judge, offline vs online, regression testing.
