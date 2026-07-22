---
title: "Foundation Models"
weight: 1
description: Large, general-purpose models pre-trained on broad data and adapted to many tasks.
---

## What it is

A **foundation model** is a large model pre-trained on a broad range of data, then adapted
to many downstream tasks. Instead of training a separate model per task, you start from one
general-purpose model and specialize it.

## Key points

- **Pre-training** learns general patterns from massive data; **fine-tuning** and **prompting**
  specialize it for a task.
- **Parameters** — the learned weights; more parameters generally mean more capacity.
- **Context window** — how much text the model can consider at once (input + output).
- **Modalities** — text, image, audio, or a mix (multimodal).
- Adaptation options, from cheapest to most involved: **prompting → RAG → fine-tuning**.

> A large language model (LLM) is a foundation model specialized for text.
