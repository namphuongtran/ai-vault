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
[bảng chủ đề](#đào-sâu-một-chủ-đề) bên dưới để đào sâu một mạch kiến thức. Để kiểm tra mình
thực sự *làm được* gì, dùng [bảng kiểm 25 kỹ năng](#bảng-kiểm-25-kỹ-năng).

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

## Bảng kiểm 25 kỹ năng

Các giai đoạn và mạch chủ đề sắp xếp những gì **đã viết**. Bảng này sắp xếp những gì bạn cần
**làm được**. Nó lấy một lộ trình ba cấp quen thuộc dành cho người xây agent (25 kỹ năng, từ
GenAI cơ bản đến deploy một agent) và gắn cho mỗi kỹ năng ba thứ: các trang giải thích nó, bước
lab nơi bạn tự xây nó, và một bài kiểm tra bạn tự chấm được.

Một kỹ năng chỉ tính là xong khi hàng của nó không còn ○ **và** bạn qua được bài kiểm tra ở cột
cuối. Đọc xong trang thì chưa đủ.

### Level 1 — GenAI và RAG cơ bản

| # | Kỹ năng | Hiểu | Làm | Làm được khi… |
| --- | --- | --- | --- | --- |
| 1 | **GenAI cơ bản** | [The AI landscape]({{< relref "/foundations/understand/ai-landscape" >}}) · [Generative AI]({{< relref "/foundations/understand/generative-ai" >}}) · [Limitations]({{< relref "/foundations/understand/limitations" >}}) | — | Bạn nói được cho đồng nghiệp generative AI giỏi việc gì, và kể được ba kiểu nó sai. |
| 2 | **LLM hoạt động ra sao** | [How LLMs work]({{< relref "/foundations/understand/how-llms-work" >}}) · [How models are trained]({{< relref "/foundations/understand/training-lifecycle" >}}) · [Under the hood]({{< relref "/foundations/understand/under-the-hood" >}}) | [Lab 2, bước 1 ✓]({{< relref "/hands-on/lab-agent-harness/step-1-stateless-call" >}}) | Bạn giải thích được token là gì, và vì sao model không nhớ gì giữa hai lời gọi API. |
| 3 | **Prompt engineering** | [Prompt engineering]({{< relref "/foundations/work-with-models/prompt-engineering" >}}) · [Context engineering]({{< relref "/foundations/work-with-models/context-engineering" >}}) · [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) | [Lab 1, bước 5 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) | Bạn viết được một prompt bám nguồn: câu trả lời trích dẫn context, và nói rõ khi context không có câu trả lời. |
| 4 | **Tham số model** | [Inference parameters]({{< relref "/foundations/work-with-models/inference-parameters" >}}) · [Reasoning models]({{< relref "/foundations/work-with-models/reasoning-models" >}}) · [Cost & tokens]({{< relref "/foundations/work-with-models/cost-and-tokens" >}}) | [Lab 2, bước 6 ✓]({{< relref "/hands-on/lab-agent-harness/step-6-model-per-role" >}}) | Bạn đoán trước được một lần chạy đổi thế nào khi chỉnh `max_tokens`, temperature hay effort, rồi kiểm lại bằng số đo. |
| 5 | **Chuẩn bị dữ liệu** | [Building RAG]({{< relref "/building/building-rag" >}}) · [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}) | [Lab 1, bước 2 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) (chỉ văn bản thuần) · ○ một bước với PDF và HTML thật: làm sạch, khử trùng lặp, so sánh cách chunk | Bạn biến được một thư mục PDF và HTML lộn xộn thành các chunk sạch kèm metadata, và chỉ ra cách chunk nào truy xuất tốt hơn. |
| 6 | **RAG cơ bản** | [Embeddings]({{< relref "/foundations/ground-in-data/embeddings" >}}) · [RAG]({{< relref "/foundations/ground-in-data/rag" >}}) · [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}) | [Lab 1, bước 3–5 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) | Pipeline của bạn trả lời từ tài liệu của chính bạn, có trích dẫn, và từ chối khi tài liệu không có câu trả lời. |
| 7 | **Vector database** | [Vector databases]({{< relref "/deep-dives/vector-databases" >}}) | [Lab 1, bước 1 và 4 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) | Bạn lưu và tìm được embedding, nói được ANN index đánh đổi điều gì, và khi nào pgvector không còn đủ. |
| 8 | **LLM framework** | ○ LangChain và LlamaIndex trong [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) | ○ bước 5 của Lab 1 dựng lại bằng một framework | Bạn dựng lại được pipeline RAG bằng một framework và chỉ ra mỗi lớp trừu tượng thay cho đoạn code nào của mình. |
| 9 | **Tool calling** | [Tool & function calling]({{< relref "/foundations/make-it-act/tool-function-calling" >}}) · [Structured outputs]({{< relref "/foundations/work-with-models/structured-outputs" >}}) | [Lab 2, bước 2 ✓]({{< relref "/hands-on/lab-agent-harness/step-2-one-tool" >}}) | Bạn tự tay chạy được một vòng `tool_use` → `tool_result`, và nói được ai mới là bên thực thi tool. |

