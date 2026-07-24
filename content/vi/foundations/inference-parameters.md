---
title: "Inference Parameters"
linkTitle: "Inference Parameters"
weight: 13
description: Các "núm" định hình đầu ra — temperature, top-p/top-k, max tokens, stop.
---

Khi gửi request, vài tham số định hình *cách* mô hình sinh nội dung. Đây là các núm hằng ngày
để kiểm soát đầu ra.

## Các núm cốt lõi

| Tham số | Kiểm soát | Dùng điển hình |
| --------- | ----------- | ---------------- |
| Temperature | Độ ngẫu nhiên | Thấp (~0) = tập trung/ổn định; cao = sáng tạo/đa dạng |
| Top-p (nucleus) | Lấy mẫu từ phần xác suất cao nhất | Thay cho temperature; thấp = an toàn hơn |
| Top-k | Lấy mẫu từ *k* ứng viên hàng đầu | Hiệu ứng tương tự; giới hạn số ứng viên |
| Max tokens | Giới hạn độ dài đầu ra | Tránh trả lời lê thê hoặc bị cắt |
| Stop sequences | Chuỗi kết thúc sinh nội dung | Dừng tại một dấu phân cách bạn định |

## Temperature trong thực tế

- **Thấp** cho trích xuất, phân loại, code, câu trả lời dữ kiện — bạn cần nhất quán.
- **Cao hơn** cho brainstorm, viết quảng cáo, đa dạng — bạn cần biên độ.
- Đừng chỉnh mạnh cả temperature *và* top-p cùng lúc; chọn một đòn bẩy.
- Ngay cả temperature 0, đầu ra không đảm bảo giống hệt mỗi lần.

## `max_tokens` là giới hạn cứng

Nếu mô hình chạm giới hạn giữa câu, câu trả lời bị cắt — hãy nâng giới hạn hoặc stream đầu ra
dài. Nhớ rằng đầu vào + đầu ra dùng chung [context window]({{< relref "/foundations/how-llms-work" >}}).

## Lưu ý về các mô hình mới

Một số mô hình mới đang chuyển khỏi các núm sampling thủ công sang điều khiển ở mức cao hơn —
ví dụ thiết lập **effort / reasoning**, hoặc reasoning tự động ("adaptive") — và có thể từ chối
`temperature`/`top_p`/`top_k`. Hãy kiểm tra API hiện tại của nhà cung cấp trước khi giả định
các núm cổ điển còn dùng được.
