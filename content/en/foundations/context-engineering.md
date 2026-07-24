---
title: "Context Engineering"
weight: 11
description: Managing what goes into the context window — the discipline beneath prompting, RAG, and agents.
---

Builds on [Prompt engineering]({{< relref "/foundations/prompt-engineering" >}}). Prompting is
*wording* the request; **context engineering** is deciding *everything* the model sees in its
finite [context window](/foundations/how-llms-work/) — and what to leave out.

## What's in the context

- **System prompt** — role, rules, output format.
- **Instructions / examples** — the task and any few-shot samples.
- **Retrieved data** — documents pulled in via [RAG]({{< relref "/foundations/rag" >}}).
- **Tool results** — output from [tools the model called]({{< relref "/foundations/tool-function-calling" >}}).
- **History / memory** — prior turns, or facts carried across sessions.

```mermaid
flowchart LR
    SP[System prompt] --> CW[Context window]
    EX[Instructions and examples] --> CW
    RD[Retrieved data via RAG] --> CW
    TR[Tool results] --> CW
    H[History and memory] --> CW
    CW --> M[Model]
```

## The core problem: the window is finite

Everything above competes for the same token budget. More is not better — irrelevant context
distracts the model and costs money. The goal is the **right** information, not the most.

## Techniques

- **Retrieval** — fetch only the passages relevant to *this* request (RAG).
- **Summarization / compaction** — condense old turns when a conversation grows long.
- **Pruning** — drop stale tool results and history the model no longer needs.
- **Ordering & caching** — put stable content first so it can be cached and reused cheaply.

## Why it matters to you

Most "the model got it wrong" problems are really context problems: it lacked the right
information, or drowned in the wrong information. Fix the context before blaming the model.
