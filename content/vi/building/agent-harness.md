---
title: "The Agent Harness"
linkTitle: "The Agent Harness"
weight: 4
description: Phần scaffolding chạy một agent — vòng lặp, quản lý context, thực thi tool, memory và guardrail.
---

Tiếp nối [Agentic AI]({{< relref "/foundations/agentic-ai" >}}). Model là động cơ; **harness** là
mọi thứ quanh nó biến một lời gọi model đơn lẻ thành một agent hoạt động. Trang này nói cách xây một cái.

## Harness sở hữu những gì

```mermaid
flowchart LR
    subgraph Harness
      Loop[Agent loop]
      CtxM[Context manager]
      ToolR[Tool executor]
      Mem[Memory]
      Guard[Guardrails / permissions]
    end
    Harness --> Model[Model API]
    Harness --> Tools[Tools]
```

## Vòng lặp

Ở lõi, harness chạy một vòng lặp đến khi xong việc:

```mermaid
flowchart TD
    In[User goal] --> Ctx[Assemble context]
    Ctx --> M[Call model]
    M --> Dec{Tool call?}
    Dec -->|no| Out[Return answer]
    Dec -->|yes| G[Check guardrails / permissions]
    G --> Ex[Execute tool]
    Ex --> Up[Append result, update memory]
    Up --> Ctx
```

Mỗi lượt: lắp ráp context, gọi [model]({{< relref "/foundations/the-ai-api" >}}), và nếu nó trả
về một [tool call]({{< relref "/foundations/tool-function-calling" >}}), thực thi tool, nối kết
quả, và lặp — đến khi model trả lời hoặc chạm điều kiện dừng.

## Những phần khó

- **Quản lý context** — [window]({{< relref "/foundations/context-engineering" >}}) là hữu hạn;
  khi vòng lặp dài ra, bạn phải tóm tắt hoặc cắt bớt kết quả tool cũ, nếu không run sẽ hỏng.
- **Thực thi tool** — validate tham số, chặn hành động rủi ro sau phê duyệt, chạy gọi song song,
  và trả lỗi dưới dạng kết quả để model phục hồi được.
- **Memory** — mang dữ kiện qua các lượt (và các phiên) mà không nhồi mọi thứ vào window.
- **Điều kiện dừng** — giới hạn số bước, phát hiện lặp, và ngân sách token/thời gian, để một
  agent bị kẹt kết thúc êm thay vì quay vòng.
- **Guardrail** — áp [kiểm tra đầu vào/đầu ra]({{< relref "/foundations/guardrails" >}}) và
  [security]({{< relref "/foundations/ai-security" >}}) ở *mỗi* lượt, không chỉ lượt đầu.

## Build vs buy

Bạn hiếm khi tự viết tất cả:

- **Tự viết vòng lặp** — toàn quyền; tốn công nhất.
- **Dùng framework / SDK** — vòng lặp, xử lý tool và quản lý context có sẵn.
- **Dịch vụ managed** — nhà cung cấp host vòng lặp và sandbox tool cho bạn.

Chọn cái nào là chủ đề [Tooling & frameworks]({{< relref "/building" >}}), sắp tới.
