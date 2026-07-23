---
title: "Prompt Patterns"
weight: 3
description: Reasoning techniques, structured output, decomposition, and prompt optimization.
---

Builds on [Prompt Engineering in Foundations]({{< relref "/foundations/prompt-engineering" >}}).
Patterns for harder tasks where a single well-formed prompt isn't enough.

## Reasoning techniques

- **Chain-of-thought** — ask for step-by-step reasoning before the answer; helps on
  multi-step problems.
- **Self-consistency** — sample several reasoning paths and take the majority answer; trades
  cost for reliability.
- **Least-to-most** — solve easier sub-problems first, then use them to solve the harder one.

## Structured output

When the output feeds another system, constrain its shape:

- Ask for **JSON** against an explicit schema; validate and retry on failure.
- Prefer native **function/tool calling** or structured-output modes over parsing free text.
- Keep schemas small and flat; describe each field.

## Decomposition and chaining

Split a big task into a **chain** of smaller prompts, each with one job and a checkable
output. Easier to test, debug, and swap. Prefer chaining over one mega-prompt when steps
have distinct goals (extract → transform → format).

## Few-shot selection

Examples steer format and style — but *which* examples matters:

- Pick examples close to the current input (retrieve them dynamically for variety).
- Cover edge cases and the exact output format.
- Too many examples waste context and can overfit to their phrasing.

## Optimization

- Iterate against a small **eval set**, not vibes (see
  [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}})).
- Change one thing at a time; keep a prompt changelog.
- Use **prompt caching** for stable prefixes (instructions, few-shot blocks) to cut cost and
  latency.

## Anti-patterns

- Cramming many unrelated jobs into one prompt.
- Vague success criteria ("make it good").
- Relying on examples to fix a task the instructions never state clearly.
