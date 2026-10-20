# Babysit

Read [the runtime contract](../references/codex-runtime.md) first.

For a status question, inspect the current head, checks, conflicts, and unresolved reviews once. For an authorized repair request, reproduce actionable failures and classify review findings by evidence, then fix within scope. Recheck the new head after every change. Use bounded polling only when requested. Do not merge merely because checks pass or schedule a monitor implicitly.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
