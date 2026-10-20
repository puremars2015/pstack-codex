---
name: maintain-verification-skill
description: 修復專案驗證技能與功能對照表的落差，重新執行受影響的真實操作路徑。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Maintain behavioral verification

Read the existing verification skill, its feature map, and relevant application changes. Classify failures as harness drift, environment failure, or product defect with evidence. Change only entries contradicted by current behavior or requirements. Do not weaken expected outcomes to hide a regression.

Run at least the affected real path with the repaired harness. Validate instructions and local references. Report corrected mappings, actual checks, remaining gaps, and any product defect left unresolved. Avoid broad regeneration that destroys working project-specific knowledge.
