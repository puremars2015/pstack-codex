# Pause safely

Read [the runtime contract](../references/codex-runtime.md) first.

Stop scheduling new work. Safely halt or communicate a stop to owned workers if supported; do not interrupt unrelated processes. Preserve uncommitted work and record revisions, dirty files, active processes, checks, and the next step in a handoff note. Update an active goal to paused only when explicitly requested and supported. Report the recoverable state and stop.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
