---
name: principle-laziness-protocol
description: 優先刪除多餘內容，以能解決問題的最小變更完成工作，避免不必要的抽象與層次。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before applying this workflow.


# Laziness Protocol

- **Consolidate decisions.** Do not repeat the same choice in several places. Put it behind one source of truth and pass the result as a simple flag.
- **Minimize the diff.** Make the smallest change that solves the problem. Fewer lines beat "elegant" boilerplate.
