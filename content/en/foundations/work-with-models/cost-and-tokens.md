---
aliases: ["/foundations/cost-and-tokens/"]
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

- **Input tokens** — your system prompt, retrieved [context]({{< relref "context-engineering.md" >}}),
  and the whole conversation history you resend each turn.
- **Output tokens** — usually priced higher than input.
- **Model tier** — a flagship model can cost 10×+ a small one (see
  [Choosing a model]({{< relref "choosing-a-model.md" >}})).
- **Number of calls** — [agents]({{< relref "agentic-ai.md" >}}) multiply calls; a
  loop can be many requests per task.

## Example — a rough cost calc

```text
Support bot, per reply:
  input  = 2,000 tokens (system + context + question)
  output =   300 tokens
Illustrative price: $3 / 1M input, $15 / 1M output
  input  = 2000/1e6 × $3  = $0.0060
  output =  300/1e6 × $15 = $0.0045
  → ~$0.011 per reply  ≈ $11 per 1,000 replies
```

Prices are illustrative — check your provider's. The point: input tokens (context + history)
usually dominate.

## The levers

- **Right-size the model** — use a smaller tier where quality holds.
- **Trim context** — send only what's relevant; don't dump whole documents.
- **Cap `max_tokens`** — bound the output.
- **Prompt caching** — reuse a stable prompt prefix across calls to cut input cost.
- **Batch** offline work; **stream** for UX (doesn't cut cost, improves perceived latency).

## How prompt caching works (KV cache)

To generate text, the model computes attention **key/value (KV) states** for every token in
the prompt — the expensive part. Normally these are recomputed on every call. **Prompt
caching** stores the KV states for a stable prefix (a long system prompt, tool definitions, a
big document) so a later call that starts with the same prefix **reuses** them instead of
recomputing — cutting input cost and time-to-first-token.

Example: a support bot whose 8,000-token policy manual sits at the top of every prompt. Cache
that prefix once; each subsequent question only pays to process the new question, not the
manual again. It works only when the prefix is **identical and at the start** — put the stable
part first, the variable part (the user's question) last.

## Estimating and tracking

- Count tokens with a tokenizer before you ship (don't guess).
- Watch real token usage in [Observability]({{< relref "observability.md" >}}) — the
  API returns `usage` on every response.

> Rule of thumb: the cheapest token is the one you don't send. Most cost problems are context
> problems.

## Sources

- [Anthropic — Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Anthropic — Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)
- [Anthropic — Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
