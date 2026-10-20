---
name: create-formal-verification-skill
description: 針對明確性質建立可重現的專案形式驗證技能，記錄假設、界限與實際驗證結果。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Create formal verification

Choose one property tests struggle to cover, such as retry idempotency, a state transition invariant, or parser soundness. State assumptions, modeled environment, state bounds, and the link between model and production code. Discover installed or project-supported verification tools; do not claim proof from a test or invent an unavailable verifier.

Build the smallest useful model/harness and run the verifier. Exercise a deliberately invalid model or known counterexample to establish that the harness detects the property violation. Follow skill-creator guidance to package rerun instructions and inputs in a project-local skill. Report proved versus bounded-checked claims precisely, including version, command, limits, and remaining modeling assumptions.
