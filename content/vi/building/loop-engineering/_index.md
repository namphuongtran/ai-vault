---
title: "Loop Engineering"
linkTitle: "Loop Engineering"
weight: 6
type: docs
no_list: true
description: Thiết kế vòng lặp như một hệ thống — cấu tạo, các hình dạng, và khi nào mới cần tới SDK.
---

## Mục tiêu

Trả lời đúng chuỗi câu hỏi một builder sẽ hỏi về loop: loop engineering *là gì*, cấu tạo gồm
những phần nào, cần bao nhiêu loop, có bao nhiêu hình dạng, vì sao cần — và có bắt buộc code
trên SDK không, hay dùng được luôn
[Claude Code / Codex]({{< relref "ai-coding-assistants.md" >}}) có sẵn? Mỗi câu hỏi có một
trang riêng; đây là bản đồ.

## Là gì

**Loop engineering là thiết kế chính sự lặp lại, thay vì tự mình ngồi lặp.**
[Prompt engineering]({{< relref "prompt-engineering.md" >}}) định hình *một lần gọi
model*; [harness]({{< relref "/building/agent-harness" >}}) chạy *vòng lặp của một agent*;
loop engineering thiết kế **hệ thống các vòng lặp**: cái gì lặp, ai kiểm kết quả, thế nào là
"xong", và cái gì dừng nó lại. Gói trong một câu: bạn thôi làm người prompt agent — bạn xây
cái thứ đi prompt agent.

Điểm mấu chốt: looping là một **cách tổ chức hệ thống, không phải một model**. Nó không phải
tính năng bạn bật lên; nó là một mẫu mà gần như agent framework nào cũng chạy được, tùy cách
bạn nối các thành phần. Đó là lý do mô hình đang dịch từ `Prompt → Output` sang
`Goal → Loop → Evaluate → Improve → Repeat → Result` — và vì sao cả Anthropic lẫn OpenAI giờ
đều khuyến khích kỹ sư xây vòng lặp, không chỉ xây prompt.

## Bậc thang trưởng thành

Mỗi thế hệ sửa đúng cái hỏng của thế hệ trước — đây là hình dạng của cả ngành, và là bản đồ
cho các trang bên dưới:

```mermaid
flowchart LR
    subgraph P1["1 · Prompt engineering — human drives every iteration"]
      H[Human] --> A1[Agent] --> O1[Output]
      O1 -. feedback .-> H
    end
    subgraph P2["2 · Loop engineering — agent improves its own work"]
      G2[Goal] --> A2[Agent] --> R2[Research] --> D2[Draft] --> E2[Evaluate] --> I2[Improve]
      I2 --> A2
    end
    subgraph P3["3 · Orchestrated looping — teams iterate until done"]
      G3[Goal] --> Orc[Orchestrator - breaks down the goal]
      Orc --> RA[Research agent] & CA[Coding agent] & TA[Testing agent]
      RA & CA & TA --> EV[Evaluation agent - checks quality]
      EV -. next round .-> Orc
    end
    P1 ==> P2 ==> P3
```

| Năm | Loop | Bài học nó dạy |
| ------ | ------ | ------ |
| 2022 | **ReAct** — reason → act → observe, một model, một vòng | Lặp thắng trả lời một phát |
| 2023 | **AutoGPT** — vòng lặp theo đuổi mục tiêu | Nổi tiếng vì quay vô tận → loop cần **điều kiện dừng** |
| 2025 | **Ralph loop** — cùng một prompt chạy lại trên các anchor file cố định | Anchor bền giữ các run dài mạch lạc |
| Đầu 2026 | **Productised loop** — validator quyết định khi nào việc xong | "Xong" phải được *kiểm*, không phải tự tuyên bố |
| Giữa 2026 | **Orchestration** — supervisor lập lịch, điều phối các worker loop | Một vòng lặp không scale; đội các vòng lặp thì có |

## Năm trang

| Trang | Câu hỏi nó trả lời |
| ------ | ------ |
| [Cấu tạo của loop]({{< relref "anatomy.md" >}}) | Bên trong một loop production có gì |
| [Bốn cấp độ loop]({{< relref "levels.md" >}}) | Cần bao nhiêu loop, và mỗi loop mua về cái gì |
| [Open vs closed loop]({{< relref "open-vs-closed.md" >}}) | Chọn hình dạng nào, khi nào |
| [Fleet looping]({{< relref "fleet-looping.md" >}}) | Looping scale lên đội agent ra sao |
| [Tự xây một loop]({{< relref "building-a-loop.md" >}}) | Dùng tool có sẵn hay SDK riêng |

Hai cách nhìn này bổ sung cho nhau. [Cấp độ]({{< relref "levels.md" >}}) cho biết **cần bọc bao
nhiêu loop** quanh công việc; các trục bên dưới mô tả **từng loop riêng lẻ** bạn có — nên mọi
loop bạn gặp đều là một điểm trên ba trục độc lập:

| Trục | Lựa chọn | Chi tiết ở |
| ------ | ------ | ------ |
| **Kiến trúc** | Open (khám phá) vs closed (đo được) | [Open vs closed]({{< relref "open-vs-closed.md" >}}) |
| **Topology** | Một worker vs fleet điều phối | [Fleet looping]({{< relref "fleet-looping.md" >}}) |
| **Giám sát** | Human in / on / out of the loop | [Fleet looping]({{< relref "fleet-looping.md" >}}) |

## Vì sao cần

- **Gọi một phát chạm trần** — chất lượng đến từ lặp-và-kiểm, và làm tay thì *bạn* thành nút
  cổ chai.
- **Niềm tin đòi validator** — output agent không ai review thì không ship được; loop có
  người kiểm biến "nghe hợp lý" thành "đã kiểm chứng".
- **Kiểm soát chi phí đòi độ đóng** — khám phá mở là chi tiêu khó đoán; closed loop với
  ngưỡng làm chi phí và chất lượng *đo được theo từng run*, nên run sau cải thiện được run
  trước.

> Bạn thôi làm người prompt agent — bạn xây cái thứ đi prompt agent.

Khi orchestration *thực sự* xứng đáng, cấu trúc mà các loop phối hợp chạy trên đó là một graph
— xem [From prompts to graphs]({{< relref "/building/engineering-disciplines" >}}) để thấy
loop engineering nằm ở đâu trong dòng tiến hoá rộng hơn.

## Nguồn

- Osmani, *Loop Engineering* (2026) — [addyo.substack.com](https://addyo.substack.com/p/loop-engineering)
- Yao et al., *ReAct* (2022) — [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- [Anthropic — Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
