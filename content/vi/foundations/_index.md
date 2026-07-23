---
title: "Nền tảng (Giai đoạn 0)"
linkTitle: "Nền tảng"
weight: 1
type: docs
menu:
  main:
    weight: 1
description: >
  Các khối kiến thức cốt lõi của hệ thống AI hiện đại — từ foundation model đến responsible AI.
---

**Giai đoạn 0** là lớp nền tảng. Mục tiêu ở đây là chiều rộng, không phải chiều sâu: hiểu mỗi
khái niệm *là gì* và *khi nào* dùng. Chúng ta đi từ nền tảng đến nâng cao, phần giải thích sâu
hơn sẽ ở các giai đoạn sau.

Viết cho **builder kỹ thuật** — developer, AI/data engineer, DevSecOps, platform và solution
architect — những người muốn *dùng và áp dụng* AI, không phải huấn luyện mô hình. Ít đi sâu vào
ML/DL, tập trung vào những gì bạn cần để xây một cách tự tin.

## Trong phần này

1. **The AI landscape** — GenAI nằm ở đâu; bạn xây *với* mô hình, không huấn luyện chúng.
2. **Foundation model** — mô hình lớn, đa dụng, được huấn luyện trước.
3. **Generative AI** — mô hình tạo ra nội dung mới.
4. **How LLMs work** — token, dự đoán token kế tiếp, context window.
5. **How models are trained** — pre-training → fine-tuning → alignment (mức nhận biết).
6. **Choosing a model** — năng lực vs chi phí vs độ trễ vs context.
7. **Inference parameters** — temperature, top-p/top-k, max tokens, stop.
8. **Prompt engineering** — cách kiểm soát đầu ra của mô hình.
9. **Context engineering** — quản lý những gì đưa vào context window.
10. **Embeddings** — biến văn bản thành vector thể hiện ý nghĩa.
11. **RAG** — trả lời dựa trên dữ liệu bên ngoài (embeddings + vector store).
12. **Tool & function calling** — nguyên thủy giúp mô hình hành động.
13. **Agentic AI** — mô hình tự dẫn dắt hành động; cái harness.
14. **Agent** — mô hình lập kế hoạch và hành động bằng công cụ.
15. **MCP** — chuẩn mở để kết nối tool và dữ liệu với mô hình.
16. **Guardrail** — an toàn và kiểm soát quanh đầu vào/đầu ra.
17. **AI security** — prompt injection, jailbreak, rò rỉ dữ liệu, và cách phòng thủ.
18. **Model evaluation** — cách đo chất lượng cho từng tác vụ.
19. **Observability** — trace, metric và eval trên production.
20. **Responsible AI** — công bằng, minh bạch và giám sát của con người.
