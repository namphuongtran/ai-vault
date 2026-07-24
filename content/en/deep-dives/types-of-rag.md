---
title: "Types of RAG"
weight: 1
description: The RAG family — standard, advanced, agentic, graph, multimodal — and which is an architecture vs a technique.
---

"RAG" has grown into a family of variants. The confusion is that some are distinct
**architectures** while others are just **techniques** used inside one. This page separates them.

## The family

| Type | What's different | When to use |
| ------ | ------------------ | ------------- |
| **Standard (naive) RAG** | Fixed pipeline: retrieve top-k → augment → generate | Simple Q&A over documents |
| **Advanced RAG** | Better retrieval: hybrid search, re-ranking, query transforms | When naive retrieval misses |
| **Agentic RAG** | An agent decides *when* and *what* to retrieve, and can iterate | Complex, multi-step questions |
| **Graph RAG** | Retrieves over a knowledge graph (entities + relationships) | Connected / multi-hop questions |
| **Multimodal RAG** | Retrieves images, tables, audio — not just text | Mixed-media sources |

## Architectures vs. techniques

This is the distinction that clears up the confusion:

- **Architectures** (the rows above) change the *shape* of the system.
- **Techniques** improve one step inside an architecture — they are **not** separate RAG types:
  - **Hybrid search** (dense + keyword), **re-ranking**, and **query transforms** live inside
    [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}).
  - **CRAG** (corrective RAG) and **Self-RAG** add a self-check step ("is the retrieved context
    good enough?") — refinements, not a new architecture.

So "we use hybrid search" and "we use agentic RAG" aren't the same kind of statement: the first
is a technique, the second is an architecture.

## Which one?

```mermaid
flowchart TD
    Start[Need RAG] --> Shape{What shape is your data?}
    Shape -->|graph / linked| Graph[Graph RAG]
    Shape -->|images / audio| MM[Multimodal RAG]
    Shape -->|plain text| R{Is retrieval good enough?}
    R -->|yes| Naive[Standard RAG]
    R -->|no| Adv[Advanced RAG - hybrid + rerank]
    Adv --> Multi{Needs multi-step reasoning?}
    Multi -->|yes| Agentic[Agentic RAG]
    Multi -->|no| Adv
```

## Where to go next

- Improve retrieval → [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}).
- Build the standard pipeline → [Building a RAG system]({{< relref "/building/building-rag" >}}).
- Agent-driven retrieval → Agentic RAG (Stage 2, coming soon).

Start simple. Move to advanced when retrieval is the bottleneck, and to agentic only when the
question genuinely needs multi-step reasoning.

## Sources

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) — [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- Asai et al., *Self-RAG* (2023) — [arXiv:2310.11511](https://arxiv.org/abs/2310.11511)
- Yan et al., *Corrective RAG (CRAG)* (2024) — [arXiv:2401.15884](https://arxiv.org/abs/2401.15884)
- Edge et al., *From Local to Global: A Graph RAG Approach* (2024) — [arXiv:2404.16130](https://arxiv.org/abs/2404.16130)
