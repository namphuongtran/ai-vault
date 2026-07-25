---
aliases: ["/foundations/limitations/"]
title: "Limitations & Failure Modes"
linkTitle: "Limitations & Failure Modes"
weight: 8
description: Mô hình sai ở đâu và vì sao — để biết khi nào cần thêm RAG, tool, guardrail, hoặc con người.
---

Biết *mô hình sai thế nào* cho bạn biết *cần thêm gì* quanh nó. Không cái nào là "bug" — chúng
đến từ chính [cách LLM hoạt động]({{< relref "how-llms-work.md" >}}).

## Các kiểu lỗi chính

| Kiểu lỗi | Là gì | Giảm thiểu |
| ---------- | ------- | ------------ |
| Hallucination | Tự tin nhưng sai hoặc không có căn cứ | [RAG]({{< relref "rag.md" >}}) + trích dẫn; cho phép "không biết" |
| Knowledge cutoff | Không biết dữ kiện mới hoặc riêng tư | RAG, tool, web search |
| Kém toán / đếm chính xác | Dự đoán token hợp lý, không tính toán | Cho nó [tool / code]({{< relref "tool-function-calling.md" >}}) |
| Non-determinism | Cùng prompt → câu trả lời khác nhau | Hạ temperature, ràng buộc đầu ra, [đánh giá]({{< relref "model-evaluation.md" >}}) |
| Nhạy với prompt | Đổi chữ nhỏ cũng lệch kết quả | Test prompt trên bộ eval |
| Bias | Phản ánh thiên lệch trong dữ liệu huấn luyện | [Responsible AI]({{< relref "responsible-ai.md" >}}), giám sát của con người |
| Giới hạn context | Quên/rớt thông tin ngoài window | [Context engineering]({{< relref "context-engineering.md" >}}) |

## Mô hình chung

```mermaid
flowchart LR
    H[Hallucination / cutoff] --> RAG[Ground with RAG + citations]
    M[Bad math / counting] --> Tools[Use tools and code]
    ND[Non-determinism] --> Eval[Constrain + evaluate]
    B[Bias / safety] --> Gov[Guardrails + human oversight]
```

## Điều rút ra

Một mô hình đứng một mình thì không đáng tin cho dữ kiện, toán, và tính nhất quán. Bạn làm nó
đáng tin bằng cách **bao quanh nó** — neo vào dữ liệu, cho tool, ràng buộc đầu ra, và đo lường.
Đó chính là nội dung của phần còn lại trong giai đoạn này.

## Nguồn

- Ji et al., *Survey of Hallucination in Natural Language Generation* (2022) — [arXiv:2202.03629](https://arxiv.org/abs/2202.03629)
