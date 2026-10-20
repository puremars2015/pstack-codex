---
name: swarm
description: 將允許平行處理的工作切成明確負責範圍，彙整各項實作、調查或驗證證據。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Swarm

Frame the done condition and required coverage before launching. Choose partitioned slices, a race with a declared winner rule, or both. Fix the source revision and measurement method where relevant. Each brief contains the goal, owned files/output, forbidden changes, acceptance check, and required evidence. Respect runtime delegation rules and concurrency limits. Sequential coverage is the fallback when workers are unavailable.

Wait for completion with the available collaboration tools, inspect outputs, and reconcile conflicting findings. Reports use PASS, ISSUES, or BLOCKED, with exact evidence and revision. A missing worker is a coverage gap, not a pass. Retry a failed slice only with a concrete corrected brief; do not loop indefinitely. Return one consolidated report and actual coverage.
