---
title: "Building with AI (Giai đoạn 2)"
linkTitle: "Building with AI"
weight: 3
type: docs
menu:
  main:
    weight: 3
description: >
  Kiến trúc thực hành để xây hệ thống AI — dự kiến, kèm C4 diagram.
---

> **Trạng thái: dự kiến — sắp tới.** Giai đoạn 2 chuyển từ *khái niệm* sang *xây dựng*.

Nếu [Nền tảng]({{< relref "/foundations" >}}) giải thích các mảnh ghép và
[Deep Dives]({{< relref "/deep-dives" >}}) đào sâu hơn, thì **Giai đoạn 2** là về lắp ráp hệ
thống thật — với **[C4](https://c4model.com/) diagram** cho thiết kế hệ thống.

## Các trang dự kiến

1. **AI system design** — mẫu kiến trúc; C4 system-context & container diagram.
2. **Building a RAG system** — kiến trúc tham chiếu end-to-end.
3. **Agentic RAG** — truy xuất do agent dẫn dắt, không phải pipeline cố định.
4. **The agent harness** — xây vòng lặp, quản lý context, và thực thi tool.
5. **AI code structure** — cách tổ chức codebase của ứng dụng AI.
6. **Tooling** — Claude Agent SDK vs Anthropic API SDK, Managed Agents, agent framework
   (Microsoft Agent Framework, LangGraph), xây skill / plugin & MCP server, deployment.

## Yêu cầu trước

Hãy học qua **[Giai đoạn 0 — Nền tảng]({{< relref "/foundations" >}})** và
**[Giai đoạn 1 — Deep Dives]({{< relref "/deep-dives" >}})** trước — Giai đoạn 2 xây trực tiếp trên cả hai.
