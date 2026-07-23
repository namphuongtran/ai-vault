---
title: "Agent Patterns"
weight: 2
description: Vòng lặp ReAct, thiết kế tool, memory, multi-agent và reflection.
---

Tiếp nối [Agent ở phần Nền tảng]({{< relref "/foundations/agents" >}}). Các mẫu giúp agent
đáng tin cậy chứ không chỉ mạnh.

## Vòng lặp ReAct

Đa số agent chạy vòng lặp **Reason → Act → Observe**: mô hình suy luận bước tiếp theo, gọi tool
(act), đọc kết quả (observe), và lặp lại đến khi xong. Suy luận rõ ràng giữa các hành động giúp
chọn tool tốt hơn và làm trace dễ debug hơn.

## Thiết kế tool

Tool là API của agent tới thế giới — hãy thiết kế như một API tốt.

- **Ít tool, đặt tên rõ** tốt hơn nhiều tool chồng chéo.
- Mô tả rõ ràng và tham số có kiểu; mô hình chọn tool dựa trên các mô tả này.
- Trả về kết quả ngắn gọn, có cấu trúc; cắt nhiễu trước khi nó quay lại context.
- Ưu tiên tool **idempotent** và validate đầu vào (xem
  [Guardrail]({{< relref "/foundations/guardrails" >}})).

## Planning

- **Decomposition** — chia mục tiêu thành các tác vụ con có thứ tự trước khi hành động.
- **Plan-and-execute** — lập kế hoạch một lần rồi thực thi (rẻ hơn, dễ đoán) so với lập lại kế
  hoạch mỗi bước (thích ứng hơn).

## Memory

- **Ngắn hạn** — context làm việc cho tác vụ hiện tại (các bước gần đây, scratchpad).
- **Dài hạn** — dữ kiện lưu qua nhiều phiên, thường truy xuất bằng RAG.
- Tóm tắt hoặc loại bỏ bước cũ để context nằm trong giới hạn window.

## Multi-agent

Chia việc cho các agent chuyên biệt khi một context không chứa hết:

- **Orchestrator–worker** — một điều phối viên giao tác vụ con cho các worker tập trung.
- **Review/critique** — một agent tạo, một agent kiểm tra.

Càng nhiều agent thì chi phí phối hợp càng lớn — chỉ dùng khi một agent thực sự đuối.

## Reflection

Cho agent tự đánh giá đầu ra so với mục tiêu và thử lại nếu chưa đạt. Rẻ và hiệu quả với các tác
vụ có kết quả kiểm tra được (test pass, schema hợp lệ, có dẫn nguồn).

## Các lỗi thường gặp

- **Loop** — lặp lại cùng một hành động; thêm giới hạn số bước và phát hiện lặp.
- **Hallucinated tool/tham số** — ràng buộc bằng schema và validate lời gọi.
- **Phình context** — tóm tắt; đừng nối thêm mọi thứ mãi mãi.
- **Không có điều kiện dừng** — định nghĩa tiêu chí thành công rõ ràng.
