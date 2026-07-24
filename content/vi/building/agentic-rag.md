---
title: "Agentic RAG"
linkTitle: "Agentic RAG"
weight: 3
description: Truy xuất do agent dẫn dắt — tự quyết khi nào, truy gì, bao nhiêu lần — không phải pipeline cố định.
---

Tiếp nối [Agentic AI]({{< relref "/foundations/agentic-ai" >}}) và
[Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}). Trong **standard RAG**, pipeline là
cố định — luôn truy xuất một lần rồi sinh câu trả lời. **Agentic RAG** giao quyền đó cho một
[agent]({{< relref "/foundations/agents" >}}): nó tự quyết *có truy xuất không*, *truy gì*, và
*bao nhiêu lần*, dùng truy xuất như một tool.

## Standard vs agentic

```mermaid
flowchart LR
    Q1[Question] --> R1[Retrieve once] --> G1[Generate] --> A1[Answer]
```

Standard RAG (trên) là một lượt cố định. Agentic RAG (dưới) là một vòng lặp do agent điều khiển:

```mermaid
flowchart TD
    Q[Question] --> A[Agent reasons]
    A --> D{Need to retrieve?}
    D -->|no| Ans[Answer]
    D -->|yes| R[Pick query + source, retrieve]
    R --> C{Enough to answer?}
    C -->|no| A
    C -->|yes| Ans
```

## Agent tự quyết những gì

- **Có truy xuất không** — có câu hỏi không cần.
- **Truy gì** — thường là viết lại câu hỏi của người dùng, hoặc nhiều truy vấn con.
- **Nguồn nào** — các vector store khác nhau, web search, database, API.
- **Bao nhiêu vòng** — truy xuất, đọc, rồi truy tiếp cho một dữ kiện bổ sung (multi-hop).
- **Context đã đủ chưa** — truy lại hoặc hỏi làm rõ nếu chưa.

Truy xuất trở thành một [tool]({{< relref "/foundations/tool-function-calling" >}}) mà agent gọi,
không phải bước đầu tiên cố định.

## Khi nào nên dùng

- ✅ **Câu hỏi multi-hop** — câu trả lời cần một dữ kiện đòi hỏi tra lần hai.
- ✅ **Nhiều nguồn** — agent định tuyến tới đúng nguồn.
- ✅ **Truy vấn mơ hồ** — agent có thể viết lại, hoặc hỏi, trước khi truy xuất.
- ❌ **Q&A đơn giản trên một corpus** — [standard RAG]({{< relref "/building/building-rag" >}})
  nhanh hơn, rẻ hơn, dễ đoán hơn.

## Đánh đổi

Mạnh hơn, nhưng nhiều độ trễ, chi phí và bộ phận chuyển động hơn — và khó làm cho đáng tin hơn
(agent có thể lặp hoặc truy xuất kém). Thêm [guardrail]({{< relref "/foundations/guardrails" >}}),
giới hạn số bước, và [đánh giá]({{< relref "/deep-dives/evaluation-in-practice" >}}) — đặc biệt là
các kiểm tra chất lượng truy xuất trong [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}).
Chỉ dùng agentic RAG khi standard hoặc advanced RAG thực sự không đủ.
