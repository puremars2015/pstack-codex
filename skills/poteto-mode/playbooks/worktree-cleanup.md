# Worktree cleanup

Read [the runtime contract](../references/codex-runtime.md) first.

Inventory with git worktree list and inspect branch, merge status, dirty and untracked files, and ownership. Report candidates before any destructive step when authorization is not specific. Prefer the host managed archive tool for managed checkouts. Resolve and verify target paths and preserve required ignored files. Never remove shared/primary checkouts or user changes incidentally.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
