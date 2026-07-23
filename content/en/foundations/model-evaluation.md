---
title: "Model Evaluation"
weight: 18
description: How to measure model quality — pick the metric that matches the task.
---

## What it is

A model can do well on one task and poorly on another, so **model evaluation** matters.
Choose a metric based on the real goal of the problem.

## Text-generation metrics

- **ROUGE** — evaluates **text summarization** by measuring overlap between generated and
  reference text. Think summaries → ROUGE.
- **BLEU** — used for **machine translation**; compares word/phrase sequences between the
  model's translation and a reference. Think translation → BLEU.

## Classification metrics

- **Precision** — of the items predicted positive, how many are actually correct. Important
  when **false positives** are costly (e.g., fraud detection flagging valid transactions).
- **Recall** — of the actual positives, how many the model found. Important when **false
  negatives** are costly (e.g., disease screening missing a real case).
- **F1 score** — the balance of precision and recall; useful when both error types matter or
  when classes are imbalanced.

## RAG-specific metrics

- **Faithfulness** — does the answer stay true to the provided context? A fluent answer can
  still contain facts not present in the retrieved documents.
- **Context relevance** — are the retrieved passages actually relevant to the question? If
  retrieval is wrong, even a good model produces poor answers.

## Human evaluation

**Human evaluation** fits when quality can't be fully captured by automatic metrics.
