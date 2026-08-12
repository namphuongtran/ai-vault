---
title: "Self-Improving Agents"
linkTitle: "Self-Improving Agents"
weight: 8
description: Cách một agent giỏi lên theo thời gian mà không đổi trọng số model.
---

## Mục tiêu

Hiểu cách một agent có thể **giỏi lên qua từng run mà không cần huấn luyện lại** — không đổi
trọng số, không fine-tune. Model đứng yên; cái thay đổi là những gì bao quanh nó. Điều này quan
trọng vì huấn luyện lại thì chậm và đắt, nhưng một agent thiết kế tốt vẫn học được từ chính
trải nghiệm của nó ngay lúc runtime.

## Hai cách "học"

| | Đổi trọng số | Giữ nguyên trọng số (trang này) |
| ------ | ------ | ------ |
| Cơ chế | [Fine-tuning / RL]({{< relref "/deep-dives/adaptation" >}}) — cập nhật model | Memory, reflection, skills quanh một model cố định |
| Tốc độ | Chậm, offline, cần data + compute | Tức thì, lúc runtime |
| Cải thiện cái gì | Năng lực thô của model | Mức độ agent *áp dụng* năng lực cố định đó |
| Trần | Nâng được kỹ năng của model | Bị chặn bởi base model — dùng tốt hơn, không phải năng lực mới |

Self-improvement ở đây là cột thứ hai: năng lực base model là một cái trần, nhưng đa số agent
hoạt động *thấp hơn nhiều* so với trần đó vì chúng quên, lặp lỗi, và suy diễn lại quy trình.
Thu hẹp khoảng cách đó là nơi có lợi ích.

## Ba cơ chế

```mermaid
flowchart LR
    T[Attempt a task] --> O[Observe result]
    O --> R[Reflect - what went wrong or right]
    R --> S[Store the lesson - memory or skill]
    S --> T2[Next attempt - starts smarter]
    W[(Model weights - unchanged)] -.-> T
    W -.-> T2
```

- **Reflection** — agent tự đánh giá đầu ra so với mục tiêu và thử lại. Trong một task nó sửa
  lỗi; xuyên các task, reflection đã lưu ngăn lặp lại. **Reflexion** cho thấy điều này: một
  agent viết self-reflection sau mỗi lần fail đạt 91% trên một benchmark code so với 80% khi
  không có — cùng model, dùng tốt hơn.
- **Episodic memory** — nhớ kết quả đã qua để lỗi tuần trước không lặp lại. Xem
  [episodic memory]({{< relref "/deep-dives/agent-memory/episodic-memory" >}}).
- **Procedural memory / xây skill** — đóng gói một task đã giải thành skill tái dùng.
  **Voyager** xây một thư viện skill chạy được ngày càng lớn và ghép chúng cho task mới, nên nó
  thực sự có năng lực hơn qua một phiên — mà không đụng trọng số. Xem
  [procedural memory]({{< relref "/deep-dives/agent-memory/procedural-memory" >}}).

## Ví dụ — một agent học cách deploy

