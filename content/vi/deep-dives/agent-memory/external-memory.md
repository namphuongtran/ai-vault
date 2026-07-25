---
title: "External Memory"
linkTitle: "External Memory"
weight: 5
description: Tri thức ngoài trong vector DB, lấy về lúc inference — chính là RAG.
---

*Mang tri thức ngoài vào.*

## Là gì

Tri thức giữ bên ngoài model trong một vector DB, lấy về lúc inference bằng similarity search.
Đây *chính là* [RAG]({{< relref "rag.md" >}}), nhìn qua lăng kính memory.

```mermaid
flowchart LR
    Q[Question] --> Emb[Embed query] --> Sim[Similarity search]
    Sim --> DB[(Vector DB - embeddings, metadata, sources)]
    DB --> TopK[Top-K chunks] --> Ctx[Inject into context] --> LLM[Model answers]
```

## Khi nào cần

Tri thức quá lớn để giữ trong context window và thay đổi thường xuyên — nên bạn tra khi cần
thay vì nhồi sẵn vào.

## Lưu ở đâu

Một [vector database]({{< relref "/deep-dives/vector-databases" >}}), chứa embedding, metadata,
và tham chiếu nguồn để trích dẫn.

## Ví dụ

Một support agent embed tài liệu của bạn, lưu lại, và truy xuất các chunk liên quan nhất khi
user hỏi — neo câu trả lời và trích nguồn.

## Liên quan

- [RAG]({{< relref "rag.md" >}}) và [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) — cơ chế đầy đủ.
- Khác [semantic memory]({{< relref "semantic-memory.md" >}}): external là *tài liệu của bạn*, semantic là *dữ kiện học về user*.
