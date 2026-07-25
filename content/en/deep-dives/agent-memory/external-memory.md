---
title: "External Memory"
weight: 5
description: Outside knowledge in a vector DB, fetched at inference — this is RAG.
---

*Bring outside knowledge in.*

## What it is

Knowledge kept outside the model in a vector DB and fetched at inference by similarity search.
This *is* [RAG]({{< relref "rag.md" >}}), seen through the lens of memory.

```mermaid
flowchart LR
    Q[Question] --> Emb[Embed query] --> Sim[Similarity search]
    Sim --> DB[(Vector DB - embeddings, metadata, sources)]
    DB --> TopK[Top-K chunks] --> Ctx[Inject into context] --> LLM[Model answers]
```

## When you need it

The knowledge is too large to keep in the context window and changes often — so you look it
up on demand instead of baking it in.

## Where it lives

A [vector database]({{< relref "/deep-dives/vector-databases" >}}), holding embeddings,
metadata, and source references for citations.

## Example

A support agent embeds your docs, stores them, and retrieves the most relevant chunks when a
user asks — grounding the answer and citing the source.

## Related

- [RAG]({{< relref "rag.md" >}}) and [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) — the full mechanics.
- Distinct from [semantic memory]({{< relref "semantic-memory.md" >}}): external is *your documents*, semantic is *facts learned about the user*.
