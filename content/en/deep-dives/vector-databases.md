---
title: "Vector Databases"
weight: 2
description: How similarity search over millions of vectors works — and how to pick a store.
---

## Goal

Understand what happens inside the "vector store" box of every
[RAG]({{< relref "/foundations/rag" >}}) diagram: how a database finds the nearest neighbors
among millions of [embeddings]({{< relref "/foundations/embeddings" >}}) in milliseconds, and
which store fits which problem.

## The problem — exact search doesn't scale

Finding the closest vectors to a query means comparing it against *every* stored vector —
fine for 10k vectors, hopeless for 100M at query time. Vector databases trade a little recall
for a lot of speed with **ANN (approximate nearest neighbor)** indexes: they return *almost
certainly* the closest matches, orders of magnitude faster.

```mermaid
flowchart LR
    Q[Query vector] --> IDX[ANN index]
    IDX --> C[Candidate neighbors]
    C --> F[Filter by metadata]
    F --> K[Top-K results]
```

## The three index ideas

| Index | Intuition | Trade-off |
| ------ | ------ | ------ |
| **HNSW** — hierarchical graph | A highway network: coarse links get you to the right region fast, local links find the exact neighbors | Best recall/speed for most workloads; index lives in RAM |
| **IVF** — inverted file / partitions | Cluster vectors into buckets; search only the few buckets nearest the query | Less memory, fast to build; recall drops if the right bucket is missed |
| **PQ** — product quantization | Compress vectors into short codes; compare codes instead of full vectors | 10–100× memory savings; some precision lost — often combined with IVF |

You rarely implement these — but the knobs you *will* tune (HNSW's `efSearch`, IVF's
`nprobe`) are all the same dial: **check more candidates → better recall, more latency**.

## Metadata filtering

Real queries are rarely pure similarity: *"passages like this query — but only from the
2026 handbook, in English, for the Pro plan."* Vector stores attach **metadata** to each
vector and filter during (not after) the search. Filtering *after* the search silently
starves results: the top-K may all fail the filter, leaving you with nothing.

## Choosing a store

| Situation | Reach for |
| ------ | ------ |
| You already run Postgres; ≤ a few million vectors | **pgvector** — one less system, SQL joins with your data |
| Library inside your own process (batch, research) | **FAISS** — no server at all |
| Quick prototyping, local-first | **Chroma** |
| Managed service, zero ops | **Pinecone** |
| Self-hosted at large scale, rich filtering | **Qdrant / Milvus / Weaviate** |

The honest default: **start with pgvector**. Move to a dedicated store when scale, latency,
or filtering demands it — not before.

## Strengths & limitations

- **Strengths** — millisecond semantic search at scales exact search can't touch; metadata
  filters make retrieval precise; ANN recall is tunable per query.
- **Limitations** — *approximate*: relevant items can be missed, and you must measure recall
  (see [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}));
  indexes cost RAM and rebuild time; one more system to run, back up, and keep in sync with
  the source documents — often the flakiest part of a RAG pipeline.

## Sources

- Malkov & Yashunin, *Efficient and robust approximate nearest neighbor search using
  Hierarchical Navigable Small World graphs* (2016) — [arXiv:1603.09320](https://arxiv.org/abs/1603.09320)
- Jégou et al., *Product Quantization for Nearest Neighbor Search* (IEEE TPAMI, 2011) — [doi:10.1109/TPAMI.2010.57](https://doi.org/10.1109/TPAMI.2010.57)
- [pgvector — open-source vector similarity for Postgres](https://github.com/pgvector/pgvector)
