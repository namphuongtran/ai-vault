---
title: "Building with AI (Giai đoạn 2)"
linkTitle: "Building with AI"
weight: 4
type: docs
no_list: true
menu:
  main:
    weight: 4
description: >
  Kiến trúc thực hành để xây hệ thống AI.
---

Nếu [Nền tảng]({{< relref "/foundations" >}}) giải thích các mảnh ghép và
[Deep Dives]({{< relref "/deep-dives" >}}) đào sâu hơn, thì **Giai đoạn 2** là về lắp ráp chúng
thành hệ thống thật — kèm sơ đồ cho phần kiến trúc.

## Lộ trình

```mermaid
flowchart LR
    A[AI system design] --> S[Scaling to production] --> V[Serving models] --> B[Building a RAG system]
    B --> C[Agentic RAG] --> D[The agent harness] --> E[Loop engineering]
    E --> F[From prompts to graphs] --> G[AI code structure] --> H[Tooling and frameworks]
```

## Trong phần này

1. [AI system design]({{< relref "/building/ai-system-design" >}}) — hình hài chuẩn của một app AI.
2. [Scaling to production]({{< relref "/building/scaling-to-production" >}}) — gateway, caching, serving, queue, reliability, chi phí ở quy mô.
3. [Serving models]({{< relref "/building/serving-models" >}}) — tầng inference: tự host, quantization, engine, queue, routing.
4. [Building a RAG system]({{< relref "/building/building-rag" >}}) — kiến trúc tham chiếu end-to-end.
5. [Agentic RAG]({{< relref "/building/agentic-rag" >}}) — truy xuất do agent dẫn dắt, không phải pipeline cố định.
6. [The agent harness]({{< relref "/building/agent-harness" >}}) — vòng lặp, context, tools, memory, guardrail.
7. [Loop engineering]({{< relref "/building/loop-engineering" >}}) — thiết kế chính các vòng lặp: closed loop, validator, orchestration.
8. [From prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) — năm engineering discipline như một dòng tiến hoá.
9. [AI code structure]({{< relref "/building/ai-code-structure" >}}) — cách tổ chức codebase app AI.
10. [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) — SDK, framework, MCP, deployment.

## Yêu cầu trước

Hãy học qua [Giai đoạn 0 — Nền tảng]({{< relref "/foundations" >}}) và
[Giai đoạn 1 — Deep Dives]({{< relref "/deep-dives" >}}) trước — Giai đoạn 2 xây trực tiếp trên cả hai.
