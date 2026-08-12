---
title: "Evaluation in Practice"
weight: 11
description: Bộ eval, LLM-as-judge, offline vs online và regression testing.
---

Tiếp nối [Model Evaluation ở phần Nền tảng]({{< relref "model-evaluation.md" >}}).
Metric chỉ hữu ích khi bạn đánh giá một cách có hệ thống. Đây là cách thực sự chạy đánh giá.

## Xây bộ eval

- Thu thập đầu vào thật (hoặc sát thực tế) kèm đầu ra đúng đã biết hoặc tiêu chí chấp nhận.
- Bao phủ **ca thường gặp và ca biên** — những ca hay hỏng trong production.
- Bắt đầu nhỏ (20–50 ví dụ) và mở rộng khi phát hiện lỗi; mỗi bug trở thành một ca.
- Đánh version; coi nó như dữ liệu test.
- **Đãi [trace]({{< relref "observability.md" >}}) ra thành ca test.** Các run thật là nguồn
  đầu vào sát thực tế rẻ nhất, và những run đã hỏng sẵn chính là những ca đáng giữ nhất.

Hãy giữ hai loại ca, và đừng lẫn lộn mục đích của chúng:

- **Kiểu unit test** — hẹp, rẻ, và mặc định phải pass. Chúng canh regression; hỏng ở đây nghĩa
  là có cái gì đó vừa vỡ.
- **Kiểu integration test** — chạy đầu-cuối và thật sự khó. Đây là điểm số bạn đang leo lên;
  hỏng ở đây là giới hạn hiện tại, không phải bug.

**Khi không có đáp án đúng** — hay gặp với task mở hoặc task nghiên cứu — bạn không thu được
đầu ra đúng đã biết, nên hãy xây rubric thay vì đáp án. Cho một người gán nhãn tốt/xấu cho một
lô nhỏ output thật và nói rõ *vì sao*; chính các lý do đó trở thành rubric mà judge áp cho mọi
ca về sau. Nhãn của con người cũng là thước để bạn hiệu chỉnh judge.

## LLM-as-judge

Với đầu ra mở, nơi khớp chính xác không dùng được, hãy dùng một mô hình mạnh để **chấm** câu
trả lời theo một rubric.

- Cho judge tiêu chí rõ ràng và một thang điểm; yêu cầu nêu lý do trước, rồi chấm điểm.
- Ưu tiên so sánh **theo cặp** (A vs B) — đáng tin hơn điểm tuyệt đối.
- Kiểm chứng judge với một số nhãn của con người; đề phòng thiên lệch (độ dài, vị trí, thiên vị chính mình).

Một rubric tối giản, cho cụ thể:

> Chấm câu trả lời 1–5 về **faithfulness**: 5 = mọi khẳng định đều được context cung cấp hỗ
> trợ; 3 = vài chi tiết nhỏ không có căn cứ; 1 = mâu thuẫn với context. Trích các khẳng định
> không có căn cứ trước, rồi mới chấm điểm.

## Offline vs online

- **Offline** — chạy bộ eval trong CI trước khi ship thay đổi. Phản hồi nhanh, có kiểm soát.
- **Online** — đo trên sử dụng thật: phản hồi người dùng, thích/không thích, tỉ lệ hoàn thành, số ca chuyển tiếp.
- Offline bắt regression; online bắt những gì bộ eval bỏ sót. Bạn cần cả hai.

## Đánh giá RAG

Đánh giá truy xuất và sinh câu trả lời tách biệt (kiểu RAGAS):

- **Context precision / recall** — chất lượng truy xuất.
- **Faithfulness** — câu trả lời bám sát context truy xuất.
- **Answer relevance** — câu trả lời đúng trọng tâm câu hỏi.

Việc này cô lập được câu trả lời tệ đến từ truy xuất hay từ sinh câu trả lời.

## Regression testing

- Chạy bộ eval trong CI mỗi khi đổi prompt, mô hình hoặc pipeline.
- **Một memory hay skill đã lưu cũng là một thay đổi.** Agent
  [tự viết lại prompt và memory của mình]({{< relref "/deep-dives/self-improving-agents" >}})
  là đang sửa hành vi mà không đụng tới code, nên nó cần đúng cái cổng kiểm này — và chính cổng
  đó làm cho self-improvement merge được một cách an toàn.
- Cho build fail nếu tụt quá một ngưỡng.
- Ghim version mô hình; một bản cập nhật từ nhà cung cấp bản thân nó là một thay đổi cần đánh giá.

## Cạm bẫy

- Test trên chính các ví dụ đã dùng để tinh chỉnh (rò rỉ dữ liệu).
- Một điểm tổng hợp che giấu lỗi ở một lát cắt quan trọng — hãy tách kết quả theo nhóm.
- Tin một judge mà bạn chưa bao giờ kiểm chứng.

## Nguồn

- Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (2023) — [arXiv:2306.05685](https://arxiv.org/abs/2306.05685)
- Es et al., *RAGAS: Automated Evaluation of Retrieval Augmented Generation* (2023) — [arXiv:2309.15217](https://arxiv.org/abs/2309.15217)
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
