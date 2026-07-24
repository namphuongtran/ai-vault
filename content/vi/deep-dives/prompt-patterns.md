---
title: "Prompt Patterns"
weight: 1
description: Kỹ thuật suy luận, structured output, phân rã và tối ưu prompt.
---

Tiếp nối [Prompt Engineering ở phần Nền tảng]({{< relref "/foundations/prompt-engineering" >}}).
Các mẫu cho những tác vụ khó hơn, khi một prompt đơn lẻ là chưa đủ.

## Kỹ thuật suy luận

- **Chain-of-thought** — yêu cầu suy luận từng bước trước khi trả lời; hữu ích với bài toán
  nhiều bước.
- **Self-consistency** — lấy mẫu nhiều đường suy luận rồi chọn đáp án theo đa số; đánh đổi chi
  phí lấy độ tin cậy.
- **Least-to-most** — giải các bài con dễ trước, rồi dùng chúng để giải bài khó hơn.

## Structured output

Khi đầu ra được đưa vào một hệ thống khác, hãy ràng buộc hình dạng của nó:

- Yêu cầu **JSON** theo schema rõ ràng; validate và thử lại khi lỗi.
- Ưu tiên **function/tool calling** hoặc chế độ structured-output có sẵn thay vì parse văn bản tự do.
- Giữ schema nhỏ và phẳng; mô tả từng trường.

## Phân rã và chaining

Chia một tác vụ lớn thành **chuỗi** prompt nhỏ, mỗi cái một nhiệm vụ và một đầu ra kiểm tra được.
Dễ test, debug và thay thế hơn. Ưu tiên chaining hơn một mega-prompt khi các bước có mục tiêu
khác nhau (extract → transform → format).

Một chuỗi cụ thể — "biến thread email support này thành ticket":

1. **Extract** — rút khách hàng, sản phẩm, nội dung khiếu nại từ thread → JSON.
2. **Transform** — phân loại mức nghiêm trọng và định tuyến về team, chỉ từ JSON đó.
3. **Format** — dựng ticket theo template của tracker.

Mỗi bước test riêng được; khi định tuyến sai, bạn debug bước 2, không phải một prompt khổng lồ.

## Chọn few-shot

Ví dụ định hướng định dạng và phong cách — nhưng *chọn ví dụ nào* mới quan trọng:

- Chọn ví dụ gần với đầu vào hiện tại (truy xuất động để đa dạng).
- Bao phủ edge case và đúng định dạng đầu ra.
- Quá nhiều ví dụ làm tốn context và có thể overfit theo cách diễn đạt của chúng.

## Tối ưu

- Lặp dựa trên một **bộ eval** nhỏ, không dựa cảm tính (xem
  [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}})).
- Đổi một thứ mỗi lần; giữ changelog cho prompt.
- Dùng **prompt caching** cho phần prefix ổn định (chỉ dẫn, khối few-shot) để giảm chi phí và
  độ trễ.

## Anti-pattern

- Nhồi nhiều nhiệm vụ không liên quan vào một prompt.
- Tiêu chí thành công mơ hồ ("làm cho tốt").
- Dựa vào ví dụ để chữa một tác vụ mà chỉ dẫn chưa bao giờ nêu rõ.

## Nguồn

- Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in LLMs* (2022) — [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Wang et al., *Self-Consistency Improves Chain of Thought Reasoning* (2022) — [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Zhou et al., *Least-to-Most Prompting* (2022) — [arXiv:2205.10625](https://arxiv.org/abs/2205.10625)
