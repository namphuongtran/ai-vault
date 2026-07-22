# 🧠 AI Vault

> A personal knowledge vault for everything I'm learning about Artificial Intelligence.

A bilingual documentation site (English / Tiếng Việt) built with **Hugo** and the
**[Docsy](https://www.docsy.dev/)** theme. Content is organized as a learning path from
foundations to advanced topics. English is the primary language; a Vietnamese translation
is available from the language switcher in the navbar.

## 📚 Content

- **Foundations (Stage 0)** — foundation models, generative AI, prompt engineering, RAG,
  agents, guardrails, model evaluation, and responsible AI.

More stages will be added over time.

## 🌐 Languages

Each language lives in its own content tree:

```
content/
├── en/   # English (primary, default)
└── vi/   # Tiếng Việt
```

To add a language, create `content/<lang>/…` and add a block under `languages:` in
`hugo.yaml`.

## 🛠️ Local development

Requires **Go** (for the Docsy Hugo module); Hugo is provided via npm.

```bash
npm install        # installs hugo-extended + build deps
npm run serve      # http://localhost:1313
npm run build      # production build into ./public
```

## 🗂️ Structure

```
ai-vault/
├── hugo.yaml       # site + language + Docsy config
├── go.mod          # Docsy pulled as a Hugo module
├── package.json    # hugo-extended + build scripts
└── content/
    ├── en/
    └── vi/
```

## 📖 License

MIT — personal study material, shared for inspiration.
