# Perf issue

Read [the runtime contract](../references/codex-runtime.md) first.

Identify the user-visible slow path, input scale, and environment. Establish a baseline and apply benchmark-checklist. Profile a separate run to locate the limiter. Change one hypothesis at a time. Compare equivalent builds with interleaved repeated runs and verify output correctness. Report end-to-end relevance, variability, and tradeoffs.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
