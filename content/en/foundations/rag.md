---
title: "RAG (Retrieval-Augmented Generation)"
weight: 10
description: Grounding a model's answers in external data via embeddings and a vector store.
---

## Goal

The goal of **RAG** is to retrieve relevant information from an external data source and add
it to the prompt *before* the foundation model generates an answer. This lets the model
answer from your organization's data instead of relying only on knowledge learned during
training.

## Basic pipeline

Collect documents → parse → chunk → embed → store in a vector store → retrieve → augment →
generate.

| Step | Role |
| ------ | ------ |
| Parse | Read and extract content from PDF, Word, HTML, or other sources |
| Chunking | Split documents into small passages for more precise retrieval |
| Embedding | Convert text into numeric vectors that capture semantic meaning |
| Vector store | Store and index the embeddings |
| Retrieval | Find the passages most relevant to the user's question |
| Augmentation | Insert the retrieved content into the prompt as context |
| Generation | The foundation model uses that context to produce the answer |

## Embeddings

An **embedding** converts text into a numeric vector that represents its meaning — text with
similar meaning maps to nearby vectors. Use the **same embedding model** for both documents
and the query, and measure relevance with **cosine similarity**.

## Vector database

A **vector store** stores and indexes embeddings and performs **similarity search** (often
approximate-nearest-neighbor for speed). Examples: pgvector, FAISS, Pinecone, Chroma, Weaviate.

## When to use RAG

- Internal data changes frequently.
- Answers must be based on company documents.
- You need to cite sources or keep references.
- You want to reduce hallucination with trustworthy context.
- You don't want to retrain the model every time data changes.
- You need to control the scope of knowledge the model can use.

## RAG vs. fine-tuning

Suppose a company has thousands of product manuals updated weekly. With fine-tuning, they may
need to retrain the model every time documents change. With RAG, they only update the data
source and re-sync the embeddings.
