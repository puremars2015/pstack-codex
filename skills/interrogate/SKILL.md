---
name: interrogate
description: 針對具體程式差異進行對抗式審查，找出可證明的缺陷與結構問題。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Interrogate

Establish the exact base/head and intended behavior. Read the diff and its callers, boundary types, and invariants. Use the bundled [rubric](references/rubric.md). Examine correctness, failure paths, concurrency, data integrity, complexity, and verification only where relevant.

For independent review, use permitted read-only workers with distinct lenses. The same model on a fresh pass is not a different-model review. If independent workers are unavailable, perform distinct passes and disclose that limitation. Reviewers must name an affected location, reachable failure path, impact, and cheap reproducer. Assess every finding yourself; reject unsupported hypotheticals. After fixes, review changed paths again at the new revision. Return actionable findings ordered by severity, or say that no actionable findings were found and identify actual coverage limits.
