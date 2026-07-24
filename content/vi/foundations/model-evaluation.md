---
title: "Model Evaluation"
weight: 26
description: Cách đo chất lượng mô hình — chọn metric phù hợp với tác vụ.
---

## Là gì

Một mô hình có thể hoạt động tốt ở tác vụ này nhưng chưa phù hợp với tác vụ khác, nên **model
evaluation** rất quan trọng. Khi lựa chọn metric, cần dựa trên mục tiêu thực tế của bài toán.

## Metric cho sinh văn bản

- **ROUGE** — thường dùng để đánh giá chất lượng **tóm tắt văn bản**, so sánh mức độ trùng khớp
  giữa nội dung do mô hình tạo ra và nội dung tham chiếu. Nói về tóm tắt → nghĩ tới ROUGE.
- **BLEU** — thường dùng trong **machine translation**; so sánh các chuỗi từ hoặc cụm từ giữa
  bản dịch của mô hình và bản dịch tham chiếu. Nói về dịch máy → nghĩ tới BLEU.

## Metric cho phân loại

- **Precision** — trong số kết quả được dự đoán là positive, có bao nhiêu thực sự đúng. Quan
  trọng khi chi phí của **false positive** cao (ví dụ hệ thống phát hiện gian lận gắn cờ nhầm
  giao dịch hợp lệ).
- **Recall** — trong số các trường hợp positive thực tế, mô hình phát hiện được bao nhiêu. Quan
  trọng khi chi phí của **false negative** cao (ví dụ hệ thống sàng lọc bệnh bỏ sót ca thật).
- **F1 score** — cân bằng giữa precision và recall; hữu ích khi cả hai loại lỗi đều quan trọng
  hoặc khi dữ liệu giữa các lớp không cân bằng.

## Metric riêng cho RAG

- **Faithfulness** — câu trả lời có bám sát context được cung cấp hay không. Một câu trả lời có
  thể nghe rất tự nhiên nhưng vẫn chứa thông tin không tồn tại trong tài liệu truy xuất.
- **Context relevance** — tài liệu/đoạn văn được truy xuất có thực sự liên quan đến câu hỏi không.
  Nếu truy xuất sai, mô hình có thể tạo câu trả lời kém chính xác dù bản thân nó hoạt động tốt.

## Human evaluation

**Human evaluation** phù hợp khi chất lượng khó được đánh giá đầy đủ bằng metric tự động.
