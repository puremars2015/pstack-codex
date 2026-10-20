---
name: principle-migrate-callers-then-delete-legacy-apis
description: 遷移內部 API 時同步更新呼叫端並移除舊路徑，避免留下無需求支撐的相容層。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before applying this workflow.


# Migrate Callers Then Delete Legacy APIs

- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative
