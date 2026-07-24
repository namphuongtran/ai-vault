---
title: "Structured Outputs"
weight: 14
description: Making a model return machine-readable JSON that matches a schema — so your code can rely on it.
---

Builds on [The AI API]({{< relref "/foundations/the-ai-api" >}}). To *build* with a model you
usually need output your code can parse — not prose. **Structured outputs** constrain the
model's answer to a **schema** (usually JSON).

## The idea

You give a schema; the model returns data that matches it; you validate and use it directly.

```mermaid
flowchart LR
    P[Prompt + schema] --> M[Model]
    M --> J[JSON matching the schema]
    J --> V{Valid?}
    V -->|yes| Use[Use directly in code]
    V -->|no| M
```

## Example

Schema (what you ask for):

```json
{ "type": "object",
  "properties": {
    "sentiment": { "type": "string", "enum": ["positive", "neutral", "negative"] },
    "score": { "type": "number" }
  },
  "required": ["sentiment", "score"] }
```

Output (what you can rely on):

```json
{ "sentiment": "positive", "score": 0.82 }
```

No string-parsing, no "sometimes it adds a sentence before the JSON."

## How it's done

- **JSON / schema mode** — the API constrains decoding to valid JSON for your schema.
- **Tool arguments** — a [tool call]({{< relref "/foundations/tool-function-calling" >}})'s
  inputs are structured outputs too; same mechanism.
- **Validate + retry** — always validate; on a mismatch, re-ask.

## Why it matters

Structured outputs are what make an LLM a **reliable component** in a pipeline — classification,
extraction, routing, or any step whose result feeds other code.
