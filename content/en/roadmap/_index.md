---
title: "Roadmap"
linkTitle: "Roadmap"
weight: 1
type: docs
no_list: true
menu:
  main:
    weight: 1
description: >
  The whole journey — what's written, what's planned, and the order to read it in.
---

This vault is a **living map**, not a finished book. The goal is to go beyond *using*
ChatGPT or Claude: **understand** how these systems work, **master** the techniques that
matter, **build** real systems, and eventually **ship** hands-on projects. Written pages are
marked ✓; planned ones ○ — they get filled in as I learn.

## The journey

```mermaid
flowchart LR
    S0[Stage 0 - Foundations ✓] --> S1[Stage 1 - Deep Dives ✓] --> S2[Stage 2 - Building ✓]
    S2 --> S3[Stage 3 - Hands-on 2 of 7] --> S4[Stage 4 - Create ○]
```

Read **across** to progress stage by stage, or pick a row in the
[threads table](#follow-one-topic-in-depth) below to go deep on one topic.

## Stage 0 — Foundations ✓

28 concepts in [five ordered modules]({{< relref "/foundations" >}}), from *what models are*
to *operating them in production*:

1. **Understand** — the landscape, generative AI, foundation models, how LLMs work, training,
   multimodality, limitations.
2. **Work with a model** — the API, parameters, prompting, context, structured outputs,
   reasoning models, cost, choosing a model.
3. **Ground it in your data** — embeddings, RAG.
4. **Make it act** — tools, agents, agentic AI, MCP, AI coding assistants.
5. **Operate & govern** — guardrails, security, evaluation, observability, responsible AI.

## Stage 1 — Deep Dives ✓

[Twelve dives]({{< relref "/deep-dives" >}}) along the same spine:
[prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) ·
[vector databases]({{< relref "/deep-dives/vector-databases" >}}) ·
[types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) ·
[advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) ·
[agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) ·
[agent memory]({{< relref "/deep-dives/agent-memory" >}}) ·
[multi-agent systems]({{< relref "/deep-dives/multi-agent" >}}) ·
[self-improving agents]({{< relref "/deep-dives/self-improving-agents" >}}) ·
[computer use]({{< relref "/deep-dives/computer-use" >}}) ·
[adaptation]({{< relref "/deep-dives/adaptation" >}}) ·
[evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) ·
[RAG evaluation]({{< relref "/deep-dives/rag-evaluation" >}}).

## Stage 2 — Building with AI ✓

[Ten entries]({{< relref "/building" >}}) that assemble the pieces:
[AI system design]({{< relref "/building/ai-system-design" >}}) ·
[scaling to production]({{< relref "/building/scaling-to-production" >}}) ·
[serving models]({{< relref "/building/serving-models" >}}) ·
[building RAG]({{< relref "/building/building-rag" >}}) ·
[agentic RAG]({{< relref "/building/agentic-rag" >}}) ·
[the agent harness]({{< relref "/building/agent-harness" >}}) ·
[loop engineering]({{< relref "/building/loop-engineering" >}}) ·
[from prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) ·
[AI code structure]({{< relref "/building/ai-code-structure" >}}) ·
[tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}).

## Stage 3 — Hands-on (in progress)

[Real projects]({{< relref "/hands-on" >}}), built incrementally:

1. ✓ **[Lab: a RAG chatbot over my own documents]({{< relref "/hands-on/lab-rag-chatbot" >}})**
   — in seven steps: infrastructure → ingestion → keyword search → hybrid search → full RAG →
   monitoring + caching → agentic upgrade.
2. ✓ **[Lab: build your own agent harness]({{< relref "/hands-on/lab-agent-harness" >}})** — in eight steps: one API call → one tool →
   the loop → context management → subagents → a model per role → permissions and hooks → MCP and
   the Agent SDK, each checked against Claude Code.
3. ○ **Lab: an eval harness + observability** for labs 1–2, plus verifying what an agent produces.
4. ○ **Lab: agents on a real repo, Level 1 → 3** — agent-ready repo, spec and verify, parallel
   solutions in git worktrees, orchestration, before/after measurement.
5. ○ **Practical fine-tuning (LoRA)** — adapt a small model for tone and schema.
6. ○ **A multimodal app** — vision input, document extraction.
7. ○ **Ship to production** — deployment, cost control, monitoring.

## Stage 4 — Create ○ (planned, further out)

