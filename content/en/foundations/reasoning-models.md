---
title: "Reasoning Models"
weight: 11
description: Models that think step-by-step before answering — when the extra time and tokens pay off.
---

A **reasoning model** is trained to work through a problem step by step *before* giving its
final answer — trading time and tokens for accuracy on hard, multi-step tasks.

```mermaid
flowchart LR
    Q[Question] --> R[Reasoning model]
    R --> Th[Internal step-by-step thinking]
    Th --> A[Final answer]
```

## How it shows up

Providers expose this differently, but the shape is the same: a **thinking / effort** dial you
turn up for harder problems (e.g. "extended" or "adaptive" thinking, an *effort* level, or a
dedicated reasoning model). Higher effort → more internal reasoning → slower and pricier.

## When to use one

- ✅ Complex reasoning, math, planning, multi-step debugging.
- ✅ [Agentic]({{< relref "/foundations/agentic-ai" >}}) tasks with many steps.
- ❌ Simple lookups, classification, or high-volume/latency-sensitive calls — a fast model is
  cheaper and good enough.

## The trade-off

| | Fast model | Reasoning model |
| -- | ----------- | ----------------- |
| Speed | Fast | Slower |
| Cost | Lower | Higher (more tokens) |
| Best at | Simple, well-scoped tasks | Hard, multi-step problems |

Choosing between them is a [model-choice]({{< relref "/foundations/choosing-a-model" >}})
decision; the effort dial is one of your [inference parameters]({{< relref "/foundations/inference-parameters" >}}).
