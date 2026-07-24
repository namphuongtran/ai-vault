---
title: "Building with AI (Giai đoạn 2)"
linkTitle: "Building with AI"
weight: 3
type: docs
no_list: true
menu:
  main:
    weight: 3
description: >
  Kiến trúc thực hành để xây hệ thống AI.
---

Nếu [Nền tảng]({{< relref "/foundations" >}}) giải thích các mảnh ghép và
[Deep Dives]({{< relref "/deep-dives" >}}) đào sâu hơn, thì **Giai đoạn 2** là về lắp ráp chúng
thành hệ thống thật — kèm sơ đồ cho phần kiến trúc.

## Lộ trình

```mermaid
flowchart LR
    A[AI system design] --> B[Building a RAG system] --> C[Agentic RAG]
    C --> D[The agent harness] --> E[AI code structure] --> F[Tooling and frameworks]
```

## Trong phần này

1. [AI system design]({{< relref "/building/ai-system-design" >}}) — hình hài chuẩn của một app AI.
2. [Building a RAG system]({{< relref "/building/building-rag" >}}) — kiến trúc tham chiếu end-to-end.
3. [Agentic RAG]({{< relref "/building/agentic-rag" >}}) — truy xuất do agent dẫn dắt, không phải pipeline cố định.
4. [The agent harness]({{< relref "/building/agent-harness" >}}) — vòng lặp, context, tools, memory, guardrail.
5. [AI code structure]({{< relref "/building/ai-code-structure" >}}) — cách tổ chức codebase app AI.
6. [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) — SDK, framework, MCP, deployment.

## Yêu cầu trước

Hãy học qua [Giai đoạn 0 — Nền tảng]({{< relref "/foundations" >}}) và
[Giai đoạn 1 — Deep Dives]({{< relref "/deep-dives" >}}) trước — Giai đoạn 2 xây trực tiếp trên cả hai.
