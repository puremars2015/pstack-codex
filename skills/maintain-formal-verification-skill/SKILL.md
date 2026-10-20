---
name: maintain-formal-verification-skill
description: 程式變更後更新既有形式模型與驗證技能，重新檢查性質並釐清失敗原因。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Maintain formal verification

Read the existing model, assumptions, verifier command, and changed production behavior. Map each changed state or transition to the model. Distinguish implementation bugs, stale models, changed requirements, and environment failures. Never relax a property solely to get a green result.

Update only the necessary model/harness/instructions, rerun the real verifier, and preserve a counterexample or negative control. Report exact property, assumptions, tool/version, bounds, result, and unresolved correspondence gaps. A previous successful proof does not apply automatically to changed code.
