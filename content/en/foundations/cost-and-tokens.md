---
title: "Cost & Tokens"
weight: 15
description: What you actually pay for, what drives it up, and the levers to bring it down.
---

You pay per **token** — input and output, priced separately. Cost is easy to reason about once
you see what feeds it.

## What drives cost

```mermaid
flowchart LR
    In[Input tokens: prompt + context + history] --> Cost[Total cost]
    Out[Output tokens] --> Cost
    Tier[Model tier price] --> Cost
    Calls[Number of calls] --> Cost
```

- **Input tokens** — your system prompt, retrieved [context]({{< relref "/foundations/context-engineering" >}}),
  and the whole conversation history you resend each turn.
- **Output tokens** — usually priced higher than input.
- **Model tier** — a flagship model can cost 10×+ a small one (see
  [Choosing a model]({{< relref "/foundations/choosing-a-model" >}})).
- **Number of calls** — [agents]({{< relref "/foundations/agentic-ai" >}}) multiply calls; a
  loop can be many requests per task.

## The levers

- **Right-size the model** — use a smaller tier where quality holds.
- **Trim context** — send only what's relevant; don't dump whole documents.
- **Cap `max_tokens`** — bound the output.
- **Prompt caching** — reuse a stable prompt prefix across calls to cut input cost.
- **Batch** offline work; **stream** for UX (doesn't cut cost, improves perceived latency).

## Estimating and tracking

- Count tokens with a tokenizer before you ship (don't guess).
- Watch real token usage in [Observability]({{< relref "/foundations/observability" >}}) — the
  API returns `usage` on every response.

> Rule of thumb: the cheapest token is the one you don't send. Most cost problems are context
> problems.
