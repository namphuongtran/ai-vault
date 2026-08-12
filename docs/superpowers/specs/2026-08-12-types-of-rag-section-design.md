# Design: split "Types of RAG" into a section

Date: 2026-08-12
Status: approved
Branch: `docs/types-of-rag-section`

## Problem

A shared post listed six RAG architectures: Simple, Hybrid, Corrective (CRAG), Self-RAG,
Graph, and Agentic. Mapping that post against the vault found three thin spots and one bug.

| Post item | Where it lives today | Verdict |
| ------ | ------ | ------ |
| Simple RAG | `foundations/ground-in-data/rag.md` (full page) | covered |
| Hybrid RAG | `deep-dives/advanced-rag.md:24` and `:36` | covered as a technique |
| Corrective RAG | `deep-dives/types-of-rag.md`, one bullet | thin |
| Self-RAG | same bullet | thin |
| Graph RAG | one table row | thin |
| Agentic RAG | `building/agentic-rag.md` (full page) | covered |
| "no best one" | a decision flowchart, no cost or latency axis | thin |

Bug: `content/en/deep-dives/types-of-rag.md:57` says "Agentic RAG (Stage 2, coming soon)",
but `content/en/building/agentic-rag.md` exists. The VI file has the same stale text.

## The organizing idea

The post calls CRAG and Self-RAG architectures. The current page calls them refinements and
stops there. Both framings are half right, and that gap is the content worth writing.

The taxonomy moves from two kinds to three:

| Kind | What it changes | Members |
| ------ | ------ | ------ |
| Architecture | the shape: what you retrieve from | Standard, Graph, Multimodal, Agentic |
| Control loop | the flow: retrieve once, or grade and retry | CRAG, Self-RAG |
| Technique | one step inside any of the above | hybrid search, re-ranking, query transforms |

This keeps the page's existing claim intact, explains why the post disagrees, and gives CRAG
and Self-RAG a real home.

## Decisions

1. **Split into a section, do not grow one page.** A single page carrying six architectures
   plus a comparison table feels heavy to read. This follows the same pattern already used by
   `deep-dives/agent-memory/` and `building/loop-engineering/`: a short `_index.md` map, plus
   one focused sub-page per item.
2. **Hybrid RAG stays a technique.** The post promotes it to an architecture. The vault does
   not, because `advanced-rag.md` already owns hybrid retrieval as one step inside a pipeline.
   Accuracy wins over matching the post.
3. **Only three sub-pages, not six.** The section writes only what it owns. Standard, Agentic,
   and Hybrid already have owner pages, so they are linked, not repeated.

## Target structure

```
content/{en,vi}/deep-dives/types-of-rag/
  _index.md           weight 3   the map only        ~90 lines
  graph-rag.md        weight 1   Graph RAG           ~55 lines
  multimodal-rag.md   weight 2   Multimodal RAG      ~45 lines
  self-correcting.md  weight 3   CRAG and Self-RAG   ~60 lines
```

The old flat file becomes `_index.md` through `git mv`, so history is preserved.

### Why each sub-page exists

| Family member | Sub-page | Reason |
| ------ | ------ | ------ |
| Graph RAG | yes | nothing owns it, one table row today |
| Multimodal RAG | yes | nothing owns it, one table row today |
| CRAG and Self-RAG | yes, one shared page | nothing owns them, one bullet today |
| Standard RAG | no | `foundations/ground-in-data/rag.md` owns it |
| Agentic RAG | no | `building/agentic-rag.md` owns it |
| Hybrid search | no | `advanced-rag.md` owns it |

## Page contents

### `_index.md`, the map

Front matter matches `agent-memory/_index.md`: `title`, `linkTitle`, `weight: 3`,
`type: docs`, `no_list: true`, and an updated `description`.

Sections in order:

1. `## Goal`. What a reader can answer after this section.
2. `## The family`. The existing table, plus a "read more" column that points to the owner
   page for each of the six members.
