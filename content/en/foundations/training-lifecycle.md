---
title: "How Models Are Trained"
linkTitle: "How Models Are Trained"
weight: 5
description: An awareness-level view of pre-training, fine-tuning, and alignment — and why it matters to a builder.
---

You won't train a foundation model, but knowing *how* one is made explains a lot of its
behavior. This is awareness-level — no training techniques required.

## The two big phases

- **Pre-training** — the model learns language and world knowledge by predicting the next
  token across a huge corpus. The result is a **base model**: knowledgeable but not good at
  following instructions.
- **Post-training** — the base model is shaped into something useful:
  - **Instruction / fine-tuning** — taught to follow instructions and answer helpfully.
  - **Alignment (e.g. RLHF)** — tuned with human feedback to be helpful, honest, and safe.

## Why this matters to you as a builder

- **Knowledge cutoff** — knowledge is frozen at pre-training time. For fresh or private facts
  you need [RAG]({{< relref "/foundations/rag" >}}), not a newer base model.
- **Why it follows instructions (and refuses)** — that behavior comes from post-training, not
  magic. It's why [prompting]({{< relref "/foundations/prompt-engineering" >}}) works and why
  models sometimes decline requests.
- **What fine-tuning does** — it adjusts *behavior and style*, and reliably teaches narrow
  skills; it does **not** reliably inject fresh knowledge. See
  [Adaptation]({{< relref "/deep-dives/adaptation" >}}).

## What you don't need

Datasets, GPUs, loss functions, gradient descent. Providers handle all of it; you consume the
finished model.
