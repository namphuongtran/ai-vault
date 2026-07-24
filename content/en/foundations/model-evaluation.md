---
title: "Model Evaluation"
weight: 26
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

## Example — precision vs recall with numbers

A fraud filter flags 100 transactions as fraud; 90 are truly fraud, 10 are fine. It also
missed 30 real frauds it never flagged:

| | Flagged fraud | Not flagged |
| -- | -------------- | ------------- |
| Actually fraud | 90 (TP) | 30 (FN) |
| Actually fine | 10 (FP) | rest (TN) |

- **Precision** = 90 / (90 + 10) = **0.90** — of what it flagged, 90% were right.
- **Recall** = 90 / (90 + 30) = **0.75** — it caught 75% of all real fraud.

Push one up and the other usually drops — that's the trade-off F1 balances.

## RAG-specific metrics

- **Faithfulness** — does the answer stay true to the provided context? A fluent answer can
  still contain facts not present in the retrieved documents.
- **Context relevance** — are the retrieved passages actually relevant to the question? If
  retrieval is wrong, even a good model produces poor answers.

## Which metric when

| Task | Reach for |
| ------ | ------ |
| Summarization | **ROUGE** |
| Translation | **BLEU** |
| Classification where false positives hurt | **Precision** |
| Classification where false negatives hurt | **Recall** |
| Both hurt, or classes are imbalanced | **F1** |
| RAG answers | **Faithfulness + context relevance** (RAGAS) |
| Open-ended generation, no reference answer | **Human review or LLM-as-judge** — see [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) |

The rule behind the table: pick the metric by **the cost of the error**, not by habit — decide
first whether a false positive or a false negative hurts more.

## Sources

- Papineni et al., *BLEU: a Method for Automatic Evaluation of Machine Translation* (2002) — [ACL P02-1040](https://aclanthology.org/P02-1040/)
- Lin, *ROUGE: A Package for Automatic Evaluation of Summaries* (2004) — [ACL W04-1013](https://aclanthology.org/W04-1013/)
- Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) — [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
