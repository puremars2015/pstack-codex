# Autopilot full

Read [the runtime contract](../references/codex-runtime.md) first.

Establish each item, done condition, resource boundary, and explicit permission for any merge. Assign non-overlapping ownership where delegation is available. Build and verify each item at its exact head, review the artifacts, and reverify after fixes. Merge only authorized verified items, otherwise present ready PRs. Keep failures and blocked items visible; green CI alone is insufficient.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
