---
title: "Deep Dives (Stage 1)"
linkTitle: "Deep Dives"
weight: 2
type: docs
no_list: true
menu:
  main:
    weight: 2
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
    A[Prompt patterns] --> B[Types of RAG] --> C[Advanced RAG]
    C --> D[Agent patterns] --> E[Adaptation] --> F[Evaluation in practice]
```

## In this section

1. [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) — reasoning techniques,
   structured output, decomposition, optimization.
2. [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) — the RAG family; which is an
   architecture vs a technique.
3. [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) — chunking, hybrid retrieval,
   re-ranking, query transforms.
4. [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) — the ReAct loop, tool
   design, memory, multi-agent, reflection.
5. [Adaptation]({{< relref "/deep-dives/adaptation" >}}) — choosing between prompting, RAG,
   and fine-tuning.
6. [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) — eval sets,
   LLM-as-judge, offline vs online, regression testing.
