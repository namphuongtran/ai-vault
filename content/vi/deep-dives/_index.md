---
title: "Deep Dives (Giai đoạn 1)"
linkTitle: "Deep Dives"
weight: 2
type: docs
no_list: true
menu:
  main:
    weight: 2
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
    A[Prompt patterns] --> B[Types of RAG] --> C[Advanced RAG]
    C --> D[Agent patterns] --> E[Adaptation] --> F[Evaluation in practice]
```

## Trong phần này

1. [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) — kỹ thuật suy luận,
   structured output, phân rã, tối ưu prompt.
2. [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) — họ RAG; cái nào là kiến trúc
   vs kỹ thuật.
3. [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) — chunking, hybrid retrieval,
   re-ranking, query transform.
4. [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) — vòng lặp ReAct, thiết kế
   tool, memory, multi-agent, reflection.
5. [Adaptation]({{< relref "/deep-dives/adaptation" >}}) — chọn giữa prompting, RAG và
   fine-tuning.
6. [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) — bộ eval,
   LLM-as-judge, offline vs online, regression testing.
