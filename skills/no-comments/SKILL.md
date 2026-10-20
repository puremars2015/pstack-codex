---
name: no-comments
description: 檢查過時或重複的程式註解，保留必要契約、設計理由、授權與工具指示。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Comment review

Read comments in the requested diff and nearby code. Keep licensing, public API contracts, non-obvious intent, externally imposed constraints, and necessary tool directives. Remove stale or redundant narration only when its meaning is carried by code. Prefer encoding a proven invariant in a type, assertion, or lint rule when that improves the design without broadening scope.

A read-only comment-focused reviewer may be used when permitted and useful; no custom agent type is required. Independently assess findings. Do not strip all comments or alter runtime behavior as a cleanup side effect. Verify any code edits and report material retained or removed intent.
