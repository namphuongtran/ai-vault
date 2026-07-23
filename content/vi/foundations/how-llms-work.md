---
title: "How LLMs Work"
linkTitle: "How LLMs Work"
weight: 4
description: Token, dự đoán token kế tiếp và context window — cơ chế bạn xây dựng trên đó.
---

Bạn không cần toán, nhưng vài cơ chế giải thích phần lớn những gì bạn sẽ gặp khi làm builder.

## Token

Mô hình không đọc ký tự hay từ — nó đọc **token**, các mẩu văn bản (khoảng ¾ một từ tiếng
Anh). "Tokenization" là bước chia văn bản thành token. Mọi thứ được đếm và tính phí theo token:
cả đầu vào **và** đầu ra của mô hình.

## Dự đoán token kế tiếp

LLM làm đúng một việc: cho văn bản hiện có, dự đoán **token kế tiếp**, nối vào, rồi lặp lại.
Chỉ vậy thôi. Đây là lý do:

- Đầu ra mang tính **xác suất** — cùng một prompt có thể cho câu trả lời khác nhau.
- Mô hình có thể trôi chảy nhưng vẫn sai (nó dự đoán văn bản hợp lý, không phải sự thật đã kiểm chứng).

## Context window

**Context window** là số token tối đa mô hình có thể xét cùng lúc — và **đầu vào + đầu ra dùng
chung ngân sách này**. Prompt dài để lại ít chỗ cho câu trả lời. Khi hội thoại vượt quá window,
bạn phải cắt bớt, tóm tắt hoặc truy xuất (xem
[Context engineering]({{< relref "/foundations/context-engineering" >}})).

## Knowledge cutoff

Mô hình chỉ biết những gì thấy trong quá trình huấn luyện, đến một **mốc thời gian cutoff**. Nó
không biết dữ liệu của bạn hay sự kiện gần đây — và đó chính là lý do có
[RAG]({{< relref "/foundations/rag" >}}) và tool.

## Vì sao điều này quan trọng với bạn

- Bạn trả phí theo token → prompt gọn và caching giúp tiết kiệm.
- Context là hữu hạn → quản lý những gì bạn đưa vào.
- Đầu ra mang tính xác suất → hãy validate và dùng [evaluation]({{< relref "/foundations/model-evaluation" >}}).
