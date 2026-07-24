---
title: "Adaptation: Fine-tuning vs RAG vs Prompting"
linkTitle: "Adaptation"
weight: 5
description: How to choose between prompting, RAG, and fine-tuning — and how to combine them.
---

Three ways to adapt a [foundation model]({{< relref "/foundations/foundation-models" >}}) to
your task, from cheapest to most involved.

## The three levers

| Lever | Changes | Best for |
| ------- | --------- | ---------- |
| Prompting | The input only | Behavior, format, simple tasks |
| RAG | The input + external knowledge | Fresh, private, or citable facts |
| Fine-tuning | The model's weights | Consistent style/format, narrow skills |

## When to use which

- **Prompting** — start here. Fast, no infrastructure. Enough for most format and behavior needs.
- **RAG** — when the model needs *knowledge* it doesn't have: changing data, private
  documents, or answers that must cite sources. See
  [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}).
- **Fine-tuning** — when you need a *consistent behavior* prompting can't reliably produce
  (a fixed style, tone, or output schema), or to teach a narrow skill. It does **not** reliably
  add fresh factual knowledge — use RAG for that.

## Fine-tuning, briefly

- **Full fine-tuning** updates all weights — expensive, rarely needed.
- **PEFT / LoRA** trains small adapter layers instead — far cheaper, and adapters are easy to
  store and swap. The usual default when you do fine-tune.
- Needs a curated, labeled dataset; quality and coverage matter more than size.

## Cost and data trade-offs

- Prompting: near-zero setup; cost is per-request tokens.
- RAG: needs an ingestion + vector store pipeline; update data without retraining.
- Fine-tuning: upfront training cost and a dataset; must retrain to change behavior.

## Combining them

These aren't exclusive. A common production stack is **fine-tune for form + RAG for
knowledge**: fine-tune so the model reliably answers in your voice and schema, and use RAG to
feed it current, grounded facts at query time.
