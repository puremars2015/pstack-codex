# Refactoring

Read [the runtime contract](../references/codex-runtime.md) first.

State the behavioral invariant and concrete structural problem. Read all affected callers, choose a coherent target shape, and establish baseline checks. Use a small codemod when it makes a repeated migration safer. Migrate callers and remove obsolete internal APIs together. Verify externally observable behavior and inspect the diff for accidental functional changes.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
