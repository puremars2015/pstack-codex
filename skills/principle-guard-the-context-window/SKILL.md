---
name: principle-guard-the-context-window
description: 處理大量資訊時控制主對話的上下文用量，保留精要證據並在允許時分工探索。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before applying this workflow.


# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.
