---
title: "Foundation Model"
weight: 3
description: Mô hình lớn, đa dụng, được huấn luyện trước trên dữ liệu rộng và điều chỉnh cho nhiều tác vụ.
---

## Là gì

**Foundation model** là mô hình lớn được huấn luyện trước (pre-train) trên nguồn dữ liệu rộng,
sau đó được điều chỉnh cho nhiều tác vụ khác nhau. Thay vì huấn luyện một mô hình riêng cho mỗi
tác vụ, ta bắt đầu từ một mô hình đa dụng và chuyên biệt hoá nó.

## Điểm chính

- **Pre-training** học các mẫu tổng quát từ dữ liệu lớn; **fine-tuning** và **prompting** giúp
  chuyên biệt hoá cho từng tác vụ.
- **Parameters** — các trọng số đã học; càng nhiều tham số thường càng nhiều "dung lượng".
- **Context window** — lượng văn bản mô hình có thể xử lý cùng lúc (đầu vào + đầu ra).
- **Modalities** — văn bản, hình ảnh, âm thanh, hoặc kết hợp (đa phương thức).
- Các cách điều chỉnh, từ rẻ đến tốn kém: **prompting → RAG → fine-tuning**.

> Large language model (LLM) là một foundation model chuyên cho văn bản.

## Ví dụ — một model, nhiều tác vụ

*Cùng một* foundation model có thể tóm tắt email, viết SQL, dịch tiếng Pháp, và trả lời một câu
hỏi hỗ trợ — không cần huấn luyện riêng cho từng tác vụ. Bạn chỉ đổi prompt.

## Điểm mạnh & hạn chế

- **Điểm mạnh** — một model đa dụng cho nhiều tác vụ; điều chỉnh rẻ theo
  prompting → RAG → fine-tuning.
- **Hạn chế** — kiến thức đóng băng ở mốc cutoff; có thể hallucinate; năng lực, chi phí và độ
  trễ đều tăng theo kích thước; hành vi khó đoán hết.

## Nguồn

- Bommasani et al., *On the Opportunities and Risks of Foundation Models* (2021) — [arXiv:2108.07258](https://arxiv.org/abs/2108.07258)
- [Anthropic — Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
