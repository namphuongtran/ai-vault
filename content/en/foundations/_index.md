---
title: "Foundations (Stage 0)"
linkTitle: "Foundations"
weight: 1
type: docs
no_list: true
menu:
  main:
    weight: 1
description: >
  The core building blocks of modern AI systems — from foundation models to
  responsible AI.
---

**Stage 0** is the foundation layer. The goal here is breadth, not depth: understand what
each concept *is* and *when* to use it. We go from foundation to advanced, and deeper
explanations come in later stages.

Written for **technical builders** — developers, AI/data engineers, DevSecOps, platform and
solution architects — who want to *use and apply* AI, not train models. Light on ML/DL
internals, heavy on what you need to build confidently.

## How to work through this

Follow the five modules in order — each builds on the last, from *understanding* models to
*operating* them in production. Start at
**[The AI landscape]({{< relref "/foundations/ai-landscape" >}})** and read each module top
to bottom.

```mermaid
flowchart TB
    M1[Module 1 - Understand] --> M2[Module 2 - Work with a model]
    M2 --> M3[Module 3 - Ground it in your data]
    M3 --> M4[Module 4 - Make it act]
    M4 --> M5[Module 5 - Operate and govern]
```

### Module 1 · Understand

*Goal: know what these models are and how they behave.*

1. [The AI landscape]({{< relref "/foundations/ai-landscape" >}})
2. [Generative AI]({{< relref "/foundations/generative-ai" >}})
3. [Foundation models]({{< relref "/foundations/foundation-models" >}})
4. [How LLMs work]({{< relref "/foundations/how-llms-work" >}})
5. [Under the hood]({{< relref "/foundations/under-the-hood" >}})
6. [How models are trained]({{< relref "/foundations/training-lifecycle" >}})
7. [Multimodality]({{< relref "/foundations/multimodality" >}})
8. [Limitations & failure modes]({{< relref "/foundations/limitations" >}})

### Module 2 · Work with a model

*Goal: talk to a model and control its output.*

1. [The AI API]({{< relref "/foundations/the-ai-api" >}})
2. [Inference parameters]({{< relref "/foundations/inference-parameters" >}})
3. [Prompt engineering]({{< relref "/foundations/prompt-engineering" >}})
4. [Context engineering]({{< relref "/foundations/context-engineering" >}})
5. [Structured outputs]({{< relref "/foundations/structured-outputs" >}})
6. [Reasoning models]({{< relref "/foundations/reasoning-models" >}})
7. [Cost & tokens]({{< relref "/foundations/cost-and-tokens" >}})
8. [Choosing a model]({{< relref "/foundations/choosing-a-model" >}}) — *the capstone: pick
   the right model once you know the knobs and the costs*

### Module 3 · Ground it in your data

*Goal: make answers use your own, current data.*

1. [Embeddings]({{< relref "/foundations/embeddings" >}})
2. [RAG]({{< relref "/foundations/rag" >}})

### Module 4 · Make it act

*Goal: let the model use tools and run as an agent.*

1. [Tool & function calling]({{< relref "/foundations/tool-function-calling" >}})
2. [Agents]({{< relref "/foundations/agents" >}})
3. [Agentic AI]({{< relref "/foundations/agentic-ai" >}})
4. [MCP]({{< relref "/foundations/mcp" >}})
5. [AI coding assistants]({{< relref "/foundations/ai-coding-assistants" >}}) — *a complete
   agent you already use every day*

### Module 5 · Operate & govern

*Goal: ship it safely, measurably, and responsibly.*

1. [Guardrails]({{< relref "/foundations/guardrails" >}})
2. [AI security]({{< relref "/foundations/ai-security" >}})
3. [Model evaluation]({{< relref "/foundations/model-evaluation" >}})
4. [Observability]({{< relref "/foundations/observability" >}})
5. [Responsible AI]({{< relref "/foundations/responsible-ai" >}})
