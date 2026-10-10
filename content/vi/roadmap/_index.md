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
    S2 --> S3[Stage 3 - Hands-on 2 of 7] --> S4[Stage 4 - Create ○]
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

[Mười hai bài đào sâu]({{< relref "/deep-dives" >}}) theo cùng trục xương sống:
[prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) ·
[vector databases]({{< relref "/deep-dives/vector-databases" >}}) ·
[types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) ·
[advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) ·
[agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) ·
[agent memory]({{< relref "/deep-dives/agent-memory" >}}) ·
[multi-agent systems]({{< relref "/deep-dives/multi-agent" >}}) ·
[self-improving agents]({{< relref "/deep-dives/self-improving-agents" >}}) ·
[computer use]({{< relref "/deep-dives/computer-use" >}}) ·
[adaptation]({{< relref "/deep-dives/adaptation" >}}) ·
[evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) ·
[RAG evaluation]({{< relref "/deep-dives/rag-evaluation" >}}).

## Giai đoạn 2 — Building with AI ✓

[Mười mục]({{< relref "/building" >}}) lắp ráp các mảnh ghép:
[AI system design]({{< relref "/building/ai-system-design" >}}) ·
[scaling to production]({{< relref "/building/scaling-to-production" >}}) ·
[serving models]({{< relref "/building/serving-models" >}}) ·
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
2. ✓ **[Lab: tự xây agent harness của riêng bạn]({{< relref "/hands-on/lab-agent-harness" >}})** — theo tám bước: một lời gọi API →
   một tool → vòng lặp → quản lý context → subagent → mỗi vai một model → permission và hook →
   MCP và Agent SDK, bước nào cũng đối chiếu với Claude Code.
3. ○ **Lab: eval harness + observability** cho lab 1–2, cộng với kiểm chứng thứ agent tạo ra.
4. ○ **Lab: agent trên một repo thật, Level 1 → 3** — repo sẵn sàng cho agent, spec và kiểm
   chứng, các giải pháp song song trong git worktree, điều phối, đo trước/sau.
5. ○ **Fine-tuning thực hành (LoRA)** — tinh chỉnh một model nhỏ cho giọng và schema.
6. ○ **App multimodal** — đầu vào vision, trích xuất tài liệu.
7. ○ **Ship to production** — deploy, kiểm soát chi phí, monitoring.

## Giai đoạn 4 — Create ○ (dự định, xa hơn)

- ○ AI product design — từ năng lực đến sản phẩm.
- ○ Kinh tế học của thử nghiệm — từ *"ta có đủ người và thời gian để xây cái này không?"* sang
  *"ta có thể chạy một thử nghiệm để biết nó có đáng xây không?"* Thử nghiệm rẻ vẫn cần giả
  thuyết, chỉ số thành công, điều kiện dừng và ngân sách **trước khi** giao việc, vì nhiều đầu
  ra hơn không có nghĩa là nhiều giá trị hơn.
- ○ Case study các sản phẩm AI thật.
- ○ Ghi chú chứng chỉ & bảng ôn tập.

## Đào sâu một chủ đề

Mỗi hàng là một mạch kiến thức xuyên các giai đoạn — cách đọc vault theo chiều dọc:

