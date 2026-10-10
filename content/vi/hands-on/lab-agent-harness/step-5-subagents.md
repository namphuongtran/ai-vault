---
title: "Bước 5 — Subagent"
linkTitle: "Step 5 — Subagents"
weight: 5
description: Chính run() của bạn được gọi lại với một context mới, ít tool hơn và một model rẻ hơn.
---

Subagent không phải là một loại thứ mới. Nó là **chính `run()` của bạn được gọi lại** với `msgs`
mới tinh, system prompt riêng, ít tool hơn, và thường là một model rẻ hơn. Chỉ báo cáo cuối cùng
của nó quay về. Lý do chính để dùng subagent là **cô lập context**. Chạy song song chỉ đứng thứ
hai.

Đến cuối bước này bạn phải trả lời được: **khi nào *không* nên dùng subagent?**

## Xây dựng

```python
MODELS = {"main": "claude-opus-5-5", "sub": "claude-haiku-5-5"}
READ_ONLY = [t for t in TOOLS if t["name"] in ("list_files", "read_file")]
SUB_SYSTEM = "You are a research subagent. Read only what the task needs, then report briefly."

def delegate(task):
    return run(task + "\n\nEnd with a short report: findings and file paths only.",
               tools=READ_ONLY, model=MODELS["sub"], effort="low", max_turns=15,
               agent="sub", system=SUB_SYSTEM)

TOOLS.append(tool(delegate,
    "Hand a self-contained, read-only research subtask to a subagent with a fresh context. "
    "It returns only a short report. Call it several times in one turn to run subtasks in parallel.",
    task="Complete instructions. The subagent sees nothing of this conversation."))
FUNCS["delegate"] = delegate
```

`run()` có thêm các tham số `effort`, `agent` và `system`: dùng `system = system or
system_prompt()`, còn `effort` đi vào dưới dạng `output_config={"effort": effort}`. Rồi sửa một
chỗ để các lời gọi song song thật sự chạy cùng lúc:

```python
        with ThreadPoolExecutor() as pool:          # các tool call song song chạy đồng thời
            msgs.append({"role": "user", "content": list(pool.map(execute, calls))})
```

Để ý rằng `READ_ONLY` được lấy **trước** khi thêm `delegate`, nên subagent không thể sinh ra
subagent.

## Kiểm tra

Với `WORKDIR` trỏ vào bản sao vault, hỏi *"Which pages discuss subagents, and what does each say
about when to use them? Use one subagent per top-level section."* Context của agent chính vẫn
nhỏ. Các subagent mới là bên đọc trang. Rồi cộng token của mọi lời gọi: **tổng lớn hơn** so với
khi một agent tự trả lời câu đó. Anthropic cho biết, theo dữ liệu của họ, hệ multi-agent dùng
khoảng 15× số token của một cuộc chat. Cô lập phải trả bằng tiền.

## Xem trong Claude Code

Tạo `.claude/agents/reviewer.md`:

```markdown
---
name: reviewer
description: Reviews a diff for bugs. Use after code changes.
tools: Read, Grep, Glob
model: haiku
---
You review code changes for correctness bugs. Report file:line and one sentence per finding.
```

Frontmatter là chữ ký `delegate()` của bạn, còn phần thân là `SUB_SYSTEM` của nó. Mỗi subagent
chạy trong context window riêng. Transcript của nó nằm ở
`~/.claude/projects/<project>/<session-id>/subagents/`.

## Làm hỏng nó

Cho hai subagent cùng sửa một file một lúc. Cái này ghi đè cái kia. Rồi giao cho một subagent
task *"fix it"* mà không kèm context. Nó chưa từng thấy hội thoại, nên không biết "it" là gì.

## Đáp án

Đừng dùng subagent khi các task con dùng chung trạng thái hoặc phải chạy tuần tự, khi chúng ghi
vào cùng file, hoặc khi task đủ nhỏ để số token tăng thêm chẳng mua được gì.

**Tiếp theo:** [Bước 6 — Mỗi vai một model]({{< relref "/hands-on/lab-agent-harness/step-6-model-per-role" >}})
