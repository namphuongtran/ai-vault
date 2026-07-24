---
title: "AI System Design"
linkTitle: "AI System Design"
weight: 1
description: Hình hài chuẩn của một app AI — model chỉ là một component trong nhiều component.
---

Xây một tính năng AI phần lớn là công việc *hệ thống* — model chỉ là một component trong nhiều
thứ. Trang này cho bạn hình hài chuẩn để xây quanh đó.

## Bức tranh tổng

```mermaid
flowchart LR
    U[User] --> App[Your AI app]
    App --> Model[Model API - hosted LLM]
    App --> Data[(Your data - docs, DBs)]
```

Người dùng nói chuyện với app của bạn; app nói chuyện với một model được host và với dữ liệu của
bạn. Bạn sở hữu mọi thứ trừ bản thân model.

## Các component chuẩn

```mermaid
flowchart LR
    U[User] --> UI[Frontend - web or chat]
    subgraph App[Your AI app]
      UI --> Orch[Orchestrator / harness]
    end
    Orch --> Vec[(Vector store - embeddings)]
    Orch --> Model[Model API - LLM]
    Orch --> Tools[Tools / external systems]
    Orch -. traces .-> Obs[Observability]
```

**Orchestrator (harness)** là "bộ não" bạn xây: nó lắp ráp prompt, quản lý
[context window]({{< relref "/foundations/context-engineering" >}}), chạy
[agent loop]({{< relref "/foundations/agentic-ai" >}}), gọi
[tool]({{< relref "/foundations/tool-function-calling" >}}), và áp
[guardrail]({{< relref "/foundations/guardrails" >}}).

## Mỗi khái niệm nền tảng nằm ở đâu

| Khái niệm | Nằm ở |
| ----------- | ------- |
| Prompting, context | Orchestrator |
| Embeddings, RAG | Vector store + retrieval |
| Tools, agents | Vòng lặp orchestrator + tools |
| Guardrails, security | Quanh đầu vào và đầu ra |
| Evaluation, observability | Xuyên suốt, bao quanh mọi thứ |

## Nguyên tắc thiết kế

- Model là **stateless** — bạn sở hữu state và context.
- Đặt **tính xác định trong code**, phần phán đoán ở model.
- **Neo** bằng dữ liệu, **ràng buộc** bằng schema, **kiểm soát** các hành động rủi ro.
- **Đo** mọi thứ — eval offline, trace online.