| Chủ đề | Giai đoạn 0 | Giai đoạn 1 | Giai đoạn 2 | Giai đoạn 3 ○ |
| ------ | ------ | ------ | ------ | ------ |
| **Prompts** | [Prompt engineering]({{< relref "prompt-engineering.md" >}}) · [Context engineering]({{< relref "context-engineering.md" >}}) | [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) | — | — |
| **Data & RAG** | [Embeddings]({{< relref "embeddings.md" >}}) · [RAG]({{< relref "rag.md" >}}) | [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) · [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) · [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) · [RAG evaluation]({{< relref "/deep-dives/rag-evaluation" >}}) | [Building RAG]({{< relref "/building/building-rag" >}}) · [Agentic RAG]({{< relref "/building/agentic-rag" >}}) | [Lab RAG chatbot ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) |
| **Agents** | [Tool calling]({{< relref "tool-function-calling.md" >}}) · [Agents]({{< relref "agents.md" >}}) · [Agentic AI]({{< relref "agentic-ai.md" >}}) · [MCP]({{< relref "mcp.md" >}}) | [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) · [Agent memory]({{< relref "/deep-dives/agent-memory" >}}) · [Multi-agent]({{< relref "/deep-dives/multi-agent" >}}) · [Self-improving]({{< relref "/deep-dives/self-improving-agents" >}}) · [Computer use]({{< relref "/deep-dives/computer-use" >}}) | [Agent harness]({{< relref "/building/agent-harness" >}}) · [Loop engineering]({{< relref "/building/loop-engineering" >}}) · [AI code structure]({{< relref "/building/ai-code-structure" >}}) | [Lab agent harness ✓]({{< relref "/hands-on/lab-agent-harness" >}}) · ○ Lab repo thật |
| **Operate** | [Guardrails]({{< relref "guardrails.md" >}}) · [AI security]({{< relref "ai-security.md" >}}) · [Đánh giá]({{< relref "model-evaluation.md" >}}) · [Observability]({{< relref "observability.md" >}}) · [Responsible AI]({{< relref "responsible-ai.md" >}}) | [Adaptation]({{< relref "/deep-dives/adaptation" >}}) · [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) · [RAG evaluation]({{< relref "/deep-dives/rag-evaluation" >}}) | [AI system design]({{< relref "/building/ai-system-design" >}}) · [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) | ○ Lab evals + ship |
| **Serving & inference** | [The AI API]({{< relref "the-ai-api.md" >}}) · [Cost & tokens]({{< relref "cost-and-tokens.md" >}}) · [Choosing a model]({{< relref "choosing-a-model.md" >}}) | [Adaptation]({{< relref "/deep-dives/adaptation" >}}) | [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Serving models]({{< relref "/building/serving-models" >}}) | ○ Lab ship to production |

## Agent engineering — bốn tầng

Mở Claude Code, viết prompt hay thêm một file skill không đồng nghĩa với hiểu agent. Kỹ năng này
xếp thành bốn tầng, và tầng nào cũng cần tầng bên dưới nó:

| Tầng | Câu hỏi nó trả lời | Trong vault |
| --- | --- | --- |
| **Cơ chế** | Agent hoạt động thế nào? Quản lý context, tool use, subagent, chọn model, vòng lặp, harness. | [Mạch Agents](#đào-sâu-một-chủ-đề) · [Lab 2 ✓]({{< relref "/hands-on/lab-agent-harness" >}}) |
| **Tay nghề** | Làm sao có kết quả *đáng tin*? Repo sẵn sàng cho agent, spec rõ ràng, và kiểm chứng đầu ra. | ○ Lab 3 · ○ Lab 4 |
| **Mở rộng** | Làm sao đi từ một agent lên nhiều agent? Level 1 một agent → Level 2 các subagent song song → Level 3 một orchestrator trong khi bạn giữ mục tiêu và quyết định. | [Multi-agent]({{< relref "/deep-dives/multi-agent" >}}) · [Fleet looping]({{< relref "/building/loop-engineering/fleet-looping" >}}) · ○ Lab 4 |
| **Phán đoán** | Cái gì đáng xây, và nó có hiệu quả không? Thử nghiệm có mục tiêu, và bằng chứng mà đồng nghiệp kiểm tra được. | ○ Giai đoạn 4 |

**Kiểm chứng** chạy xuyên qua cả bốn tầng. Agent nhanh hơn chỉ có ích khi bạn phân biệt được đầu
ra tốt với đầu ra tồi. Thang Level 1 → 3 đo **chiều rộng**: bao nhiêu agent, và ai điều phối
chúng. [The Four Levels of Loops]({{< relref "/building/loop-engineering/levels" >}}) đo
**chiều sâu**: thứ gì bọc quanh mỗi vòng lặp. Đó là hai trục khác nhau, và một hệ thống thật có
vị trí trên cả hai.
