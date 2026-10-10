---
title: "Serving Models"
linkTitle: "Serving models"
weight: 3
type: docs
no_list: true
description: Tầng inference — có nên tự host không, làm sao để model vừa phần cứng, phục vụ nhanh, và sống sót khi hỏng.
---

## Mục tiêu

Tất cả những gì nằm giữa *"tôi có một model"* và *"app của tôi gọi được nó dưới tải."*
[The AI API]({{< relref "the-ai-api.md" >}}) dạy bạn thực hiện một lời gọi;
[AI system design]({{< relref "/building/ai-system-design" >}}) và
[scaling to production]({{< relref "/building/scaling-to-production" >}}) khảo sát hệ thống bao
quanh nó. Phần này là tầng ở giữa — **tầng inference** — và đó là phần mà một managed API giấu
đi khỏi bạn, cho tới ngày bạn cần đến nó.

## Tầng này gồm gì

```mermaid
flowchart LR
    App[Your app] --> GW[Gateway - routing and fallback]
    GW --> LB[Queue and load balancer]
    LB --> ENG[Serving engine - vLLM or TensorRT or SGLang]
    ENG --> W[Model weights - quantized]
    W --> GPU[GPU or CPU you chose]
```

Đọc sơ đồ từ phải sang trái là bạn có đúng thứ tự của phần này: chọn phần cứng, làm trọng số
vừa với nó, đặt một engine phía trước, đặt một queue trước engine, và đặt một router trước tất cả.

## Trong phần này

Thứ tự ở đây là một chuỗi phụ thuộc, không phải thực đơn — mỗi trang giả định bạn đã đọc trang trên:

| # | Trang | Câu hỏi nó trả lời |
| ------ | ------ | ------ |
| 1 | [Local vs cloud]({{< relref "local-vs-cloud.md" >}}) | Có nên tự host không? |
| 2 | [Quantization]({{< relref "quantization.md" >}}) | Làm sao để trọng số vừa phần cứng? |
| 3 | [Serving engines]({{< relref "serving-engines.md" >}}) | Làm sao ép throughput ra khỏi một GPU? |
| 4 | [Load balancing & queuing]({{< relref "load-balancing-queuing.md" >}}) | Làm sao đi từ một replica lên nhiều replica? |
| 5 | [Routing & fallback]({{< relref "routing-and-fallback.md" >}}) | Chuyện gì xảy ra khi model chậm, đắt, hoặc chết? |

**Nếu bạn không bao giờ tự host, hãy đọc 1 và 5.** Trang 1 nói vì sao ở lại với managed API
thường là đúng, còn trang 5 áp dụng nguyên vẹn cho managed API — routing và fallback là hai
pattern mọi app AI production đều cần, bất kể ai vận hành GPU.

## Mỗi tầng mua cho bạn điều gì

| Tầng | Đòn bẩy | Lợi ích điển hình | Cái giá phải trả |
| ------ | ------ | ------ | ------ |
| **Chọn phần cứng** | GPU riêng vs trả theo token | Chi phí cố định thắng per-token khi vượt ngưỡng sản lượng | Ops, hoạch định năng lực, tiền trả cho lúc nhàn rỗi |
| **Quantization** | Độ chính xác số của trọng số | Ít hơn 2–4× VRAM, decode nhanh hơn 1,5–3× | Mất một phần chất lượng — bắt buộc phải đo |
| **Serving engine** | Bố trí bộ nhớ và batching | Throughput gấp 5–20× so với vòng lặp ngây thơ | Thêm một hệ thống phải vận hành và tinh chỉnh |
| **Queue + load balancer** | Admission control qua nhiều replica | Sống sót qua đỉnh tải thay vì sụp đổ | Thêm độ trễ, thêm bộ phận chuyển động |
| **Routing + fallback** | Model nào trả lời | Tiết kiệm chi phí lớn, không còn điểm chết đơn lẻ | Hành vi thay đổi tuỳ model nào phục vụ bạn |

Mỗi dòng chỉ đáng kéo khi dòng phía trên đã được tinh chỉnh. Quantize một model mà managed API
có thể phục vụ bạn là ví dụ kinh điển của việc giải sai bài toán.

## Đi tiếp

- Hệ thống bao quanh tầng này → [Scaling to production]({{< relref "/building/scaling-to-production" >}}).
- Có nên fine-tune model bạn đang phục vụ → [Adaptation]({{< relref "/deep-dives/adaptation" >}}).
- Đo gì khi đã chạy thật → [Observability]({{< relref "observability.md" >}}).

Phần lớn team nên đọc trang 1, kết luận "ở lại với API", triển khai trang 5, rồi quay lại trang
2–4 vào năm mà họ thật sự cần đến chúng.

## Nguồn

- Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (2023) — [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)
- Frantar et al., *GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers* (2022) — [arXiv:2210.17323](https://arxiv.org/abs/2210.17323)
- Lin et al., *AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration* (2023) — [arXiv:2306.00978](https://arxiv.org/abs/2306.00978)
- Zheng et al., *SGLang: Efficient Execution of Structured Language Model Programs* (2023) — [arXiv:2312.07104](https://arxiv.org/abs/2312.07104)
