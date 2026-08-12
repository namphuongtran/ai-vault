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

## Learning from traces

The three mechanisms work *inside* one task. Improving the agent across *many* tasks needs a
different input, because it needs a different source of truth. In ordinary software the truth
about behaviour is the code. In an agent it isn't — the same code produces a different run
every time, so what actually happened only exists in the
[trace]({{< relref "observability.md" >}}): the context it was given, the tools it called, the
results that came back, and the verdict on the output.

A second agent, running after the fact over a batch of traces, reads them for a failure that
*repeats*:

- a tool called with the wrong arguments, run after run;
- a tool never called at all, because nothing in the context told the agent it existed;
- a preference the user stated once and the agent keeps ignoring.

It then proposes the fix, and the fix lands in one of two places:

- **Procedural** — the prompt, tool descriptions, and skills: *how* the work gets done.
- **Semantic** — stored facts and preferences: an assistant that learns to write formally to
  your manager and casually to your team.

The semantic half only works if corrections have a **write path**. When a user blocks an
over-casual draft to their manager, that correction has to be consolidated into a durable
preference, not just applied to the one message — otherwise the same mistake comes back next
week. See [semantic memory]({{< relref "/deep-dives/agent-memory/semantic-memory" >}}) for
where it is stored.

## What to change first

When the analysis finds a repeating failure, resist rewriting the architecture. Most agent
failures are not *the model wasn't smart enough*; they are *the model didn't have the right
information*. Work down this list, and stop as soon as the failure stops:

1. **Memory and skills** — it lacked a fact or a procedure it should have had.
2. **Prompts and tool descriptions** — it had what it needed and used it wrong.
3. **Tools** — it needed a capability nothing gave it.
4. **Architecture** — only when the agent keeps failing something that is *not allowed* to
   fail, such as a compliance step. Then take the decision away from the model and make it a
   deterministic step in code.

Each rung costs more to change and more to live with. The top two cover most of it.

None of this merges safely without evals. A new prompt or a newly stored preference can fix
one case and quietly break five others, so every proposed change runs against an
[eval set]({{< relref "/deep-dives/evaluation-in-practice" >}}) first. Until that set is
trustworthy, a human approves the merge — the level 4 placement in
[the four levels of loops]({{< relref "/building/loop-engineering/levels" >}}).

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
- Runkle, *The Art of Loop Engineering* (2026) — [langchain.com](https://www.langchain.com/blog/the-art-of-loop-engineering)
