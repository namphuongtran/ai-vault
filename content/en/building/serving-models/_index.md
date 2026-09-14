---
title: "Serving Models"
linkTitle: "Serving models"
weight: 3
type: docs
no_list: true
description: The inference layer — whether to self-host, how to make a model fit, how to serve it fast, and how to survive failure.
---

## Goal

Everything between *"I have a model"* and *"my app can call it under load."*
[The AI API]({{< relref "the-ai-api.md" >}}) taught you to make one call;
[AI system design]({{< relref "/building/ai-system-design" >}}) and
[scaling to production]({{< relref "/building/scaling-to-production" >}}) surveyed the system
around it. This section is the layer in between — **the inference layer** — and it is the part
of the stack a managed API hides from you until the day you need it.

## The layer

```mermaid
flowchart LR
    App[Your app] --> GW[Gateway - routing and fallback]
    GW --> LB[Queue and load balancer]
    LB --> ENG[Serving engine - vLLM or TensorRT or SGLang]
    ENG --> W[Model weights - quantized]
    W --> GPU[GPU or CPU you chose]
```

Read the diagram right to left and you have the order of this section: you pick the hardware,
you make the weights fit it, you put an engine in front of them, you put a queue in front of
the engine, and you put a router in front of everything.

## In this section

The order is a dependency chain, not a menu — each page assumes the one above it:

| # | Page | The question it answers |
| ------ | ------ | ------ |
| 1 | [Local vs cloud]({{< relref "local-vs-cloud.md" >}}) | Should you self-host at all? |
| 2 | [Quantization]({{< relref "quantization.md" >}}) | How do you make the weights fit the hardware? |
| 3 | [Serving engines]({{< relref "serving-engines.md" >}}) | How do you get throughput out of one GPU? |
| 4 | [Load balancing & queuing]({{< relref "load-balancing-queuing.md" >}}) | How do you go from one replica to many? |
| 5 | [Routing & fallback]({{< relref "routing-and-fallback.md" >}}) | What happens when a model is slow, expensive, or down? |

**If you never self-host, read 1 and 5.** Page 1 tells you why staying on a managed API is
usually right, and page 5 applies to managed APIs unchanged — routing and fallback are the
two patterns every production AI app needs regardless of who runs the GPU.

## What each layer buys you

| Layer | Lever | Typical gain | Cost of pulling it |
| ------ | ------ | ------ | ------ |
| **Hardware choice** | Own GPUs vs pay per token | Fixed cost beats per-token above a volume threshold | Ops, capacity planning, idle spend |
| **Quantization** | Numeric precision of the weights | 2–4× less VRAM, 1.5–3× faster decode | Some quality loss — must be measured |
| **Serving engine** | Memory layout and batching | 5–20× throughput over a naive loop | A new system to operate and tune |
| **Queue + load balancer** | Admission control across replicas | Survives spikes instead of collapsing | Added latency, more moving parts |
| **Routing + fallback** | Which model answers | Big cost savings, no single point of failure | Behaviour varies by which model served you |

Each row is only worth pulling when the row above it is already tuned. Quantizing a model
that a managed API could serve you is a classic case of solving the wrong problem.

## Where to go next

- The system around this layer → [Scaling to production]({{< relref "/building/scaling-to-production" >}}).
- Whether to fine-tune the model you are serving → [Adaptation]({{< relref "/deep-dives/adaptation" >}}).
- What to measure once it is live → [Observability]({{< relref "observability.md" >}}).

Most teams should read page 1, conclude "stay on the API", implement page 5, and come back to
pages 2–4 the year they actually need them.

## Sources

- Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (2023) — [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)
- Frantar et al., *GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers* (2022) — [arXiv:2210.17323](https://arxiv.org/abs/2210.17323)
- Lin et al., *AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration* (2023) — [arXiv:2306.00978](https://arxiv.org/abs/2306.00978)
- Zheng et al., *SGLang: Efficient Execution of Structured Language Model Programs* (2023) — [arXiv:2312.07104](https://arxiv.org/abs/2312.07104)
