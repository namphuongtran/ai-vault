---
title: "Bước 7 — Kiểm soát của harness"
linkTitle: "Step 7 — Harness controls"
weight: 7
description: Luật permission, hook và lưu session — guardrail nằm trong code, không nằm trong prompt.
---

Đến giờ model chạy được mọi lệnh shell. Một harness được định nghĩa bởi những gì nó **từ chối**
làm, và các [guardrail]({{< relref "guardrails.md" >}}) đó phải nằm trong code, không nằm trong
prompt.

Đến cuối bước này bạn phải trả lời được: **vì sao luật phải nằm trong harness chứ không nằm
trong prompt?**

## Xây dựng

Thêm luật permission, hook và lưu session:

```python
RULES = [  # luật khớp đầu tiên thắng: (tên tool hoặc *, regex trên tham số, quyết định)
    ("run_bash", r"\brm\b|-delete|\bsudo\b|\bcurl\b|git\s+push", "deny"),
    ("run_bash", r"^(python -m pytest|ls|cat|grep|sed -n|wc)\b", "allow"),
    ("run_bash", r".*", "ask"),
    ("write_file", r".*", "ask"),
    ("*", r".*", "allow"),
]
ASK = threading.Lock()

def permit(call):
    args = " ".join(str(v) for v in call.input.values())
    for name, pattern, decision in RULES:
        if name in (call.name, "*") and re.search(pattern, args):
            if decision == "ask":
                with ASK:
                    return input(f"\nallow {call.name}: {args[:200]!r}? [y/N] ").strip().lower() == "y"
            return decision == "allow"
    return False

def audit(call, out):                      # một post-hook: mỗi tool call một dòng
    with open(WORKDIR.parent / "audit.jsonl", "a") as f:
        f.write(json.dumps({"tool": call.name, "input": call.input, "chars": len(out)}) + "\n")

HOOKS = {"pre": [], "post": [audit]}       # pre-hook trả về một chuỗi lý do để chặn

def result(call, content, is_error=False):
    return {"type": "tool_result", "tool_use_id": call.id,
            "content": content or "(empty)", "is_error": is_error}

def execute(call):
    if not permit(call):
        return result(call, "Denied by the harness permission rules. Choose another way.", True)
    for hook in HOOKS["pre"]:
        if reason := hook(call):
            return result(call, f"Blocked by a hook: {reason}", True)
    try:
        out, failed = FUNCS[call.name](**call.input), False
    except Exception as e:
        out, failed = f"{type(e).__name__}: {e}", True
    out = clip(call.id, out)
    for hook in HOOKS["post"]:
        hook(call, out)
    return result(call, out, failed)
```

Một lần từ chối quay về model như một kết quả lỗi bình thường, nên model có thể chọn cách khác.
Với session, lưu mọi message ngay khi nó được nối thêm, mỗi message một dòng, đúng cấu trúc
JSONL của Claude Code:

```python
def load(session):                         # resume từ mốc compaction gần nhất
    path = WORKDIR.parent / "sessions" / f"{session}.jsonl"
    lines = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
    start = max([i for i, m in enumerate(lines) if m["compacted"]], default=0)
    return [{"role": m["role"], "content": m["content"]} for m in lines[start:]]

def save(session, msg, compacted):         # chỉ nối thêm, mỗi message một dòng
    path = WORKDIR.parent / "sessions" / f"{session}.jsonl"
    path.parent.mkdir(exist_ok=True)
    content = msg["content"]
    if not isinstance(content, str):
        content = [b if isinstance(b, dict) else b.model_dump(mode="json", exclude_none=True) for b in content]
    with open(path, "a") as f:
        f.write(json.dumps({"role": msg["role"], "content": content, "compacted": compacted}) + "\n")
```

Trong `run()`, thêm tham số `session=None`. Khởi đầu từ `msgs = load(session) if session else
[]`, và cho mọi lần nối thêm đi qua một hàm phụ cũng đảm nhận việc lưu. Compaction trở thành một
mốc ranh giới thay vì một lần viết lại:

```python
    def push(msg, compacted=False):
        msgs.append(msg)
        if session:
            save(session, msg, compacted)
    # ...mọi chỗ nối thêm đều qua push(...), và khi compaction:
            summary = compact(task, msgs, system, tools, model)
            msgs.clear()
            push(summary, compacted=True)
```

## Kiểm tra

Bảo agent *"delete the test file"*. Lệnh `rm` bị từ chối và model đọc được lời từ chối. Bảo nó
sửa `calc.py` và bạn nhận được một câu hỏi xác nhận. `audit.jsonl` có một dòng cho mỗi lời gọi.
Chạy `run("How many files?", session="s1")`, rồi `run("Name them.", session="s1")`. Lần chạy thứ
hai biết lần đầu đã tìm ra gì.

## Xem trong Claude Code

- Permission nằm trong `settings.json` dưới dạng các luật `allow`, `ask` và `deny`, như
  `Bash(npm run test *)` hay `Bash(rm *)`.
- Các permission mode là `default`, `acceptEdits`, `plan`, `auto`, `dontAsk` và
  `bypassPermissions`.
- Một hook `PreToolUse` thoát với exit code 2 sẽ chặn lời gọi, và stderr của nó quay về model,
  y như pre-hook của bạn.
- `claude --continue` và `claude --resume` chính là `load()` của bạn.

Tài liệu nói thẳng: luật permission được Claude Code thực thi, không phải model.

## Làm hỏng nó

1. Bỏ luật `rm` và thay bằng câu *"never delete files"* trong `SYSTEM`. Rồi giao cho agent một
   task mà việc xoá trông có vẻ hữu ích.
2. Lách qua chính regex của bạn bằng `python -c "import shutil; shutil.rmtree('x')"` hoặc
   `python -m pytest && <anything>`. Luật theo tiền tố khớp với văn bản, không khớp với ý định.
   Đó là lý do harness thật tách các lệnh ghép và vẫn chạy bên trong sandbox.
3. Claude Code xét **deny, rồi ask, rồi allow**, nên một luật allow không bao giờ khoét được ngoại
   lệ trong một luật deny. Chuyển luật rộng `("*", r".*", "allow")` lên đầu `RULES` và xem vì sao
   thứ tự ưu tiên đó tồn tại.

## Đáp án

Model làm theo chỉ dẫn phần lớn thời gian, còn guardrail phải đứng vững mọi lúc, kể cả khi một
kết quả tool mang theo prompt injection. Chỉ code mới bảo đảm được điều đó.

**Tiếp theo:** [Bước 8 — Plug-in, và hàng thật]({{< relref "/hands-on/lab-agent-harness/step-8-mcp-and-agent-sdk" >}})
