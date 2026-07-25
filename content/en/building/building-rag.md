---
title: "Building a RAG System"
linkTitle: "Building a RAG System"
weight: 3
description: An end-to-end reference architecture — the ingest pipeline and the query pipeline.
---

Builds on [RAG in Foundations]({{< relref "rag.md" >}}). A real RAG system is **two
pipelines** that meet at the vector store: one runs *offline* to index your data, the other
runs *online* per question.

## The two pipelines

```mermaid
flowchart LR
    subgraph Ingest[Ingest pipeline - offline]
      Docs[Documents] --> Parse[Parse] --> Chunk[Chunk] --> Emb1[Embed]
    end
    Emb1 --> Vec[(Vector store)]
    subgraph Query[Query pipeline - online]
      Q[User question] --> Emb2[Embed query] --> Ret[Retrieve top-k]
      Ret --> Aug[Augment prompt] --> Model --> Ans[Answer]
    end
    Vec --> Ret
```

## Ingest pipeline (offline)

Runs when data changes, not per request:

1. **Parse** documents (PDF, HTML, Word) into clean text.
2. **Chunk** into passages sized for retrieval.
3. **Embed** each chunk with an [embedding model]({{< relref "embeddings.md" >}}).
4. **Store** the vectors (+ source metadata) in the vector store.

Re-run it when documents change — no model retraining needed.

## Query pipeline (online)

Runs per user question:

1. **Embed** the question with the *same* embedding model.
2. **Retrieve** the top-k most similar chunks from the vector store.
3. **Augment** the prompt with those chunks as context.
4. **Generate** the answer — ideally with citations back to the sources.

## The components you build

| Component | Job |
| ----------- | ----- |
| Ingestion job | Parse → chunk → embed → store (scheduled or on change) |
| Embedding model | Same model for documents and queries |
| Vector store | Index + similarity search (pgvector, FAISS, …) |
| Retriever | Fetch top-k (add hybrid + re-ranking as needed) |
| Orchestrator | Build the augmented prompt, call the model, format citations |

## Getting it right

Most RAG quality problems are **retrieval** problems, not model problems — chunking, hybrid
search, and re-ranking are the levers. See
[Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) for those, and evaluate retrieval and
generation separately (see [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}})).

## Sources

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) — [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
- Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) — [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
