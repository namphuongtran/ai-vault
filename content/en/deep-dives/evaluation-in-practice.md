---
title: "Evaluation in Practice"
weight: 5
description: Eval sets, LLM-as-judge, offline vs online, and regression testing.
---

Builds on [Model Evaluation in Foundations]({{< relref "/foundations/model-evaluation" >}}).
Metrics only help if you evaluate systematically. This is how to actually run evaluation.

## Build an eval set

- Collect real inputs (or realistic ones) with known-good outputs or acceptance criteria.
- Cover the **common cases and the edge cases** — the ones that break in production.
- Start small (20–50 examples) and grow it as you find failures; every bug becomes a case.
- Version it; treat it like test data.

## LLM-as-judge

For open-ended outputs where exact-match doesn't work, use a strong model to **grade**
responses against a rubric.

- Give the judge explicit criteria and a scale; ask for a reason, then a score.
- Prefer **pairwise** comparisons (A vs B) — more reliable than absolute scores.
- Validate the judge against some human labels; watch for bias (length, position, self-preference).

## Offline vs online

- **Offline** — run the eval set in CI before shipping a change. Fast feedback, controlled.
- **Online** — measure real usage: user feedback, thumbs up/down, task success, escalations.
- Offline catches regressions; online catches what your eval set missed. You need both.

## RAG evaluation

Evaluate retrieval and generation separately (RAGAS-style):

- **Context precision / recall** — retrieval quality.
- **Faithfulness** — answer grounded in retrieved context.
- **Answer relevance** — answer addresses the question.

This isolates whether a bad answer came from retrieval or generation.

## Regression testing

- Run the eval set in CI on every prompt, model, or pipeline change.
- Fail the build on a drop past a threshold.
- Pin the model version; a provider update is itself a change to evaluate.

## Pitfalls

- Testing on examples you tuned against (leakage).
- One aggregate score hiding failures on a key slice — break results down by category.
- Trusting a judge you never validated.
