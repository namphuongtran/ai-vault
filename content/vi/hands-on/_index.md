---
title: "Hands-on (Giai đoạn 3)"
linkTitle: "Hands-on"
weight: 5
type: docs
no_list: true
menu:
  main:
    weight: 5
description: >
  Dự án thật, xây tăng dần — nơi các giai đoạn trước trở thành hệ thống chạy được.
---

Nếu [Nền tảng]({{< relref "/foundations" >}}) giải thích các mảnh ghép và
[Building]({{< relref "/building" >}}) trình bày kiến trúc, thì **Giai đoạn 3** là lúc bạn gõ
phím. Mọi lab đều tăng dần: mỗi bước chạy và được kiểm chứng trước khi sang bước sau, vì hệ
thống production thực tế lớn lên đúng như vậy.

## Lộ trình

```mermaid
flowchart LR
    L1[Lab 1 - RAG chatbot ✓] --> L2[Lab 2 - Agent + MCP server ○] --> L3[Lab 3 - Evals + observability ○]
    L3 --> L4[LoRA fine-tuning ○] --> L5[Multimodal app ○] --> L6[Ship to production ○]
```

## Các lab

1. [Lab 1 — RAG chatbot trên tài liệu của chính bạn]({{< relref "/hands-on/lab-rag-chatbot" >}}) ✓
   — hạ tầng → ingestion → keyword search → hybrid → RAG hoàn chỉnh → monitoring + cache → agentic.
2. ○ **Lab 2 — agent với tools + tự viết một MCP server.**
3. ○ **Lab 3 — eval harness + observability** cho lab 1–2.
4. ○ **Fine-tuning thực hành (LoRA)** — tinh chỉnh một model nhỏ cho giọng và schema.
5. ○ **App multimodal** — đầu vào vision, trích xuất tài liệu.
6. ○ **Ship to production** — deploy, kiểm soát chi phí, monitoring.

## Yêu cầu trước

Hãy đi hết [mạch RAG]({{< relref "/roadmap#đào-sâu-một-chủ-đề" >}}) của Giai đoạn 0–2 trước —
các lab mặc định bạn đã nắm khái niệm và chỉ tham chiếu thay vì giải thích lại.
