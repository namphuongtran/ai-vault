---
title: "Guardrails"
weight: 16
description: Safety and control mechanisms around a model's inputs and outputs.
---

## What it is

**Guardrails** are the controls placed around a model to keep its behavior safe, on-topic,
and compliant. They sit *before* the model (on inputs) and *after* it (on outputs), and they
work regardless of how the model itself was trained.

## Where they apply

- **Input guardrails** — block prompt injection, off-topic requests, or disallowed content;
  redact PII before it reaches the model.
- **Output guardrails** — filter toxic or unsafe responses, enforce format, check that answers
  stay grounded in provided context (see [Faithfulness]({{< relref "model-evaluation" >}})).

## Common types

- **Content moderation** — detect toxic, hateful, or unsafe text.
- **Topic restriction** — keep the model within an allowed domain.
- **PII detection / redaction** — protect personal and sensitive data.
- **Format / schema enforcement** — ensure valid, structured output.
- **Grounding checks** — reject answers not supported by the retrieved context.

## Why it matters

Guardrails reduce risk (harmful output, data leakage, off-scope use) without retraining the
model. They pair naturally with **agents**, where more autonomy raises the need for control.
