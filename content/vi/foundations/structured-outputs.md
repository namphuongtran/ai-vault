---
title: "Structured Outputs"
linkTitle: "Structured Outputs"
weight: 14
description: Bắt model trả về JSON đúng schema để code của bạn dựa vào được.
---

Tiếp nối [The AI API]({{< relref "/foundations/the-ai-api" >}}). Để *build* với model, bạn
thường cần đầu ra code parse được — không phải văn xuôi. **Structured outputs** ràng buộc câu
trả lời của model theo một **schema** (thường là JSON).

## Ý tưởng

Bạn đưa schema; model trả về dữ liệu khớp schema; bạn validate và dùng trực tiếp.

```mermaid
flowchart LR
    P[Prompt + schema] --> M[Model]
    M --> J[JSON matching the schema]
    J --> V{Valid?}
    V -->|yes| Use[Use directly in code]
    V -->|no| M
```

## Ví dụ

Schema (thứ bạn yêu cầu):

```json
{ "type": "object",
  "properties": {
    "sentiment": { "type": "string", "enum": ["positive", "neutral", "negative"] },
    "score": { "type": "number" }
  },
  "required": ["sentiment", "score"] }
```

Đầu ra (thứ bạn dựa vào được):

```json
{ "sentiment": "positive", "score": 0.82 }
```

Không parse chuỗi, không "thỉnh thoảng nó thêm một câu trước JSON".

## Cách thực hiện

- **JSON / schema mode** — API ràng buộc decoding thành JSON hợp lệ theo schema của bạn.
- **Tool arguments** — tham số của một [tool call]({{< relref "/foundations/tool-function-calling" >}})
  cũng là structured output; cùng cơ chế.
- **Validate + retry** — luôn validate; nếu lệch, hỏi lại.

## Vì sao quan trọng

Structured outputs là thứ biến một LLM thành **một thành phần đáng tin** trong pipeline — phân
loại, trích xuất, định tuyến, hay bất kỳ bước nào mà kết quả đưa vào code khác.
