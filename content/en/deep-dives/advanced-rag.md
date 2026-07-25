---
title: "Advanced RAG"
weight: 4
description: Chunking, hybrid retrieval, re-ranking, query transforms, and RAG evaluation.
---

Builds on [RAG in Foundations]({{< relref "rag.md" >}}). Basic RAG often
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

Why hybrid wins, in one query: *"error E-4012 when the invoice sync times out."* Dense
retrieval finds passages about *invoice synchronization timeouts* (meaning) but misses the
exact code; sparse finds every mention of *E-4012* (exact term) but not the paraphrased
troubleshooting doc. Fused, the right page ranks first.

## Re-ranking

Retrieve a wide set (e.g. top 50), then re-score with a **cross-encoder** re-ranker that
reads query and passage together, and keep the top few. More accurate than embedding
similarity alone, at extra cost — so apply it only to the shortlist.

## Context compression

Retrieved chunks carry a lot of text that doesn't answer the question — it wastes tokens and
dilutes the model's attention. **Context compression** trims each chunk to just the relevant
part before it reaches the model:

- **Extractive** — keep only the sentences that match the query (a small model or filter
  scores each sentence).
- **Abstractive** — summarize the chunk down to its query-relevant facts.

Example: a 1,200-token policy chunk retrieved for *"what's the refund window?"* compresses to
the two sentences stating the 30-day window — cheaper, and *more* faithful, because the model
isn't distracted by the surrounding text. Apply it after re-ranking, on the final shortlist;
skip it when chunks are already tight.

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

## Sources

- Gao et al., *Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)* (2022) — [arXiv:2212.10496](https://arxiv.org/abs/2212.10496)
- Jiang et al., *LLMLingua: Compressing Prompts for Accelerated Inference* (2023) — [arXiv:2310.06839](https://arxiv.org/abs/2310.06839)
- Reimers & Gurevych, *Sentence-BERT* (2019, cross-encoders for re-ranking) — [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) — [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) — [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
