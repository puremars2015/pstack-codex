---
name: how
description: 沿著程式碼、呼叫端與執行證據，追查既有子系統的資料流與實際運作方式。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# How it works

Start from the user's concrete operation. Find the entry point, domain types, state ownership, important branches, side effects, and exit. Follow real callers and pinned dependencies. Separate a code-derived explanation from observed runtime behavior. Use small targeted executions when they settle a fact within scope.

For a large subsystem, partition exploration by boundary if delegation is permitted; otherwise trace each boundary sequentially. Keep evidence as file/line references and concise data-flow notes. Explain the main path first, then the edge cases that change the answer. Record uncertainty instead of inventing a connection. Return an answer at the user's requested depth, with references and unresolved questions.
