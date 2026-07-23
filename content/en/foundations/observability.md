---
title: "Observability"
weight: 19
description: Seeing what your AI system actually did — traces, metrics, and production evals.
---

Builds on [Model evaluation]({{< relref "/foundations/model-evaluation" >}}). Evaluation asks
*is it good?*; **observability** asks *what actually happened in production, and why?* Because
output is non-deterministic, you can't debug an AI system you can't see into.

## What to capture

```mermaid
flowchart LR
    Req[Request] --> App[App]
    App --> M[Model]
    App --> R[Retrieval]
    App --> T[Tools]
    App -. traces .-> Obs[Observability - traces, metrics, evals]
    M -. tokens, latency .-> Obs
```

- **Traces** — the full step-by-step of a request: the prompt, retrieved context, each tool
  call and result, and the final output. This is what you replay when something goes wrong.
- **Metrics** — latency, token usage, **cost**, and error / refusal rates over time.
- **Quality signals** — user feedback (thumbs up/down), task success, and **online evals**
  (scoring a sample of real traffic, often with [LLM-as-judge]({{< relref "/deep-dives/evaluation-in-practice" >}})).

## Why it matters

- **Debugging** — a bad answer could come from retrieval, the prompt, a tool, or the model;
  only a trace tells you which.
- **Cost control** — tokens are money; you can't manage what you don't measure.
- **Drift** — quality can change when data, prompts, or the model version change; online evals
  catch it.

## Offline vs. online

Offline evals (in [CI]({{< relref "/deep-dives/evaluation-in-practice" >}})) catch regressions
before shipping; observability catches what real users hit *after*. You need both.
