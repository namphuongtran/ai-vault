---
title: "Guardrail"
weight: 24
description: Cơ chế an toàn và kiểm soát quanh đầu vào và đầu ra của mô hình.
---

## Là gì

**Guardrail** là các cơ chế kiểm soát đặt quanh mô hình để giữ hành vi an toàn, đúng phạm vi và
tuân thủ. Chúng nằm *trước* mô hình (với đầu vào) và *sau* mô hình (với đầu ra), và hoạt động độc
lập với cách mô hình được huấn luyện.

## Áp dụng ở đâu

- **Guardrail đầu vào** — chặn prompt injection, yêu cầu lạc đề, hoặc nội dung không được phép;
  che (redact) PII trước khi đưa vào mô hình.
- **Guardrail đầu ra** — lọc phản hồi độc hại hoặc không an toàn, ép định dạng, kiểm tra câu trả
  lời có bám sát context được cung cấp hay không (xem [Faithfulness]({{< relref "model-evaluation" >}})).

## Các loại phổ biến

- **Content moderation** — phát hiện nội dung độc hại, thù ghét, không an toàn.
- **Topic restriction** — giữ mô hình trong phạm vi được phép.
- **PII detection / redaction** — bảo vệ dữ liệu cá nhân và nhạy cảm.
- **Format / schema enforcement** — đảm bảo đầu ra hợp lệ, có cấu trúc.
- **Grounding checks** — loại bỏ câu trả lời không được hỗ trợ bởi context truy xuất.

## Vì sao quan trọng

Guardrail giảm rủi ro (đầu ra gây hại, rò rỉ dữ liệu, dùng sai phạm vi) mà không cần huấn luyện
lại mô hình. Chúng đi đôi tự nhiên với **agent**, nơi quyền tự chủ càng cao thì càng cần kiểm soát.
