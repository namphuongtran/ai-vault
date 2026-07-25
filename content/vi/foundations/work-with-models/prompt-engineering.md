---
aliases: ["/foundations/prompt-engineering/"]
title: "Prompt Engineering"
weight: 11
description: Cách trực tiếp nhất để kiểm soát đầu ra của foundation model.
---

## Là gì

**Prompt engineering** là nhóm kiến thức tương đối dễ gặp vì đây là cách trực tiếp nhất để kiểm
soát đầu ra của foundation model — không cần huấn luyện lại.

## Cấu trúc một prompt tốt

| Thành phần | Vai trò |
| ------------ | --------- |
| Role | Xác định vai trò của mô hình |
| Task | Mô tả nhiệm vụ cần thực hiện |
| Context | Cung cấp thông tin nền cần thiết |
| Constraints | Nêu rõ các giới hạn hoặc điều kiện |
| Response format | Chỉ định định dạng đầu ra |
| Response style | Xác định phong cách trả lời |
| Success criteria | Mô tả thế nào là câu trả lời đạt yêu cầu |
| Examples | Cung cấp ví dụ khi cần thiết |

**Chưa tốt:** "Hãy tóm tắt tài liệu này."

**Tốt hơn:** "Bạn là chuyên viên phân tích tài liệu. Hãy tóm tắt nội dung dưới đây trong tối đa
năm ý chính. Mỗi ý không quá hai câu. Chỉ sử dụng thông tin có trong tài liệu và không tự bổ
sung dữ kiện."

Prompt thứ hai rõ ràng hơn vì có vai trò, nhiệm vụ, giới hạn, định dạng và tiêu chí đầu ra.

## Khi nào dùng kỹ thuật nào

| Tình huống | Dùng |
| ------ | ------ |
| Tác vụ phổ biến, ai cũng hiểu | **Zero-shot** — hỏi thẳng; model hiện đại thường làm được |
| Định dạng hoặc phong cách output cứ trôi | **Few-shot** — 2–5 ví dụ dạy được khuôn mẫu nhanh hơn cả đoạn văn mô tả luật |
| Logic nhiều bước bị sai | **Chain-of-thought** — yêu cầu suy luận từng bước (hoặc dùng [reasoning model]({{< relref "reasoning-models.md" >}})) |
| Tác vụ quá lớn cho một prompt | **Prompt chaining** — tách thành các prompt nối tiếp, kiểm tra giữa các bước |
| Cùng một khuôn prompt chạy trên nhiều input | **Prompt template** — một cấu trúc, các biến đầu vào |
| Mỗi lần gọi lặp lại một prefix dài | **Prompt caching** — đòn bẩy chi phí; xem [Cost & tokens]({{< relref "cost-and-tokens.md" >}}) |

Quy luật đằng sau bảng: ví dụ thắng chỉ dẫn khi cần *đúng dạng*; suy luận thắng cả hai khi cần
*đúng logic*; và phân rã thắng prompt to hơn.

## Điểm mạnh & hạn chế

- **Điểm mạnh** — đòn bẩy rẻ nhất, nhanh nhất; không cần hạ tầng; lặp lại tức thì.
- **Hạn chế** — không thêm được kiến thức model thiếu (dùng RAG); nhạy với cách diễn đạt; chạm trần
  ở tác vụ khó hoặc cần nhất quán cao (khi đó cân nhắc fine-tuning).

## Nguồn

- [Anthropic — Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [OpenAI — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
