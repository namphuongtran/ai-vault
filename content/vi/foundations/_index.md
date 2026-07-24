---
title: "Nền tảng (Giai đoạn 0)"
linkTitle: "Nền tảng"
weight: 1
type: docs
menu:
  main:
    weight: 1
description: >
  Các khối kiến thức cốt lõi của hệ thống AI hiện đại — từ foundation model đến responsible AI.
---

**Giai đoạn 0** là lớp nền tảng. Mục tiêu ở đây là chiều rộng, không phải chiều sâu: hiểu mỗi
khái niệm *là gì* và *khi nào* dùng. Chúng ta đi từ nền tảng đến nâng cao, phần giải thích sâu
hơn sẽ ở các giai đoạn sau.

Viết cho **builder kỹ thuật** — developer, AI/data engineer, DevSecOps, platform và solution
architect — những người muốn *dùng và áp dụng* AI, không phải huấn luyện mô hình. Ít đi sâu vào
ML/DL, tập trung vào những gì bạn cần để xây một cách tự tin.

## Học theo thứ tự nào

Đi theo năm module tuần tự — mỗi cái xây trên cái trước, từ *hiểu* mô hình đến *vận hành* chúng
trên production. Mới bắt đầu? Hãy xem
**[AI coding assistants]({{< relref "/foundations/ai-coding-assistants" >}})** — các công cụ bạn
đã dùng — rồi vào Module 1.

```mermaid
flowchart TB
    Start[Start here - AI coding assistants] --> M1[Module 1 - Understand]
    M1 --> M2[Module 2 - Work with a model]
    M2 --> M3[Module 3 - Ground it in your data]
    M3 --> M4[Module 4 - Make it act]
    M4 --> M5[Module 5 - Operate and govern]
```

### Module 1 · Understand

*Mục tiêu: biết các mô hình này là gì và hành xử ra sao.*

1. [The AI landscape]({{< relref "/foundations/ai-landscape" >}})
2. [Foundation models]({{< relref "/foundations/foundation-models" >}})
3. [Generative AI]({{< relref "/foundations/generative-ai" >}})
4. [How LLMs work]({{< relref "/foundations/how-llms-work" >}})
5. [How models are trained]({{< relref "/foundations/training-lifecycle" >}})

### Module 2 · Work with a model

*Mục tiêu: gọi được model và kiểm soát đầu ra.*

1. [Choosing a model]({{< relref "/foundations/choosing-a-model" >}})
2. [The AI API]({{< relref "/foundations/the-ai-api" >}})
3. [Inference parameters]({{< relref "/foundations/inference-parameters" >}})
4. [Prompt engineering]({{< relref "/foundations/prompt-engineering" >}})
5. [Context engineering]({{< relref "/foundations/context-engineering" >}})

### Module 3 · Ground it in your data

*Mục tiêu: khiến câu trả lời dùng dữ liệu của bạn, cập nhật.*

1. [Embeddings]({{< relref "/foundations/embeddings" >}})
2. [RAG]({{< relref "/foundations/rag" >}})

### Module 4 · Make it act

*Mục tiêu: cho model dùng tool và chạy như một agent.*

1. [Tool & function calling]({{< relref "/foundations/tool-function-calling" >}})
2. [Agentic AI]({{< relref "/foundations/agentic-ai" >}})
3. [Agents]({{< relref "/foundations/agents" >}})
4. [MCP]({{< relref "/foundations/mcp" >}})

### Module 5 · Operate & govern

*Mục tiêu: đưa lên production an toàn, đo được, có trách nhiệm.*

1. [Guardrails]({{< relref "/foundations/guardrails" >}})
2. [AI security]({{< relref "/foundations/ai-security" >}})
3. [Model evaluation]({{< relref "/foundations/model-evaluation" >}})
4. [Observability]({{< relref "/foundations/observability" >}})
5. [Responsible AI]({{< relref "/foundations/responsible-ai" >}})
