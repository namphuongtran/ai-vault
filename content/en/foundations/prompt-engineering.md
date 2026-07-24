---
title: "Prompt Engineering"
weight: 11
description: The most direct way to control a foundation model's output.
---

## What it is

**Prompt engineering** is designing the input to a foundation model to get the output you
want. It's the most direct lever over model behavior — no retraining required.

## Anatomy of a good prompt

| Component | Purpose |
| ----------- | --------- |
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

## Which technique when

| Situation | Reach for |
| ------ | ------ |
| The task is common and well-understood | **Zero-shot** — just ask; modern models usually get it |
| Output format or style keeps drifting | **Few-shot** — 2–5 examples teach the pattern faster than a paragraph of rules |
| Multi-step logic goes wrong | **Chain-of-thought** — ask it to reason step by step (or use a [reasoning model]({{< relref "/foundations/reasoning-models" >}})) |
| The task is too big for one prompt | **Prompt chaining** — split into sequential prompts and validate between steps |
| The same prompt shape runs on many inputs | **Prompt template** — one structure, input variables |
| Every call repeats a long prefix | **Prompt caching** — a cost lever; see [Cost & tokens]({{< relref "/foundations/cost-and-tokens" >}}) |

The pattern behind the table: examples beat instructions for *form*; reasoning beats both for
*logic*; and decomposition beats bigger prompts.

## Strengths & limitations

- **Strengths** — the cheapest, fastest lever; no infrastructure; you iterate instantly.
- **Limitations** — can't add knowledge the model lacks (use RAG); sensitive to wording; hits a
  ceiling on hard or consistency-critical tasks (then consider fine-tuning).

## Sources

- [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
