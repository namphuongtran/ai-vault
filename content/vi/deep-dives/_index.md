---
title: "Deep Dives (Giai đoạn 1)"
linkTitle: "Deep Dives"
weight: 3
type: docs
no_list: true
menu:
  main:
    weight: 3
description: >
  Đào sâu hơn một mức vào các chủ đề cốt lõi ở Giai đoạn 0 — những phần thực sự hữu ích khi
  xây hệ thống thật.
---

**Giai đoạn 1** đào sâu vào các chủ đề đã giới thiệu ở
[Nền tảng]({{< relref "/foundations" >}}). Nếu Giai đoạn 0 trả lời *cái gì* và *khi nào*,
thì Giai đoạn 1 trả lời *như thế nào* — các chiến lược, mẫu (pattern) và đánh đổi xuất hiện
khi bạn xây hệ thống thật.

## Lộ trình

Các bài đào sâu đi theo đúng trục module của Giai đoạn 0 — prompt, rồi dữ liệu, rồi agent,
rồi vận hành:

```mermaid
flowchart LR
    A[Prompt patterns] --> B[Vector databases] --> C[Types of RAG] --> D[Advanced RAG]
    D --> E[Agent patterns] --> F[Agent memory] --> G[Adaptation] --> H[Evaluation in practice]
```

## Trong phần này

1. [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) — kỹ thuật suy luận,
   structured output, phân rã, tối ưu prompt.
2. [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) — chỉ mục ANN (HNSW,
   IVF, PQ), lọc metadata, chọn store.
3. [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) — họ RAG; cái nào là kiến trúc
   vs kỹ thuật.
4. [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) — chunking, hybrid retrieval,
   re-ranking, query transform.
5. [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) — vòng lặp ReAct, thiết kế
   tool, multi-agent, reflection.
6. [Agent memory]({{< relref "/deep-dives/agent-memory" >}}) — các loại bộ nhớ, và khi nào
   mỗi loại xứng đáng có mặt.
7. [Adaptation]({{< relref "/deep-dives/adaptation" >}}) — chọn giữa prompting, RAG và
   fine-tuning.
8. [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) — bộ eval,
   LLM-as-judge, offline vs online, regression testing.
