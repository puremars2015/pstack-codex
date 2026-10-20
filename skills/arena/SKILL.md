---
name: arena
description: 針對同一任務比較多個候選方案，依明確標準選擇基礎方案並整合、驗證成果。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Arena

Declare the common task, output artifact, candidate count, and three to six task-specific evaluation criteria. Candidates share the same source baseline but own isolated writable directories or worktrees. Use allowed collaboration tools when available; otherwise generate candidates in sequential, explicitly labeled passes. Default to the current model; claim model diversity only when actual distinct models were available and used.

After candidate outputs stop changing, inspect every artifact and score it against the rubric. A permitted fresh read-only judge can review anonymized candidates. Choose one base, incorporate useful ideas deliberately, and explain rejected grafts. Run acceptance checks on the synthesized result, not just each candidate. Report scores, selection rationale, actual independence, dropouts, and validation gaps.
