---
title: "Parametric Memory"
weight: 6
description: Knowledge baked into the model's weights — instant, but frozen at the training cutoff.
---

*Knowledge baked into the weights.*

## What it is

Knowledge learned during training and stored directly in the model's weights: language,
reasoning patterns, world knowledge, facts. No retrieval — it's just *there*.

```mermaid
flowchart LR
    Q[Question] --> LLM[LLM - parametric memory in weights: language, world knowledge, facts]
    LLM --> A[Answer - instant, no retrieval]
```

## When you need it

You don't *add* it at runtime — it's always present, the fastest and cheapest memory. The
design question is what to *rely* on it for versus fetch externally.

## The trade-off

Instant and free at inference, but **frozen at the training cutoff** and hard to update or
audit. Fill gaps with [external memory]({{< relref "external-memory.md" >}}) (fresh, citable)
or [fine-tuning]({{< relref "/deep-dives/adaptation" >}}) (new behavior) — never at runtime.

## Example

The model knows what a REST API is without being told, but won't know a library released last
month. The first is parametric; the second needs external memory.

## Related

- [How models are trained]({{< relref "training-lifecycle.md" >}}) — how knowledge gets into the weights.
- [Adaptation]({{< relref "/deep-dives/adaptation" >}}) — when to fine-tune versus retrieve.