- ○ AI product design — from capability to product.
- ○ The economics of experimentation — from *"do we have the people and time to build this?"* to
  *"can we run an experiment to find out whether it's worth building?"* Cheap experiments still
  need a hypothesis, a success metric, a kill criterion and a budget **before** you delegate
  them, because more output is not more value.
- ○ Case studies of real AI products.
- ○ Certification notes & review sheets.

## Follow one topic in depth

Each row is one thread through all stages — the vertical way to read the vault:

| Thread | Stage 0 | Stage 1 | Stage 2 | Stage 3 ○ |
| ------ | ------ | ------ | ------ | ------ |
| **Prompts** | [Prompt engineering]({{< relref "prompt-engineering.md" >}}) · [Context engineering]({{< relref "context-engineering.md" >}}) | [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) | — | — |
| **Data & RAG** | [Embeddings]({{< relref "embeddings.md" >}}) · [RAG]({{< relref "rag.md" >}}) | [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) · [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) · [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) · [RAG evaluation]({{< relref "/deep-dives/rag-evaluation" >}}) | [Building RAG]({{< relref "/building/building-rag" >}}) · [Agentic RAG]({{< relref "/building/agentic-rag" >}}) | [RAG chatbot lab ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) |
| **Agents** | [Tool calling]({{< relref "tool-function-calling.md" >}}) · [Agents]({{< relref "agents.md" >}}) · [Agentic AI]({{< relref "agentic-ai.md" >}}) · [MCP]({{< relref "mcp.md" >}}) | [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) · [Agent memory]({{< relref "/deep-dives/agent-memory" >}}) · [Multi-agent]({{< relref "/deep-dives/multi-agent" >}}) · [Self-improving]({{< relref "/deep-dives/self-improving-agents" >}}) · [Computer use]({{< relref "/deep-dives/computer-use" >}}) | [Agent harness]({{< relref "/building/agent-harness" >}}) · [Loop engineering]({{< relref "/building/loop-engineering" >}}) · [AI code structure]({{< relref "/building/ai-code-structure" >}}) | [Agent harness lab ✓]({{< relref "/hands-on/lab-agent-harness" >}}) · ○ Real-repo lab |
| **Operate** | [Guardrails]({{< relref "guardrails.md" >}}) · [AI security]({{< relref "ai-security.md" >}}) · [Evaluation]({{< relref "model-evaluation.md" >}}) · [Observability]({{< relref "observability.md" >}}) · [Responsible AI]({{< relref "responsible-ai.md" >}}) | [Adaptation]({{< relref "/deep-dives/adaptation" >}}) · [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) · [RAG evaluation]({{< relref "/deep-dives/rag-evaluation" >}}) | [AI system design]({{< relref "/building/ai-system-design" >}}) · [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) | ○ Evals + ship lab |
| **Serving & inference** | [The AI API]({{< relref "the-ai-api.md" >}}) · [Cost & tokens]({{< relref "cost-and-tokens.md" >}}) · [Choosing a model]({{< relref "choosing-a-model.md" >}}) | [Adaptation]({{< relref "/deep-dives/adaptation" >}}) | [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Serving models]({{< relref "/building/serving-models" >}}) | ○ Ship to production lab |

## Agent engineering — four layers

Opening Claude Code, writing prompts or adding a skill file is not the same as understanding
agents. The skill stacks in four layers, and each one needs the layer below it:

| Layer | The question it answers | In the vault |
| --- | --- | --- |
| **Mechanics** | How does an agent work? Context management, tool use, subagents, model selection, the loop, the harness. | [Agents thread](#follow-one-topic-in-depth) · [Lab 2 ✓]({{< relref "/hands-on/lab-agent-harness" >}}) |
| **Craft** | How do I get work I can *trust*? An agent-ready repo, a clear spec, and verification of the output. | ○ Lab 3 · ○ Lab 4 |
| **Scale** | How do I go from one agent to many? Level 1 one agent → Level 2 parallel subagents → Level 3 an orchestrator while you own goals and decisions. | [Multi-agent]({{< relref "/deep-dives/multi-agent" >}}) · [Fleet looping]({{< relref "/building/loop-engineering/fleet-looping" >}}) · ○ Lab 4 |
| **Judgment** | What is worth building, and did it work? Experiments with objectives, and evidence colleagues can check. | ○ Stage 4 |

**Verification** runs through all four. A faster agent only helps if you can tell good output
from bad. The Level 1 → 3 ladder measures **breadth**: how many agents, and who coordinates
them. [The Four Levels of Loops]({{< relref "/building/loop-engineering/levels" >}}) measure
**depth**: what wraps each loop. They are different axes, and a real system has a position on
both.
