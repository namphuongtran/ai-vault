---
title: "How Models Are Trained"
linkTitle: "How Models Are Trained"
weight: 5
description: Góc nhìn mức nhận biết về pre-training, fine-tuning và alignment — và vì sao nó quan trọng với builder.
---

Bạn sẽ không huấn luyện một foundation model, nhưng biết *cách* nó được tạo ra sẽ giải thích
nhiều hành vi của nó. Đây là mức nhận biết — không cần kỹ thuật huấn luyện.

## Hai giai đoạn lớn

- **Pre-training** — mô hình học ngôn ngữ và kiến thức thế giới bằng cách dự đoán token kế tiếp
  trên một kho dữ liệu khổng lồ. Kết quả là **base model**: nhiều kiến thức nhưng chưa giỏi làm
  theo chỉ dẫn.
- **Post-training** — biến base model thành thứ hữu ích:
  - **Instruction / fine-tuning** — dạy làm theo chỉ dẫn và trả lời hữu ích.
  - **Alignment (ví dụ RLHF)** — tinh chỉnh bằng phản hồi của con người để hữu ích, trung thực và an toàn.

## Vì sao điều này quan trọng với bạn (builder)

- **Knowledge cutoff** — kiến thức đóng băng ở thời điểm pre-training. Với dữ kiện mới hoặc
  riêng tư, bạn cần [RAG]({{< relref "/foundations/rag" >}}), không phải một base model mới hơn.
- **Vì sao nó làm theo chỉ dẫn (và từ chối)** — hành vi đó đến từ post-training, không phải
  phép màu. Đó là lý do [prompting]({{< relref "/foundations/prompt-engineering" >}}) hiệu quả
  và đôi khi mô hình từ chối yêu cầu.
- **Fine-tuning làm gì** — nó điều chỉnh *hành vi và phong cách*, và dạy được kỹ năng hẹp một
  cách đáng tin cậy; nó **không** đáng tin để bổ sung kiến thức mới. Xem
  [Adaptation]({{< relref "/deep-dives/adaptation" >}}).

## Những gì bạn chưa cần

Tập dữ liệu, GPU, hàm mất mát, gradient descent. Nhà cung cấp lo hết; bạn dùng mô hình đã hoàn thiện.
