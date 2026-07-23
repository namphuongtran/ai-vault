---
title: "Adaptation: Fine-tuning vs RAG vs Prompting"
linkTitle: "Adaptation"
weight: 4
description: Cách chọn giữa prompting, RAG và fine-tuning — và cách kết hợp chúng.
---

Ba cách điều chỉnh một [foundation model]({{< relref "/foundations/foundation-models" >}}) cho
tác vụ của bạn, từ rẻ nhất đến tốn kém nhất.

## Ba đòn bẩy

| Đòn bẩy | Thay đổi gì | Phù hợp nhất cho |
| --------- | ------------- | ------------------ |
| Prompting | Chỉ đầu vào | Hành vi, định dạng, tác vụ đơn giản |
| RAG | Đầu vào + kiến thức bên ngoài | Dữ kiện mới, riêng tư, cần dẫn nguồn |
| Fine-tuning | Trọng số của mô hình | Style/định dạng nhất quán, kỹ năng hẹp |

## Khi nào dùng cái nào

- **Prompting** — bắt đầu từ đây. Nhanh, không cần hạ tầng. Đủ cho hầu hết nhu cầu về định dạng
  và hành vi.
- **RAG** — khi mô hình cần *kiến thức* mà nó không có: dữ liệu thay đổi, tài liệu riêng tư, hoặc
  câu trả lời cần dẫn nguồn. Xem
  [Advanced RAG]({{< relref "/deep-dives/advanced-rag" >}}).
- **Fine-tuning** — khi cần một *hành vi nhất quán* mà prompting không tạo ra ổn định (style,
  giọng điệu, hoặc schema đầu ra cố định), hoặc để dạy một kỹ năng hẹp. Nó **không** đáng tin để
  bổ sung kiến thức mới — hãy dùng RAG cho việc đó.

## Fine-tuning, tóm tắt

- **Full fine-tuning** cập nhật toàn bộ trọng số — tốn kém, hiếm khi cần.
- **PEFT / LoRA** chỉ huấn luyện các lớp adapter nhỏ — rẻ hơn nhiều, và adapter dễ lưu và hoán
  đổi. Đây là lựa chọn mặc định khi thực sự cần fine-tune.
- Cần một tập dữ liệu được gán nhãn, chọn lọc; chất lượng và độ bao phủ quan trọng hơn số lượng.

## Đánh đổi chi phí và dữ liệu

- Prompting: gần như không cần thiết lập; chi phí là token mỗi request.
- RAG: cần pipeline ingest + vector store; cập nhật dữ liệu mà không cần huấn luyện lại.
- Fine-tuning: chi phí huấn luyện ban đầu và một tập dữ liệu; phải huấn luyện lại để đổi hành vi.

## Kết hợp

Chúng không loại trừ nhau. Một kiến trúc production phổ biến là **fine-tune cho hình thức + RAG
cho kiến thức**: fine-tune để mô hình trả lời đúng giọng và schema của bạn, và dùng RAG để cấp
dữ kiện cập nhật, có căn cứ ngay lúc truy vấn.
