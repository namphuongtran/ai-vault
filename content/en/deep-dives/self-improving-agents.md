---
title: "Self-Improving Agents"
weight: 8
description: How an agent gets better over time without changing the model's weights.
---

## Goal

Understand how an agent can **improve run over run without any retraining** — no weight
changes, no fine-tuning. The model stays frozen; what changes is what surrounds it. This
matters because retraining is slow and expensive, but a well-designed agent can still learn
from its own experience at runtime.

## Two ways to "learn"

| | Weight-changing | Weight-frozen (this page) |
| ------ | ------ | ------ |
| Mechanism | [Fine-tuning / RL]({{< relref "/deep-dives/adaptation" >}}) — update the model | Memory, reflection, and skills around a fixed model |
| Speed | Slow, offline, needs data + compute | Instant, at runtime |
| What improves | The model's raw capability | How well the agent *applies* a fixed capability |
| Ceiling | Can raise the model's skill | Bounded by the base model — better use, not new ability |

Self-improvement here is the second column: the base model's ability is a ceiling, but most
agents perform *well below* it because they forget, repeat mistakes, and re-derive procedures.
Closing that gap is where the gains are.

## The three mechanisms

```mermaid
flowchart LR
    T[Attempt a task] --> O[Observe result]
    O --> R[Reflect - what went wrong or right]
    R --> S[Store the lesson - memory or skill]
    S --> T2[Next attempt - starts smarter]
    W[(Model weights - unchanged)] -.-> T
    W -.-> T2
```

- **Reflection** — the agent evaluates its own output against the goal and retries. Within a
  task this fixes errors; across tasks, stored reflections prevent repeats. **Reflexion**
  showed this: an agent that writes a self-reflection after each failure reached 91% on a
  coding benchmark versus 80% without — same model, better use of it.
- **Episodic memory** — remembering past outcomes so a mistake made last week isn't made
  again. See [episodic memory]({{< relref "/deep-dives/agent-memory/episodic-memory" >}}).
- **Procedural memory / skill-building** — packaging a solved task into a reusable skill.
  **Voyager** builds a growing library of executable skills and composes them for new tasks,
  so it genuinely gets more capable over a session — without touching weights. See
  [procedural memory]({{< relref "/deep-dives/agent-memory/procedural-memory" >}}).

## Example — an agent that learns to deploy

A deploy agent fails because it forgot to run migrations. It **reflects** ("migrations must
run before restart"), **stores** that as an episodic lesson, and later **packages** the full
deploy sequence as a procedural skill. Next week, faced with a new service, it recalls the
lesson and reuses the skill — succeeding first try. The model never changed; the *system
around it* learned.

## Where it fits

Self-improvement is the payoff of the memory types working together, applied in a
[loop]({{< relref "/building/loop-engineering" >}}). In a
[multi-agent]({{< relref "/deep-dives/multi-agent" >}}) system a shared knowledge graph makes
the learning *collective* — one agent's lesson helps the whole team.

## Strengths & limitations

- **Strengths** — improvement without the cost and latency of retraining; the agent adapts to
  *your* environment and mistakes; gains compound as memory and skills accumulate.
- **Limitations** — bounded by the base model — it can't learn a skill the model fundamentally
  lacks (that needs [fine-tuning]({{< relref "/deep-dives/adaptation" >}})); stored lessons go
  stale or wrong and can entrench a *bad* habit as easily as a good one; more memory/skills
  means more retrieval noise. Verify what gets stored, and prune it — a self-improving loop
  with no quality gate self-degrades.

## Sources

- Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning* (2023) — [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- Wang et al., *Voyager: An Open-Ended Embodied Agent with Large Language Models* (2023) — [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)
- Huang et al., *Large Language Models Can Self-Improve* (2022) — [arXiv:2210.11610](https://arxiv.org/abs/2210.11610)
