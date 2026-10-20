# Multi phase plan

Read [the runtime contract](../references/codex-runtime.md) first.

Write the outcome, constraints, current state, and unknowns. Define phases by independently checkable artifacts and dependency order, with named acceptance evidence and rollback considerations where relevant. Avoid disposable compatibility layers that preserve no required contract. Execute the plan only when implementation is requested and revise it when observations change the premise.

Finish with the outcome, concrete evidence, and any remaining work. Do not invent unavailable tooling or silently skip a required check.
