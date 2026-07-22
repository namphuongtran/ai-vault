---
title: "Prompt Engineering"
weight: 3
description: The most direct way to control a foundation model's output.
---

## What it is

**Prompt engineering** is designing the input to a foundation model to get the output you
want. It's the most direct lever over model behavior — no retraining required.

## Anatomy of a good prompt

| Component | Purpose |
|-----------|---------|
| Role | Who the model should act as |
| Task | What to do |
| Context | Background information needed |
| Constraints | Limits and conditions |
| Response format | Output structure |
| Response style | Tone and voice |
| Success criteria | What "good" looks like |
| Examples | Sample inputs/outputs when helpful |

**Weak:** "Summarize this document."

**Strong:** "You are a document analyst. Summarize the content below in at most five key
points. Each point is no more than two sentences. Use only information present in the
document and do not add facts."

## Techniques to distinguish

- **Zero-shot** — ask the task with no examples.
- **One-shot** — give exactly one example first.
- **Few-shot** — give several examples so the model infers the pattern.
- **Prompt chaining** — split a big task into smaller prompts run in sequence.
- **Prompt template** — a reusable prompt structure with input variables.
- **Chain-of-thought** — ask the model to reason step by step.
- **Prompt caching** — reuse a repeated prompt prefix to cut latency and cost (where supported).
