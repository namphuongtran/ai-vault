---
aliases: ["/foundations/reasoning-models/"]
title: "Reasoning Models"
weight: 14
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
- ✅ [Agentic]({{< relref "agentic-ai.md" >}}) tasks with many steps.
- ❌ Simple lookups, classification, or high-volume/latency-sensitive calls — a fast model is
  cheaper and good enough.

## Example — where the extra tokens pay off

*"Invoice totals are wrong, but only for orders with mixed-currency line items — find the
bug."*

A fast model pattern-matches and blames the rounding helper — plausible, wrong. A reasoning
model traces the flow: line items convert to base currency per line, the discount is applied
at order level, but one code path applies it *before* conversion — a double conversion only
mixed-currency orders can hit. Chained dependencies like this are exactly where the thinking
earns its cost; for a lookup or a classification it's money spent on nothing.

## The trade-off

| | Fast model | Reasoning model |
| -- | ----------- | ----------------- |
| Speed | Fast | Slower |
| Cost | Lower | Higher (more tokens) |
| Best at | Simple, well-scoped tasks | Hard, multi-step problems |

Choosing between them is a [model-choice]({{< relref "choosing-a-model.md" >}})
decision; the effort dial is one of your [inference parameters]({{< relref "inference-parameters.md" >}}).

## Sources

- [Anthropic — Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- [Anthropic — Effort](https://platform.claude.com/docs/en/build-with-claude/effort)