3. `## Architecture, loop, or technique`. The three-way split above. Replaces the current
   "Architectures vs. techniques" section.
4. `## In this section`. Nav table for the three sub-pages, same format as
   `agent-memory/_index.md`.
5. `## Choosing one`. New comparison table with these columns: accuracy gain, added latency,
   added cost, complexity, and worth it when. This carries the post's "there is no best RAG"
   point.
6. `## Which one?`. The existing mermaid decision flowchart, extended with a self-correction
   branch.
7. `## Where to go next`. The stale "coming soon" text replaced with a real relref to
   `/building/agentic-rag`.
8. `## Sources`. The four arXiv citations already on the page are kept.

### Sub-page shape

Each sub-page follows the `agent-memory` sub-page shape:

1. A one-line italic summary under the front matter.
2. `## What it is`.
3. Its own mermaid flowchart.
4. `## How it works`.
5. `## When to use it`.
6. `## Example`. One concrete case, not a list.
7. `## Sources`, when the page has a citation of its own.

Per-page notes:

- `graph-rag.md`. Contrast chunk retrieval with entity and relation retrieval. Use a
  multi-hop question as the example. Link to `deep-dives/multi-agent.md` rather than
  re-explaining how a knowledge graph is built.
- `multimodal-rag.md`. Retrieval over images, tables, and audio. Cover the two common
  designs: one shared embedding space, or caption the media and retrieve the text.
- `self-correcting.md`. One diagram showing both loops. A table comparing CRAG and Self-RAG on
  what triggers them, what they grade, and what they cost. State plainly that both add at
  least one extra model call per query.

## Ownership rules to respect

- Graph RAG here means the knowledge graph as a **retrieval index**. `multi-agent.md` already
  owns the knowledge graph as **shared agent memory**. Link, do not repeat.
- The self-correcting page describes the control loop only. Retrieval quality itself stays
  owned by `advanced-rag.md`.
- Agentic RAG stays a pointer to `building/agentic-rag.md`.

## Links and URLs

The URL `/deep-dives/types-of-rag/` does not change, because the folder index takes over the
old page path. That keeps all eight inbound links working:

| File | Line |
| ------ | ------ |
| `content/en/roadmap/_index.md` | 48, 97 |
| `content/vi/roadmap/_index.md` | 48, 97 |
| `content/en/foundations/ground-in-data/rag.md` | 74 |
| `content/vi/foundations/ground-in-data/rag.md` | 76 |
| `content/en/deep-dives/_index.md` | 37 |
| `content/vi/deep-dives/_index.md` | 38 |
| `content/en/building/agentic-rag.md` | 8 |
| `content/vi/building/agentic-rag.md` | 9 |

No `aliases` entries are needed, because no URL moves.

## Out of scope

- The Martin Fowler article on Structured-Prompt-Driven Development. It is a different topic
  and belongs in the `building` section. A grep of `content/en` for
  `spec-driven|SPDD|structured prompt` returned zero hits, so it is fully net-new work for a
  later change.
- No new top-level page, so the roadmap marks, the deep-dives landing count, and the homepage
  counts do not change.
- No restructuring of `advanced-rag.md`.

## Conventions to follow

- Vietnamese mirror carries the same four files, same structure, and the same mermaid blocks
  with English labels.
- Mermaid: flowchart only. Avoid `<br/>`, parentheses, and colons inside `[]` labels.
- Cross-links to foundation pages use filename-based relref. Links to other sections use
  path-based relref, matching what the existing files already do.

## Verification

1. `npm run lint:md:fix`, then `npm run lint:md` returns clean.
2. `npm run build` succeeds.
3. `npm run serve`, then open `/deep-dives/types-of-rag/` and confirm the sidebar groups the
   three sub-pages, and that every mermaid block renders.
4. Confirm each of the eight inbound links in the table above still resolves.
5. Branch, pull request, CI gate on Lint Markdown and Build, then squash merge.
