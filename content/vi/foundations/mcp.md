---
title: "MCP (Model Context Protocol)"
linkTitle: "MCP (Model Context Protocol)"
weight: 13
description: Chuẩn mở để kết nối tool và dữ liệu với mô hình — là gì và vì sao tồn tại.
---

**MCP (Model Context Protocol)** là một chuẩn mở để kết nối mô hình với tool và dữ liệu bên
ngoài. Hãy xem nó như một "phích cắm" chung: thay vì đấu nối thủ công từng tích hợp, bạn kết
nối tới các MCP server bày ra năng lực theo một khuôn dạng chuẩn.

## Vấn đề nó giải quyết

Trước MCP, mỗi ứng dụng tự đấu nối [tool]({{< relref "/foundations/tool-function-calling" >}}) và
nguồn dữ liệu theo cách riêng. N ứng dụng × M tích hợp nghĩa là xây đi xây lại cùng những
connector. MCP chuẩn hoá giao diện để một tích hợp được viết **một lần** và tái dùng bởi mọi
ứng dụng tương thích MCP.

## Cách ghép lại với nhau

- **MCP server** — bày ra năng lực (server GitHub, server database, server filesystem, …).
- **MCP client / host** — ứng dụng hoặc agent kết nối tới các server và đưa năng lực của chúng
  cho mô hình.

Một server có thể bày ra ba thứ:

- **Tools** — hàm mô hình có thể gọi (xem [Tool & function calling]({{< relref "/foundations/tool-function-calling" >}})).
- **Resources** — dữ liệu/context mô hình có thể đọc (file, bản ghi).
- **Prompts** — mẫu prompt tái sử dụng.

## Vì sao điều này quan trọng với bạn

- **Tái dùng thay vì xây lại** — kết nối tới một server có sẵn thay vì viết connector.
- **Tính di động** — cùng một server chạy được trên mọi client tương thích MCP.
- **Là xương sống của hệ sinh thái** — nhiều "connector", "skill" và "plugin" bên dưới là MCP server.

> *MCP là gì* thuộc phần nền tảng. *Xây* một MCP server là chủ đề giai đoạn build — để sau.
