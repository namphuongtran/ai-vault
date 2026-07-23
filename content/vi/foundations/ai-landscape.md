---
title: "The AI Landscape"
linkTitle: "The AI Landscape"
weight: 1
description: GenAI nằm ở đâu — và vì sao, với vai trò builder, bạn dùng mô hình chứ không huấn luyện chúng.
---

Bạn không cần xây mô hình AI để tạo ra những thứ mạnh mẽ với chúng. Trang này đặt đúng vị trí
các khái niệm cốt lõi để phần sau dễ hiểu — không cần toán.

## Cấu trúc lồng nhau: AI ⊃ ML ⊃ DL ⊃ GenAI

- **AI** — mục tiêu rộng: làm cho phần mềm thực hiện các tác vụ "thông minh".
- **ML (machine learning)** — AI học mẫu từ dữ liệu thay vì quy tắc lập trình cứng.
- **DL (deep learning)** — ML dùng mạng nơ-ron lớn.
- **Generative AI** — mô hình DL *tạo ra* nội dung (văn bản, hình ảnh, code). LLM và các
  [foundation model]({{< relref "/foundations/foundation-models" >}}) nằm ở đây.

## Foundation model đã thay đổi điều gì

Chúng được huấn luyện trước trên dữ liệu khổng lồ, đa dụng, và dùng qua API hoặc prompt. Bạn
không thu thập dữ liệu hay huấn luyện chúng — bạn **dùng** chúng và điều chỉnh hành vi bằng
prompt, dữ liệu của bạn (RAG), và tool.

## Vai trò của bạn với tư cách builder

Công việc là **orchestration**, không phải huấn luyện: ghép mô hình vào phần mềm, công cụ và
tự động hoá, rồi kiểm soát và đánh giá đầu ra. Kỹ năng quan trọng: prompting, context/RAG,
thiết kế tool & agent, guardrail, đánh giá, và ý thức về chi phí/độ trễ.

## Những gì bạn chưa cần (bây giờ)

Thuật toán huấn luyện, gradient descent, chi tiết kiến trúc mô hình. Là kiến thức nền hữu ích
về sau — không bắt buộc để bắt đầu làm.
