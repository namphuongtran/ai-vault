---
aliases: ["/foundations/limitations/"]
title: "Limitations & Failure Modes"
linkTitle: "Limitations & Failure Modes"
weight: 8
description: What models get wrong and why — so you know when to add RAG, tools, guardrails, or a human.
---

Knowing *how* models fail tells you *what to add* around them. None of these are bugs — they
follow from [how LLMs work]({{< relref "how-llms-work.md" >}}).

## The main failure modes

| Failure mode | What it is | Mitigation |
| -------------- | ----------- | ------------ |
| Hallucination | Confident but false or unsupported output | [RAG]({{< relref "rag.md" >}}) + citations; ask for "I don't know" |
| Knowledge cutoff | No knowledge of recent or private facts | RAG, tools, web search |
| Bad at exact math / counting | Predicts plausible tokens, doesn't compute | Give it [tools / code]({{< relref "tool-function-calling.md" >}}) |
| Non-determinism | Same prompt → different answers | Lower temperature, constrain output, [evaluate]({{< relref "model-evaluation.md" >}}) |
| Prompt sensitivity | Small wording changes shift results | Test prompts against an eval set |
| Bias | Reflects biases in training data | [Responsible AI]({{< relref "responsible-ai.md" >}}) review, human oversight |
| Context limits | Forgets or drops info beyond the window | [Context engineering]({{< relref "context-engineering.md" >}}) |

## The pattern

```mermaid
flowchart LR
    H[Hallucination / cutoff] --> RAG[Ground with RAG + citations]
    M[Bad math / counting] --> Tools[Use tools and code]
    ND[Non-determinism] --> Eval[Constrain + evaluate]
    B[Bias / safety] --> Gov[Guardrails + human oversight]
```

## The takeaway

A model alone is unreliable for facts, math, and consistency. You make it reliable by
**surrounding it** — grounding it in data, giving it tools, constraining its output, and
measuring it. That's what the rest of this stage is about.

## Sources

- Ji et al., *Survey of Hallucination in Natural Language Generation* (2022) — [arXiv:2202.03629](https://arxiv.org/abs/2202.03629)
