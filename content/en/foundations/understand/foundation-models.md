---
aliases: ["/foundations/foundation-models/"]
title: "Foundation Models"
weight: 3
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

## Example — one model, many tasks

The *same* foundation model can summarize an email, write SQL, translate French, and answer a
support question — with no task-specific training. You just change the prompt.

## Strengths & limitations

- **Strengths** — one general-purpose model for many tasks; adapt it cheaply along
  prompting → RAG → fine-tuning.
- **Limitations** — knowledge frozen at a cutoff; can hallucinate; capability, cost, and
  latency all scale with size; behavior is hard to fully predict.

## Sources

- Bommasani et al., *On the Opportunities and Risks of Foundation Models* (2021) — [arXiv:2108.07258](https://arxiv.org/abs/2108.07258)
- [Anthropic — Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
