---
name: correct
description: 根據你反覆提出的修正，找出共同原因，將改善落實於架構、型別或檢查機制。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Correct

Gather corrections from accessible relevant context, not private application storage. Group demonstrated recurring mistakes by cause. For each, choose the highest useful enforcement layer: domain/API shape, types, lint/CI, behavioral test, then documentation. Preserve product direction and avoid treating preferences as universal constraints.

Implement authorized scoped corrections and validate the actual behavior. Return a table pairing each repeated mistake, its evidence, the chosen enforcement, and validation. If only prose can help, state the limitation. Do not modify global instructions as an implicit side effect.
