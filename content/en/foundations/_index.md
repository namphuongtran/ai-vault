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
*operating* them in production. New here? Start with
**[AI coding assistants]({{< relref "/foundations/ai-coding-assistants" >}})** — the tools you
already use — then Module 1.

```mermaid
flowchart TB
    Start[Start here - AI coding assistants] --> M1[Module 1 - Understand]
    M1 --> M2[Module 2 - Work with a model]
    M2 --> M3[Module 3 - Ground it in your data]
    M3 --> M4[Module 4 - Make it act]
    M4 --> M5[Module 5 - Operate and govern]
```

### Module 1 · Understand

*Goal: know what these models are and how they behave.*

1. [The AI landscape]({{< relref "/foundations/ai-landscape" >}})
2. [Foundation models]({{< relref "/foundations/foundation-models" >}})
3. [Generative AI]({{< relref "/foundations/generative-ai" >}})
4. [Multimodality]({{< relref "/foundations/multimodality" >}})
5. [How LLMs work]({{< relref "/foundations/how-llms-work" >}})
6. [Under the hood]({{< relref "/foundations/under-the-hood" >}})
7. [How models are trained]({{< relref "/foundations/training-lifecycle" >}})
8. [Limitations & failure modes]({{< relref "/foundations/limitations" >}})

### Module 2 · Work with a model

*Goal: talk to a model and control its output.*

1. [Choosing a model]({{< relref "/foundations/choosing-a-model" >}})
2. [Reasoning models]({{< relref "/foundations/reasoning-models" >}})
3. [The AI API]({{< relref "/foundations/the-ai-api" >}})
4. [Inference parameters]({{< relref "/foundations/inference-parameters" >}})
5. [Structured outputs]({{< relref "/foundations/structured-outputs" >}})
6. [Cost & tokens]({{< relref "/foundations/cost-and-tokens" >}})
7. [Prompt engineering]({{< relref "/foundations/prompt-engineering" >}})
8. [Context engineering]({{< relref "/foundations/context-engineering" >}})

### Module 3 · Ground it in your data

*Goal: make answers use your own, current data.*

1. [Embeddings]({{< relref "/foundations/embeddings" >}})
2. [RAG]({{< relref "/foundations/rag" >}})

### Module 4 · Make it act

*Goal: let the model use tools and run as an agent.*

1. [Tool & function calling]({{< relref "/foundations/tool-function-calling" >}})
2. [Agentic AI]({{< relref "/foundations/agentic-ai" >}})
3. [Agents]({{< relref "/foundations/agents" >}})
4. [MCP]({{< relref "/foundations/mcp" >}})

### Module 5 · Operate & govern

*Goal: ship it safely, measurably, and responsibly.*

1. [Guardrails]({{< relref "/foundations/guardrails" >}})
2. [AI security]({{< relref "/foundations/ai-security" >}})
3. [Model evaluation]({{< relref "/foundations/model-evaluation" >}})
4. [Observability]({{< relref "/foundations/observability" >}})
5. [Responsible AI]({{< relref "/foundations/responsible-ai" >}})
