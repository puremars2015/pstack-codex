---
name: architect
description: 以真實呼叫情境比較 API、資料模型與模組邊界，釐清重要設計取捨後再實作。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Architect

Read relevant callers and constraints. Write two or three representative usage examples before deriving types, function signatures, module ownership, and state transitions. Name the invariant each structure enforces. Trace dominant access patterns, errors, retries, and concurrent writers. Prefer a deep implementation behind a small public interface.

When alternatives materially differ, compare two candidate sketches using arena if permitted, otherwise make and compare them sequentially. Keep sketches separate from production changes. Evaluate boundary size, shared state, migration cost, and testability. Select a coherent base and incorporate only useful compatible ideas. Report the chosen interface, rejected alternative, tradeoff, and verification plan. Do not implement full prototypes when signatures and one focused experiment settle the question.
