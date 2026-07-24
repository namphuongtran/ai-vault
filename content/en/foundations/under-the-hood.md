---
title: "Under the Hood"
weight: 7
description: A light look at transformers and attention — just enough to explain why LLMs behave as they do.
---

Builds on [How LLMs work]({{< relref "/foundations/how-llms-work" >}}). You don't need this to
build, but a light mental model of *what's inside* explains a lot of the behavior you'll see.

## Attention, in one idea

LLMs are **transformers**. The key trick is **attention**: to predict the next token, the
model looks at *all* the tokens so far and weighs how much each one matters to the current
step. "It" gets linked to the noun it refers to; a question gets linked to the relevant fact
earlier in the prompt.

```mermaid
flowchart LR
    In[All tokens so far] --> Att[Attention - weigh how tokens relate]
    Att --> H[Context-aware representation]
    H --> Next[Predict next token]
```

## Why this explains the behavior you see

- **Context is everything** — the model has no memory beyond what's in the window; attention
  works over exactly that text. More relevant context → better answers (and more cost).
- **Order and phrasing matter** — attention is sensitive to how things are worded and placed;
  that's why [prompting]({{< relref "/foundations/prompt-engineering" >}}) and
  [context engineering]({{< relref "/foundations/context-engineering" >}}) work.
- **Cost grows with length** — attention compares tokens against each other, so long inputs are
  disproportionately expensive.
- **No true understanding** — it's pattern prediction, not comprehension, which is why models
  can be confidently wrong (see [Limitations]({{< relref "/foundations/limitations" >}})).

That's the whole point of this page — awareness, not implementation. The math is optional.
