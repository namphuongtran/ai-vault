---
title: "Agentic AI"
weight: 21
description: The paradigm where a model drives its own multi-step actions — and the harness that makes it work.
---

**Agentic** describes systems where the model doesn't just answer — it drives its own
multi-step actions toward a goal, deciding what to do next and using tools along the way.

## Workflows vs. agents

It's a spectrum of how much control you hand to the model:

```mermaid
flowchart LR
    W[Fixed workflow - you control each step] --- Mix[Model chooses among set steps] --- A[Autonomous agent - model drives the loop]
```

- **Workflow** — you code the steps; the model fills in blanks (extract, classify, summarize).
  Predictable and cheap.
- **Agent** — the model decides the steps at runtime via a
  [reason → act → observe loop]({{< relref "/foundations/agents" >}}). Flexible but harder to
  predict.

Prefer the leftmost option that solves the problem. Agentic is powerful, not free.

## The harness

An agent is a model **plus a harness** — the scaffolding around it that makes the loop work:

```mermaid
flowchart TB
    subgraph Harness[The harness]
      Loop[Reason - act - observe loop]
      Ctx[Context management]
      Tools[Tool execution]
      Mem[Memory]
      Guard[Guardrails and permissions]
    end
    Harness --> LLM[LLM]
```

The model is the engine; the harness is the chassis — it runs the loop, manages the
[context window]({{< relref "/foundations/context-engineering" >}}), executes
[tool calls]({{< relref "/foundations/tool-function-calling" >}}), stores memory, and enforces
[guardrails]({{< relref "/foundations/guardrails" >}}).

## When to go agentic

- ✅ The task is multi-step and hard to fully script in advance.
- ✅ It needs to react to intermediate results (search, then decide, then act).
- ❌ A fixed workflow already solves it — don't add autonomy you don't need.

## The trade-off

More autonomy = more capability, but also more cost, more latency, and less predictability.
That's why [evaluation]({{< relref "/foundations/model-evaluation" >}}) and
[guardrails]({{< relref "/foundations/guardrails" >}}) matter more the more agentic you go.
