---
title: "Roadmap"
linkTitle: "Roadmap"
weight: 1
type: docs
no_list: true
menu:
  main:
    weight: 1
description: >
  Toàn bộ hành trình — đã viết gì, dự định gì, và đọc theo thứ tự nào.
---

Vault này là một **bản đồ sống**, không phải cuốn sách đã đóng bìa. Mục tiêu là đi xa hơn
việc *dùng* ChatGPT hay Claude: **hiểu** các hệ thống này hoạt động ra sao, **thuần thục**
những kỹ thuật quan trọng, **xây** hệ thống thật, và cuối cùng **ship** các dự án hands-on.
Trang đã viết đánh dấu ✓; trang dự định ○ — học tới đâu điền vào tới đó.

## Hành trình

```mermaid
flowchart LR
    S0[Stage 0 - Foundations ✓] --> S1[Stage 1 - Deep Dives ✓] --> S2[Stage 2 - Building ✓]
    S2 --> S3[Stage 3 - Hands-on 1 of 6] --> S4[Stage 4 - Create ○]
```

Đọc **theo hàng ngang** để tiến từng giai đoạn, hoặc chọn một hàng trong
[bảng chủ đề](#đào-sâu-một-chủ-đề) bên dưới để đào sâu một mạch kiến thức.

## Giai đoạn 0 — Nền tảng ✓

28 khái niệm trong [năm module có thứ tự]({{< relref "/foundations" >}}), từ *mô hình là gì*
đến *vận hành chúng trên production*:

1. **Understand** — bức tranh AI, generative AI, foundation model, LLM hoạt động ra sao,
   huấn luyện, multimodality, giới hạn.
2. **Work with a model** — API, tham số, prompting, context, structured outputs, reasoning
   model, chi phí, chọn model.
3. **Ground it in your data** — embeddings, RAG.
4. **Make it act** — tools, agents, agentic AI, MCP, AI coding assistants.
5. **Operate & govern** — guardrails, security, đánh giá, observability, responsible AI.

## Giai đoạn 1 — Deep Dives ✓

[Tám bài đào sâu]({{< relref "/deep-dives" >}}) theo cùng trục xương sống:
[prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) ·
[vector databases]({{< relref "/deep-dives/vector-databases" >}}) ·
[types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) ·
[advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) ·
[agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) ·
[agent memory]({{< relref "/deep-dives/agent-memory" >}}) ·
[adaptation]({{< relref "/deep-dives/adaptation" >}}) ·
[evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}).

## Giai đoạn 2 — Building with AI ✓

[Chín trang]({{< relref "/building" >}}) lắp ráp các mảnh ghép:
[AI system design]({{< relref "/building/ai-system-design" >}}) ·
[scaling to production]({{< relref "/building/scaling-to-production" >}}) ·
[building RAG]({{< relref "/building/building-rag" >}}) ·
[agentic RAG]({{< relref "/building/agentic-rag" >}}) ·
[the agent harness]({{< relref "/building/agent-harness" >}}) ·
[loop engineering]({{< relref "/building/loop-engineering" >}}) ·
[from prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) ·
[AI code structure]({{< relref "/building/ai-code-structure" >}}) ·
[tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}).

## Giai đoạn 3 — Hands-on (đang tiến hành)

[Dự án thật]({{< relref "/hands-on" >}}), xây tăng dần:

1. ✓ **[Lab: RAG chatbot trên tài liệu của chính mình]({{< relref "/hands-on/lab-rag-chatbot" >}})**
   — theo bảy bước: hạ tầng → ingestion → keyword search → hybrid search → RAG hoàn chỉnh →
   monitoring + caching → nâng cấp agentic.
2. ○ **Lab: agent với tools + tự viết một MCP server.**
3. ○ **Lab: eval harness + observability** cho lab 1–2.
4. ○ **Fine-tuning thực hành (LoRA)** — tinh chỉnh một model nhỏ cho giọng và schema.
5. ○ **App multimodal** — đầu vào vision, trích xuất tài liệu.
6. ○ **Ship to production** — deploy, kiểm soát chi phí, monitoring.

## Giai đoạn 4 — Create ○ (dự định, xa hơn)

- ○ AI product design — từ năng lực đến sản phẩm.
- ○ Case study các sản phẩm AI thật.
- ○ Ghi chú chứng chỉ & bảng ôn tập.

## Đào sâu một chủ đề

Mỗi hàng là một mạch kiến thức xuyên các giai đoạn — cách đọc vault theo chiều dọc:

| Chủ đề | Giai đoạn 0 | Giai đoạn 1 | Giai đoạn 2 | Giai đoạn 3 ○ |
| ------ | ------ | ------ | ------ | ------ |
| **Prompts** | [Prompt engineering]({{< relref "prompt-engineering.md" >}}) · [Context engineering]({{< relref "context-engineering.md" >}}) | [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) | — | — |
| **Data & RAG** | [Embeddings]({{< relref "embeddings.md" >}}) · [RAG]({{< relref "rag.md" >}}) | [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) · [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) · [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) | [Building RAG]({{< relref "/building/building-rag" >}}) · [Agentic RAG]({{< relref "/building/agentic-rag" >}}) | [Lab RAG chatbot ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) |
| **Agents** | [Tool calling]({{< relref "tool-function-calling.md" >}}) · [Agents]({{< relref "agents.md" >}}) · [Agentic AI]({{< relref "agentic-ai.md" >}}) · [MCP]({{< relref "mcp.md" >}}) | [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) · [Agent memory]({{< relref "/deep-dives/agent-memory" >}}) | [Agent harness]({{< relref "/building/agent-harness" >}}) · [Loop engineering]({{< relref "/building/loop-engineering" >}}) · [AI code structure]({{< relref "/building/ai-code-structure" >}}) | ○ Lab agent + MCP |
| **Operate** | [Guardrails]({{< relref "guardrails.md" >}}) · [AI security]({{< relref "ai-security.md" >}}) · [Đánh giá]({{< relref "model-evaluation.md" >}}) · [Observability]({{< relref "observability.md" >}}) · [Responsible AI]({{< relref "responsible-ai.md" >}}) | [Adaptation]({{< relref "/deep-dives/adaptation" >}}) · [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) | [AI system design]({{< relref "/building/ai-system-design" >}}) · [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) | ○ Lab evals + ship |
