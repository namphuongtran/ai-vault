---
title: "Choosing a Model"
weight: 10
description: Capability vs cost vs latency vs context — how to pick the right model for a task.
---

There's rarely one "best" model — there's the right model for *this* task. Pick along a few
axes.

## The dimensions that matter

| Dimension | Question |
| ----------- | ---------- |
| Capability | Is it smart enough for the task's hardest step? |
| Speed / latency | Does the use case need fast responses (chat) or can it wait (batch)? |
| Cost | Price per input and output token — multiplied by your volume |
| Context window | How much text must it handle at once? |
| Modalities | Text only, or also images / audio? |
| Hosting | Proprietary API vs open-weight model you can self-host |

## Capability tiers

Most providers offer a **tier ladder** — a large flagship model (most capable, slower,
pricier), a mid tier (balanced), and a small model (fast, cheap, good for simple or
high-volume tasks). Match the tier to the job rather than defaulting to the biggest.

## Example — matching model to task

| Task | Pick | Why |
| ------ | ------ | ----- |
| Code autocomplete in the IDE | Small / fast model | High volume, latency-sensitive, simple |
| Summarize a support chat | Mid tier | Balanced quality vs. cost |
| Analyze a 50-page contract for risks | Flagship / reasoning | Hard, low volume, tolerates latency |

## A practical approach

1. **Prototype on a capable model** so model quality isn't the bottleneck while you build.
2. **Then optimize** — drop to a smaller/cheaper tier where quality still holds; keep the big
   one only where it's needed.
3. **Measure the trade-off** with an [eval set]({{< relref "/deep-dives/evaluation-in-practice" >}}),
   not by feel.

## Open vs proprietary

- **Proprietary (API)** — easiest, most capable, no infrastructure; you send data to a vendor.
- **Open-weight (self-host)** — full control and data residency; you run and scale the
  infrastructure.
