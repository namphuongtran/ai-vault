---
title: "Advanced RAG"
weight: 4
description: Chunking, hybrid retrieval, re-ranking, query transform và đánh giá RAG.
---

Tiếp nối [RAG ở phần Nền tảng]({{< relref "rag.md" >}}). RAG cơ bản thường kém hiệu
quả vì chất lượng *truy xuất*, không phải do mô hình. Các kỹ thuật sau nhắm vào điều đó.

Trong họ [Types of RAG]({{< relref "/deep-dives/types-of-rag" >}}), đây là trục *kỹ thuật*:
các bước bạn thêm vào bên trong bất kỳ kiến trúc nào, không phải một kiến trúc riêng.

## Chiến lược chunking

Cách chia tài liệu ảnh hưởng mạnh đến chất lượng truy xuất.

| Chiến lược | Ý tưởng | Khi nào dùng |
| ------------ | --------- | -------------- |
| Fixed-size | Chia mỗi N token, có overlap | Văn bản đơn giản, đồng đều |
| Recursive | Chia theo cấu trúc (heading → đoạn → câu) | Đa số tài liệu |
| Semantic | Chia ở nơi ý nghĩa thay đổi (khoảng cách embedding) | Văn bản dày, nhiều chủ đề |
| Document-aware | Tôn trọng bảng, code block, mục | PDF, tài liệu kỹ thuật |

Giữ mỗi chunk tự chứa ý; thêm một chút **overlap** (khoảng 10–20%) để ngữ cảnh không bị cắt
giữa chừng.

## Truy xuất: dense, sparse, hybrid

- **Dense** — tương đồng embedding; nắm được ý nghĩa và cách diễn đạt khác.
- **Sparse** — khớp từ khóa (BM25); nắm được thuật ngữ chính xác, tên riêng, mã.
- **Hybrid** — kết hợp cả hai rồi hợp nhất điểm (ví dụ Reciprocal Rank Fusion). Thường là lựa
  chọn mặc định mạnh nhất, vì mỗi bên bù điểm mù cho bên kia.

Vì sao hybrid thắng, gói trong một truy vấn: *"lỗi E-4012 khi đồng bộ hóa đơn bị timeout."*
Dense tìm ra các đoạn nói về *timeout khi đồng bộ hóa đơn* (đúng nghĩa) nhưng trượt mã lỗi
chính xác; sparse tìm ra mọi chỗ nhắc *E-4012* (đúng term) nhưng trượt tài liệu troubleshooting
viết bằng cách diễn đạt khác. Hợp nhất lại, trang đúng xếp hạng nhất.

## Re-ranking

Truy xuất một tập rộng (ví dụ top 50), rồi chấm lại bằng **cross-encoder** đọc cả câu hỏi và
đoạn văn cùng lúc, giữ lại vài kết quả tốt nhất. Chính xác hơn chỉ dùng tương đồng embedding,
nhưng tốn kém hơn — nên chỉ áp dụng cho danh sách rút gọn.

## Context compression

Chunk lấy về chứa nhiều câu không trả lời câu hỏi — tốn token và làm loãng sự chú ý của model.
**Context compression** cắt mỗi chunk còn đúng phần liên quan trước khi tới model:

- **Extractive** — chỉ giữ các câu khớp truy vấn (một model nhỏ hoặc filter chấm điểm từng câu).
- **Abstractive** — tóm tắt chunk còn các dữ kiện liên quan tới truy vấn.

Ví dụ: một chunk chính sách 1.200 token lấy về cho *"refund window bao lâu?"* nén còn hai câu
nêu mốc 30 ngày — rẻ hơn, và faithfulness *cao hơn*, vì model không bị phần văn bản xung quanh
làm phân tâm. Áp dụng sau re-ranking, trên danh sách rút gọn cuối; bỏ qua khi chunk đã gọn.

## Query transformation

Câu hỏi của người dùng thường không phải là truy vấn tìm kiếm tốt nhất.

- **Multi-query** — sinh vài cách diễn đạt lại, truy xuất cho từng cái, gộp lại.
- **HyDE** — sinh một câu trả lời giả định, embed *nó*, và tìm kiếm bằng nó.
- **Decomposition** — chia câu hỏi phức tạp thành các câu hỏi con, truy xuất riêng.

## Đánh giá RAG

Đo truy xuất và sinh câu trả lời tách biệt:

- **Context precision / recall** — truy xuất có ra đúng đoạn cần không?
- **Faithfulness** — câu trả lời có bám sát các đoạn đó không?
- **Answer relevance** — có thực sự trả lời đúng câu hỏi không?

Xem [Evaluation in practice]({{< relref "/deep-dives/evaluation-in-practice" >}}).

## Các lỗi thường gặp

- Chunk quá lớn (nhiễu) hoặc quá nhỏ (mất ngữ cảnh).
- Truy xuất bỏ sót thuật ngữ chính xác → thêm sparse/hybrid.
- Đúng đoạn được truy xuất nhưng xếp hạng thấp → thêm re-ranking.
- Câu trả lời lệch khỏi context → siết prompt và kiểm tra faithfulness.

## Nguồn

- Gao et al., *Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)* (2022) — [arXiv:2212.10496](https://arxiv.org/abs/2212.10496)
- Jiang et al., *LLMLingua: Compressing Prompts for Accelerated Inference* (2023) — [arXiv:2310.06839](https://arxiv.org/abs/2310.06839)
- Reimers & Gurevych, *Sentence-BERT* (2019, cross-encoder cho re-ranking) — [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) — [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) — [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)
