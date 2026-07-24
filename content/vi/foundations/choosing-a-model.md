---
title: "Choosing a Model"
linkTitle: "Choosing a Model"
weight: 7
description: Năng lực vs chi phí vs độ trễ vs context — cách chọn đúng mô hình cho tác vụ.
---

Hiếm khi có một mô hình "tốt nhất" — chỉ có mô hình phù hợp cho *tác vụ này*. Chọn theo vài trục.

## Các trục quan trọng

| Trục | Câu hỏi |
| ------ | --------- |
| Năng lực | Có đủ thông minh cho bước khó nhất của tác vụ không? |
| Tốc độ / độ trễ | Cần phản hồi nhanh (chat) hay chờ được (batch)? |
| Chi phí | Giá mỗi token đầu vào và đầu ra — nhân với lượng dùng của bạn |
| Context window | Cần xử lý bao nhiêu văn bản cùng lúc? |
| Modalities | Chỉ văn bản, hay cả hình ảnh / âm thanh? |
| Hosting | API độc quyền vs mô hình open-weight bạn tự host |

## Các bậc năng lực

Đa số nhà cung cấp có một **thang bậc** — mô hình flagship lớn (mạnh nhất, chậm hơn, đắt hơn),
bậc trung (cân bằng), và mô hình nhỏ (nhanh, rẻ, hợp tác vụ đơn giản hoặc khối lượng lớn). Hãy
chọn bậc theo công việc thay vì mặc định lấy cái lớn nhất.

## Cách tiếp cận thực tế

1. **Prototype trên một mô hình mạnh** để chất lượng mô hình không phải nút thắt khi đang xây.
2. **Rồi tối ưu** — hạ xuống bậc nhỏ/rẻ hơn ở nơi chất lượng vẫn đạt; chỉ giữ mô hình lớn ở nơi
   thực sự cần.
3. **Đo lường đánh đổi** bằng một [bộ eval]({{< relref "/deep-dives/evaluation-in-practice" >}}),
   không dựa cảm tính.

## Open vs proprietary

- **Proprietary (API)** — dễ nhất, mạnh nhất, không cần hạ tầng; bạn gửi dữ liệu cho nhà cung cấp.
- **Open-weight (tự host)** — toàn quyền kiểm soát và chủ quyền dữ liệu; bạn tự vận hành và mở
  rộng hạ tầng.
