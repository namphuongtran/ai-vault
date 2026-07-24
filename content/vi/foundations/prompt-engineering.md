---
title: "Prompt Engineering"
weight: 16
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

## Các kỹ thuật cần phân biệt

- **Zero-shot** — yêu cầu mô hình thực hiện nhiệm vụ mà không cung cấp ví dụ.
- **One-shot** — cung cấp một ví dụ trước khi yêu cầu mô hình thực hiện.
- **Few-shot** — cung cấp một số ví dụ để mô hình nhận biết cách trả lời.
- **Prompt chaining** — chia một nhiệm vụ lớn thành nhiều prompt nhỏ nối tiếp nhau.
- **Prompt template** — tạo cấu trúc prompt tái sử dụng được bằng cách thay đổi các biến đầu vào.
- **Chain-of-thought** — hướng mô hình xử lý bài toán theo từng bước suy luận.
- **Prompt caching** — tái sử dụng phần prompt lặp lại để giảm độ trễ và chi phí xử lý đầu vào
  (trong những trường hợp được hỗ trợ).
