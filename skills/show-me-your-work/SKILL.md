---
name: show-me-your-work
description: 為長時間或需要稽核的任務，記錄重要決策、替代方案、依據與目前狀態。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Decision trail

Keep a local TSV log of material decisions, alternatives rejected, evidence, and current status. Use the bundled script at scripts/log.py with an explicit path in work/ or the repository's established notes directory. Do not log secrets or bulk tool output. Commit the log only if it belongs in the requested deliverable.

```text
python <skill-directory>/scripts/log.py --path work/pstack-decisions.tsv --decision "Choose X" --evidence "Observed Y" --alternative "Rejected Z because ..." --status accepted
```

Entries are append-only in time order; supersede a decision with a new entry. Record a concrete observation or artifact reference rather than claiming certainty. Read the log before handing off a long task and report unresolved decisions.
