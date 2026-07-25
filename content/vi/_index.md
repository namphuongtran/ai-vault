---
title: AI Vault
description: Kho kiến thức cá nhân để học về AI.
type: docs
no_list: true
cascade:
  - _target:
      path: /**
    type: docs
---

Kho kiến thức cá nhân cho mọi thứ mình đang học về Trí tuệ nhân tạo — ghi chú, tài liệu tham
khảo và các mô hình tư duy, được sắp xếp thành một lộ trình học từ nền tảng đến nâng cao.

Nội dung được viết chủ yếu bằng **tiếng Anh**, kèm bản dịch **tiếng Việt** truy cập được qua
nút chuyển ngôn ngữ ở thanh điều hướng phía trên.

## Lộ trình học

Vault được tổ chức thành một lộ trình theo giai đoạn — từ *hiểu* AI, đến *đào sâu* các chủ đề
cốt lõi, rồi đến *xây* hệ thống thật.

```mermaid
flowchart LR
    subgraph S0["Stage 0 · Foundations ✓"]
      A0[28 concepts + diagrams]
    end
    subgraph S1["Stage 1 · Deep Dives ✓"]
      A1[8 deep dives]
    end
    subgraph S2["Stage 2 · Building with AI ✓"]
      A2[System design · RAG · agentic RAG · harness · code structure]
    end
    subgraph S3["Stage 3 · Hands-on ◐"]
      A3[Lab 1 RAG chatbot ✓ + 5 planned]
    end
    S0 --> S1 --> S2 --> S3
```

- **[Giai đoạn 0 — Nền tảng]({{< relref "/foundations" >}})** ✓ — các khối kiến thức cốt lõi,
  cho builder kỹ thuật *dùng* AI: mô hình, prompting, context, embeddings, RAG, tool, agent,
  MCP, guardrail, security, đánh giá, observability.
- **[Giai đoạn 1 — Deep Dives]({{< relref "/deep-dives" >}})** ✓ — đào sâu hơn các chủ đề hữu
  ích trong hệ thống thật: prompt patterns, vector databases, types of RAG, advanced RAG,
  agent patterns, agent memory, adaptation, evaluation in practice.
- **[Giai đoạn 2 — Building with AI]({{< relref "/building" >}})** ✓ — lắp ráp các mảnh ghép
  thành hệ thống thật: AI system design, building RAG, agentic RAG, agent harness, code
  structure, và tooling & frameworks.
- **[Giai đoạn 3 — Hands-on]({{< relref "/hands-on" >}})** — *đang tiến hành* — lab thật, mở
  đầu bằng một RAG chatbot xây qua bảy bước kiểm chứng được.

Mới bắt đầu? Hãy vào **[Giai đoạn 0 — Nền tảng]({{< relref "/foundations" >}})**. Agenda đầy
đủ — kể cả các giai đoạn hands-on dự định — nằm ở trang
**[Roadmap]({{< relref "/roadmap" >}})**.
