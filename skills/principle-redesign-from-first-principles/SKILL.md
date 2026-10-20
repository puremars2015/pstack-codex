---
name: principle-redesign-from-first-principles
description: 整合新需求時回到根本模型，思考需求若從一開始就存在，系統應如何設計。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before applying this workflow.


# Redesign From First Principles

When integrating a change, don't bolt it onto the existing design. Redesign as if the requirement had been a foundational assumption from the start.

- Read all affected files and understand the current design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the whole redesign, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.