Một deploy agent fail vì quên chạy migration. Nó **reflect** ("migration phải chạy trước khi
restart"), **lưu** đó thành một bài học episodic, và sau đó **đóng gói** cả trình tự deploy
thành một skill procedural. Tuần sau, với một service mới, nó nhớ lại bài học và tái dùng skill
— thành công ngay lần đầu. Model không hề đổi; *hệ thống quanh nó* đã học.

## Học từ trace

Ba cơ chế trên làm việc *bên trong* một task. Cải thiện agent xuyên *nhiều* task cần một đầu
vào khác, vì nó cần một nguồn sự thật khác. Với phần mềm thường, sự thật về hành vi nằm ở code.
Với agent thì không — cùng một đoạn code cho ra mỗi run một khác, nên cái thật sự đã xảy ra chỉ
tồn tại trong [trace]({{< relref "observability.md" >}}): context nó được đưa, các tool nó gọi,
kết quả trả về, và phán xét trên output.

Một agent thứ hai, chạy sau, quét qua một lô trace để tìm lỗi *lặp lại*:

- một tool bị gọi sai tham số, run này qua run khác;
- một tool không bao giờ được gọi, vì không gì trong context cho agent biết là nó tồn tại;
- một sở thích người dùng đã nói một lần và agent cứ phớt lờ.

Rồi nó đề xuất cách sửa, và cách sửa rơi vào một trong hai chỗ:

- **Thủ tục (procedural)** — prompt, mô tả tool, và skill: công việc được làm *như thế nào*.
- **Ngữ nghĩa (semantic)** — dữ kiện và sở thích đã lưu: một trợ lý học được rằng phải viết
  trang trọng với sếp và thân mật với đồng nghiệp.

Nửa ngữ nghĩa chỉ chạy được nếu các lần chỉnh sửa có **đường ghi**. Khi người dùng chặn một bản
nháp quá suồng sã gửi sếp, lần chỉnh đó phải được củng cố (consolidate) thành một sở thích bền,
chứ không chỉ áp cho đúng cái mail này — nếu không tuần sau lỗi cũ quay lại. Xem
[semantic memory]({{< relref "/deep-dives/agent-memory/semantic-memory" >}}) cho chỗ nó được lưu.

## Sửa cái gì trước

Khi phân tích tìm ra một lỗi lặp lại, đừng vội viết lại kiến trúc. Đa số lỗi của agent không
phải *model không đủ thông minh*, mà là *model không có đúng thông tin*. Hãy đi từ trên xuống,
và dừng ngay khi lỗi hết:

1. **Memory và skill** — nó thiếu một dữ kiện hoặc một quy trình đáng lẽ phải có.
2. **Prompt và mô tả tool** — nó có đủ thứ cần nhưng dùng sai.
3. **Tool** — nó cần một năng lực mà không ai cấp cho.
4. **Kiến trúc** — chỉ khi agent liên tục hỏng ở chỗ *không được phép* hỏng, ví dụ một bước
   tuân thủ quy định. Khi đó hãy lấy quyết định đó ra khỏi model và biến nó thành một bước
   deterministic trong code.

Mỗi bậc đi xuống lại đắt hơn cả lúc sửa lẫn lúc nuôi. Hai bậc đầu giải quyết phần lớn.

Không thứ nào ở đây merge an toàn nếu thiếu eval. Một prompt mới hay một sở thích vừa lưu có
thể sửa được một ca và âm thầm làm hỏng năm ca khác, nên mọi thay đổi đề xuất đều phải chạy qua
[bộ eval]({{< relref "/deep-dives/evaluation-in-practice" >}}) trước. Chừng nào bộ eval đó chưa
đáng tin, con người duyệt lần merge — đúng vị trí cấp 4 trong
[bốn cấp độ loop]({{< relref "/building/loop-engineering/levels" >}}).

## Nó nằm ở đâu

Self-improvement là phần thưởng của các loại memory phối hợp với nhau, áp trong một
[loop]({{< relref "/building/loop-engineering" >}}). Trong một hệ
[multi-agent]({{< relref "/deep-dives/multi-agent" >}}), một knowledge graph chung làm việc học
trở nên *tập thể* — bài học của một agent giúp cả nhóm.

## Điểm mạnh & hạn chế

- **Điểm mạnh** — cải thiện mà không tốn chi phí và độ trễ huấn luyện lại; agent thích nghi với
  môi trường và lỗi *của bạn*; lợi ích tích lũy khi memory và skill dồn lại.
- **Hạn chế** — bị chặn bởi base model — không học được kỹ năng model về cơ bản không có (cái
  đó cần [fine-tuning]({{< relref "/deep-dives/adaptation" >}})); bài học đã lưu cũ đi hoặc sai
  và có thể đóng đinh một thói quen *xấu* dễ như một thói quen tốt; càng nhiều memory/skill càng
  nhiều nhiễu truy xuất. Hãy kiểm chứng cái được lưu và tỉa bớt — một vòng self-improvement
  không có cổng chất lượng sẽ tự thoái hóa.

## Nguồn

- Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning* (2023) — [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)
- Wang et al., *Voyager: An Open-Ended Embodied Agent with Large Language Models* (2023) — [arXiv:2305.16291](https://arxiv.org/abs/2305.16291)
- Huang et al., *Large Language Models Can Self-Improve* (2022) — [arXiv:2210.11610](https://arxiv.org/abs/2210.11610)
- Runkle, *The Art of Loop Engineering* (2026) — [langchain.com](https://www.langchain.com/blog/the-art-of-loop-engineering)
