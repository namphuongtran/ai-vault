---
aliases: ["/foundations/under-the-hood/"]
title: "Under the Hood"
linkTitle: "Under the Hood"
weight: 5
description: Nhìn nhẹ vào transformer và attention — vừa đủ để hiểu vì sao LLM hành xử như vậy.
---

Tiếp nối [How LLMs work]({{< relref "how-llms-work.md" >}}). Bạn không cần cái này để
build, nhưng một mô hình tư duy nhẹ về *bên trong có gì* sẽ giải thích nhiều hành vi bạn gặp.

## Attention, gói trong một ý

LLM là **transformer**. Mẹo cốt lõi là **attention**: để dự đoán token kế tiếp, mô hình nhìn
*tất cả* token đến hiện tại và cân xem mỗi token quan trọng bao nhiêu với bước hiện tại. "It"
được nối với danh từ nó ám chỉ; một câu hỏi được nối với dữ kiện liên quan ở phía trước prompt.

```mermaid
flowchart LR
    In[All tokens so far] --> Att[Attention - weigh how tokens relate]
    Att --> H[Context-aware representation]
    H --> Next[Predict next token]
```

## Ví dụ — attention giải quyết cái gì

*"Chiếc cúp không bỏ vừa vali vì **nó** quá to."*

*Nó* là cái gì? Bạn biết ngay: chiếc cúp — vì *không bỏ vừa* và *quá to* trỏ về đó. Đổi thành
*quá nhỏ* thì *nó* lập tức thành cái vali. Attention chính là cơ chế cân các mối quan hệ giữa
token, nhờ vậy model trả lời đúng mà không cần bất kỳ luật ngữ pháp nào.

## Vì sao điều này giải thích hành vi bạn thấy

- **Context là tất cả** — mô hình không có bộ nhớ ngoài những gì trong window; attention làm việc
  đúng trên đoạn text đó. Context liên quan nhiều hơn → câu trả lời tốt hơn (và tốn hơn).
- **Thứ tự và cách diễn đạt quan trọng** — attention nhạy với cách viết và vị trí; đó là vì sao
  [prompting]({{< relref "prompt-engineering.md" >}}) và
  [context engineering]({{< relref "context-engineering.md" >}}) hiệu quả.
- **Chi phí tăng theo độ dài** — attention so từng token với nhau, nên đầu vào dài đắt lên không cân xứng.
- **Không thực sự "hiểu"** — đây là dự đoán mẫu, không phải thấu hiểu, nên mô hình có thể sai một
  cách tự tin (xem [Limitations]({{< relref "limitations.md" >}})).

## Nguồn

- Vaswani et al., *Attention Is All You Need* (2017) — [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
