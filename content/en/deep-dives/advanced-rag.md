---
title: "Advanced RAG"
weight: 1
description: Chunking, hybrid retrieval, re-ranking, query transforms, and RAG evaluation.
---

Builds on [RAG in Foundations]({{< relref "/foundations/rag" >}}). Basic RAG often
under-performs because of *retrieval* quality, not the model. These techniques target that.

## Chunking strategies

How you split documents strongly affects retrieval quality.

| Strategy | Idea | When |
| ---------- | ------ | ------ |
| Fixed-size | Split every N tokens with overlap | Simple, uniform text |
| Recursive | Split on structure (headings → paragraphs → sentences) | Most documents |
| Semantic | Split where meaning shifts (embedding distance) | Dense, mixed-topic text |
| Document-aware | Respect tables, code blocks, sections | PDFs, technical docs |

Keep chunks self-contained; add a small **overlap** (e.g. 10–20%) so context isn't cut
mid-thought.

## Retrieval: dense, sparse, hybrid

- **Dense** — embedding similarity; captures meaning and paraphrase.
- **Sparse** — keyword match (BM25); captures exact terms, names, codes.
- **Hybrid** — combine both, then fuse scores (e.g. Reciprocal Rank Fusion). Usually the
  strongest default, since each covers the other's blind spots.

## Re-ranking

Retrieve a wide set (e.g. top 50), then re-score with a **cross-encoder** re-ranker that
reads query and passage together, and keep the top few. More accurate than embedding
similarity alone, at extra cost — so apply it only to the shortlist.

## Query transformation

The user's question is often not the best search query.

- **Multi-query** — generate several rephrasings, retrieve for each, merge.
- **HyDE** — generate a hypothetical answer, embed *that*, and search with it.
- **Decomposition** — break a complex question into sub-questions retrieved separately.

## Evaluating RAG

Measure retrieval and generation separately:

- **Context precision / recall** — did retrieval surface the right passages?
- **Faithfulness** — is the answer grounded in those passages?
- **Answer relevance** — does it actually address the question?

See [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}).

## Common failure modes

- Chunks too large (noise) or too small (lost context).
- Retrieval misses exact terms → add sparse/hybrid.
- Right passages retrieved but ranked low → add re-ranking.
- Answer drifts from context → tighten the prompt and check faithfulness.