### Level 2 — Thiết yếu về AI agent

| # | Kỹ năng | Hiểu | Làm | Làm được khi… |
| --- | --- | --- | --- | --- |
| 10 | **Agent là gì** | [Agents]({{< relref "/foundations/make-it-act/agents" >}}) · [Agentic AI]({{< relref "/foundations/make-it-act/agentic-ai" >}}) · [AI coding assistants]({{< relref "/foundations/make-it-act/ai-coding-assistants" >}}) | [Lab 2, bước 3 ✓]({{< relref "/hands-on/lab-agent-harness/step-3-the-loop" >}}) | Bạn phân biệt được workflow cố định với agent, và nêu được một việc mà agent là lựa chọn sai. |
| 11 | **Agent framework** | [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) · [From prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) · ○ bảng so sánh LangGraph, CrewAI, Agno và SDK của các hãng | [Lab 2, bước 8 ✓]({{< relref "/hands-on/lab-agent-harness/step-8-mcp-and-agent-sdk" >}}) (Claude Agent SDK) · ○ cùng agent đó viết bằng LangGraph và một framework nữa | Bạn chuyển được `agent.py` sang một framework và liệt kê được nó cho bạn gì, che mất gì. |
| 12 | **Agent đầu tiên** | [The agent harness]({{< relref "/building/agent-harness" >}}) | [Lab 2, bước 1–3 ✓]({{< relref "/hands-on/lab-agent-harness" >}}) | Vòng lặp do bạn viết tự sửa được một test đang fail trong project sandbox mà không cần bạn giúp. |
| 13 | **Agent flow** | [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) · [Loop engineering]({{< relref "/building/loop-engineering" >}}) · [From prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) | [Lab 1, bước 7 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) · [Lab 2, bước 3 ✓]({{< relref "/hands-on/lab-agent-harness/step-3-the-loop" >}}) | Bạn vẽ được chỗ agent suy luận, hành động, kiểm tra và dừng, và chọn được giữa pipeline và loop cho một việc. |
| 14 | **Agent memory** | [Agent memory]({{< relref "/deep-dives/agent-memory" >}}) | [Lab 2, bước 4 ✓]({{< relref "/hands-on/lab-agent-harness/step-4-context-management" >}}) · [bước 7 ✓]({{< relref "/hands-on/lab-agent-harness/step-7-harness-controls" >}}) (context, `AGENT.md`, session) · ○ memory dài hạn do agent tự ghi và tự truy xuất | Agent của bạn nhớ lại được một điều từ phiên làm việc tuần trước, và bạn gọi tên được loại memory đã giữ nó. |
| 15 | **Đánh giá agent** | [Model evaluation]({{< relref "/foundations/operate-and-govern/model-evaluation" >}}) · [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}) · ○ đánh giá agent: trajectory, tool call, tỉ lệ hoàn thành task | ○ Lab 3 | Bạn có một bộ task kèm grader, và nêu được tỉ lệ pass, chi phí và độ trễ của agent trước và sau một thay đổi. |
| 16 | **Suy luận nhiều bước** | [Reasoning models]({{< relref "/foundations/work-with-models/reasoning-models" >}}) · [Prompt patterns]({{< relref "/deep-dives/prompt-patterns" >}}) | [Lab 2, bước 6 ✓]({{< relref "/hands-on/lab-agent-harness/step-6-model-per-role" >}}) | Bạn chứng minh được bằng benchmark khi nào tăng reasoning effort là đáng tiền, và khi nào không. |
| 17 | **Hệ multi-agent** | [Multi-agent]({{< relref "/deep-dives/multi-agent" >}}) · [Fleet looping]({{< relref "/building/loop-engineering/fleet-looping" >}}) | [Lab 2, bước 5 ✓]({{< relref "/hands-on/lab-agent-harness/step-5-subagents" >}}) · ○ Lab 4 | Bạn chia được một việc cho orchestrator và các subagent, và chỉ ra nó có thắng một agent đơn hay không. |
| 18 | **Agentic RAG** | [Agentic RAG]({{< relref "/building/agentic-rag" >}}) · [Self-correcting RAG]({{< relref "/deep-dives/types-of-rag/self-correcting" >}}) | [Lab 1, bước 7 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) | Một câu hỏi multi-hop cho thấy hai lượt tìm khác nhau trong trace, còn "hello" thì không có lượt nào. |
| 19 | **Lập kế hoạch hành động** | [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) · [Cấu tạo của loop]({{< relref "/building/loop-engineering/anatomy" >}}) | [Lab 2, bước 3 ✓]({{< relref "/hands-on/lab-agent-harness/step-3-the-loop" >}}) (lỗi trả về như result) · ○ một kế hoạch do agent tự viết và tự sửa | Agent của bạn viết kế hoạch, gặp một bước thất bại, sửa kế hoạch rồi làm xong, và trace cho thấy từng lần sửa. |
| 20 | **An toàn và guardrail** | [Guardrails]({{< relref "/foundations/operate-and-govern/guardrails" >}}) · [AI security]({{< relref "/foundations/operate-and-govern/ai-security" >}}) · [Responsible AI]({{< relref "/foundations/operate-and-govern/responsible-ai" >}}) | [Lab 2, bước 7 ✓]({{< relref "/hands-on/lab-agent-harness/step-7-harness-controls" >}}) (permission, hook) · ○ guardrail cho input và output, và một bài test prompt injection | Bạn cho thấy được một chỉ dẫn cài trong tool result bị chặn bằng code chứ không phải bằng prompt. |

