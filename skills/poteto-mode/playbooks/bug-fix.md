# Bug fix

Read [the runtime contract](../references/codex-runtime.md) first.

Identify intended versus observed behavior. Reproduce the defect on the affected surface. Trace the earliest violated invariant. Use tdd when a cheap regression path exists. Make the smallest root-cause correction, then rerun the reproduction and appropriate nearby checks. Report failing-before and passing-after evidence or explicitly name missing evidence.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
