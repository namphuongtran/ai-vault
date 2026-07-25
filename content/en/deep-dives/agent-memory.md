---
title: "Agent Memory"
weight: 6
description: The types of memory an agent can have — and when each one is actually worth adding.
---

## Goal

Know the kinds of memory an [agent]({{< relref "/foundations/agents" >}}) can have, and —
more importantly — **when each one earns its place**. Memory is the most over-engineered part
of agent design: every type you add is state to store, retrieve, secure, and keep fresh.

## Start from one fact

The model itself remembers nothing between calls — its only "memory" is whatever the harness
puts in the [context window]({{< relref "/foundations/context-engineering" >}}) this turn.
Every memory type below is just a different strategy for *what to persist outside the model
and when to load it back in*.

```mermaid
flowchart LR
    subgraph Stores[Persisted outside the model]
      SM[Semantic - facts]
      EM[Episodic - past events]
      PM[Procedural - how-to]
      XM[External - documents]
    end
    Stores -->|retrieve when relevant| W[Working memory - the context window]
    W --> LLM[Model call]
```

## The types, and when you need them

| Type | What it holds | Add it when… |
| ------ | ------ | ------ |
| **Working** | What's in the context window right now | Always — this is the baseline, managed by the [harness]({{< relref "/building/agent-harness" >}}) |
| **Semantic** | Durable facts and preferences ("user is on the Pro plan", "replies in Vietnamese") | Users repeat themselves across sessions |
| **Episodic** | Past events and outcomes ("the last deploy failed on migrations") | The agent repeats mistakes it already made |
| **Procedural** | How to do tasks — prompts, skills, runbooks | The agent re-derives the same procedure every time (see [Skills]({{< relref "/building/agent-harness" >}})) |
| **External** | Document knowledge in a vector store, fetched via [RAG]({{< relref "/foundations/rag" >}}) | The knowledge doesn't fit in context and changes often |
| **Parametric** | What the model learned in training — frozen in its weights | You don't add this at runtime — it's why cutoffs exist; fix gaps with RAG or [fine-tuning]({{< relref "/deep-dives/adaptation" >}}) |
| **Prospective** | Things to do later ("follow up when CI finishes") | The agent must act on future events, not just the current turn |

## Symptom → memory

Work backwards from failure, not forwards from the taxonomy:

| Symptom | What's missing |
| ------ | ------ |
| Forgets instructions mid-task | Working memory management (trim/summarize), not more storage |
| Asks the user the same thing every session | Semantic |
| Repeats a mistake it made last week | Episodic |
| Solves a routine task differently (and worse) each time | Procedural |
| Doesn't know your documents | External (RAG) |
| Knowledge is outdated | Parametric limit — RAG or fine-tune, no runtime fix |

## Example — a support agent's memory stack

Turn 1 of a session: the harness loads the ticket thread (working), the customer's plan and
language (semantic), a note that this customer's last issue was mis-escalated (episodic), the
refund runbook (procedural), and retrieves the relevant policy passages (external). Five
types, one context window — each loaded *because a past failure demanded it*, not because the
diagram had a box for it.

## Strengths & limitations

- **Strengths** — continuity across sessions is what separates an assistant from a stateless
  chatbot; episodic + procedural memory is how agents get *better* instead of starting from
  zero each run.
- **Limitations** — stored memories go stale and confidently wrong (a moved customer, a
  changed policy); retrieval can surface the *wrong* memory, which poisons the turn; personal
  facts raise privacy and retention duties (see
  [Responsible AI]({{< relref "/foundations/responsible-ai" >}})); every store is
  infrastructure to run and sync.

> Start with working memory only. Add one type at a time, when a real symptom appears — never
> all seven because a diagram showed seven.

## Sources

- Sumers et al., *Cognitive Architectures for Language Agents (CoALA)* (2023) — [arXiv:2309.02427](https://arxiv.org/abs/2309.02427)
- Packer et al., *MemGPT: Towards LLMs as Operating Systems* (2023) — [arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
