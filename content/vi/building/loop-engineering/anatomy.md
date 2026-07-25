---
title: "Cấu tạo của loop"
linkTitle: "Cấu tạo"
weight: 1
description: Sáu thành phần của một loop production — và vì sao worker là phần ít thú vị nhất.
---

*Bên trong một loop production có gì.*

## Là gì

Một loop production có sáu phần. Worker — agent làm task — là phần *ít* thú vị nhất; chính các
phần bao quanh nó mới biến một demo thành thứ bạn tin để chạy không người canh.

```mermaid
flowchart LR
    D[Discovery - finds work] --> B[Backlog and decomposition]
    B --> W[Worker loop - does the task]
    W --> V[Validator - checks the result]
    V -->|pass| Done[Merge and record]
    V -->|fail, with feedback| W
    S[Stop conditions - rounds, tokens, time] -.-> W
    M[Memory and anchors - skills, project rules] -.-> W
```

## Sáu thành phần

- **Discovery / automations** — tự tìm việc không cần con người kích hoạt: lịch chạy,
  webhook, scanner. Đây là cái cho loop chạy *không người canh*.
- **Decomposition** — orchestrator chia mục tiêu thành các task worker nhận được. Xem
  [fleet looping]({{< relref "fleet-looping.md" >}}) khi việc này thành nhiều tầng.
- **Worker** — một agent với [tools]({{< relref "tool-function-calling.md" >}}) và
  [MCP connector]({{< relref "mcp.md" >}}); worker chạy song song thì cần **git
  worktree** để không ghi đè lên nhau.
- **Validator** — một phán xét thứ hai ([LLM-as-judge]({{< relref "/deep-dives/evaluation-in-practice" >}}),
  bộ test, hoặc cả hai) quyết định đạt/không đạt — không bao giờ để worker tự chấm mình.
- **Điều kiện dừng** — giới hạn vòng, ngân sách token, phát hiện lặp: bài học AutoGPT, thừa
  kế từ [harness]({{< relref "/building/agent-harness" >}}).
- **Memory & anchors** — [skills]({{< relref "/building/agent-harness" >}}), luật dự án, và
  [agent memory]({{< relref "/deep-dives/agent-memory" >}}) để mỗi vòng xây trên vòng trước
  thay vì khám phá lại.

## Ví dụ

Một loop cập nhật dependency hằng đêm: **discovery** là cron trigger; **decomposition** chia
"cập nhật mọi package" thành một task mỗi package; **worker** nâng version và chạy build;
**validator** là bộ test; **điều kiện dừng** chặn ở ba lần thử sửa mỗi package; **anchors** là
ghi chú nâng cấp của dự án để nó không học lại các lỗi đã biết. Chỉ worker là "agent" — năm
phần còn lại mới là cái làm cho việc để nó chạy qua đêm trở nên an toàn.

## Liên quan

- [Open vs closed loop]({{< relref "open-vs-closed.md" >}}) — validator chính là cái làm loop thành *closed*.
- [The agent harness]({{< relref "/building/agent-harness" >}}) — nơi điều kiện dừng và memory đến từ.

## Nguồn

- [Anthropic — Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) — vòng lặp theo đuổi mục tiêu, và các bài học của nó