### Level 3 — Kỹ năng agent nâng cao

| # | Kỹ năng | Hiểu | Làm | Làm được khi… |
| --- | --- | --- | --- | --- |
| 21 | **Tích hợp thực tế** | [MCP]({{< relref "/foundations/make-it-act/mcp" >}}) · [Tooling & frameworks]({{< relref "/building/tooling-and-frameworks" >}}) | [Lab 2, bước 8 ✓]({{< relref "/hands-on/lab-agent-harness/step-8-mcp-and-agent-sdk" >}}) (server cục bộ) · ○ một server remote thật như Slack, Notion hay Gmail, qua OAuth | Agent của bạn đọc và ghi được trong một workspace thật qua MCP, với quyền truy cập thu hẹp theo đúng việc. |
| 22 | **Vòng lặp tự hành** | [Loop engineering]({{< relref "/building/loop-engineering" >}}) · [Self-improving agents]({{< relref "/deep-dives/self-improving-agents" >}}) | ○ một agent chạy theo lịch mà không ai ngồi canh · ○ Lab 4 | Agent chạy theo trigger, tự dừng theo điều kiện của nó, và để lại log mà bạn tin được. |
| 23 | **Bộ tool tự viết** | [Tool & function calling]({{< relref "/foundations/make-it-act/tool-function-calling" >}}) · [Agent patterns]({{< relref "/deep-dives/agent-patterns" >}}) | [Lab 2, bước 2 ✓]({{< relref "/hands-on/lab-agent-harness/step-2-one-tool" >}}) · [bước 3 ✓]({{< relref "/hands-on/lab-agent-harness/step-3-the-loop" >}}) · [bước 8 ✓]({{< relref "/hands-on/lab-agent-harness/step-8-mcp-and-agent-sdk" >}}) (MCP server của riêng bạn) · ○ một tool bọc một HTTP API thật | Bạn bọc được một API thành tool, có auth, phân trang và lỗi trả về như result, và model dùng đúng chỉ nhờ phần mô tả. |
| 24 | **Tối ưu hiệu năng** | [Cost & tokens]({{< relref "/foundations/work-with-models/cost-and-tokens" >}}) · [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Routing & fallback]({{< relref "/building/serving-models/routing-and-fallback" >}}) | [Lab 1, bước 6 ✓]({{< relref "/hands-on/lab-rag-chatbot" >}}) · [Lab 2, bước 4 ✓]({{< relref "/hands-on/lab-agent-harness/step-4-context-management" >}}) · [bước 6 ✓]({{< relref "/hands-on/lab-agent-harness/step-6-model-per-role" >}}) · ○ Lab 3, để có tỉ lệ pass | Bạn giảm được chi phí hoặc độ trễ của một lần chạy một lượng đo được mà không làm tụt tỉ lệ pass. |
| 25 | **Deploy lên production** | [AI system design]({{< relref "/building/ai-system-design" >}}) · [Scaling to production]({{< relref "/building/scaling-to-production" >}}) · [Observability]({{< relref "/foundations/operate-and-govern/observability" >}}) · ○ deploy một agent: session, state, sandbox, giới hạn | ○ Lab 7 | Một người khác dùng agent của bạn qua một URL, có session riêng, có trần chi tiêu, và có trace để bạn đọc. |

### Các ô ○ thêm gì vào kế hoạch

Các ô ○ là phần việc còn nợ. Theo thứ tự dự định làm:

1. **Lab 3 trở thành lab đánh giá agent** (kỹ năng 15 và 24). Làm trước tiên, để mọi bước sau
   đều có một con số để cải thiện.
2. **Một lab mới: agent làm việc thật** (kỹ năng 14, 19, 20, 21, 22 và 23). Lab này tiếp nối
   `agent.py` của Lab 2 qua sáu bước: tool gọi một API thật → kế hoạch tự sửa được → memory dài
   hạn → một MCP server thật → guardrail và bài test injection → chạy theo lịch.
3. **Một lượt framework** (kỹ năng 8 và 11). Cùng pipeline RAG và cùng agent đó, dựng lại bằng
   framework rồi so với bản tự viết.
4. **Một bước chuẩn bị dữ liệu trong Lab 1** (kỹ năng 5).
5. **Lab 7 mở ra thành các bước deploy** (kỹ năng 25).
