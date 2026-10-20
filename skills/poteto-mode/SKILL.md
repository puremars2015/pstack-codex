---
name: poteto-mode
description: 在你指定 pstack 工作方式時，選擇適合的工程流程，完成分析、實作與驗證。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Poteto mode for Codex

Read the Codex runtime contract linked above. Identify the requested outcome and acceptance evidence, then choose the smallest matching playbook below. Keep the receiving chat in charge. Do not spawn an agent merely to run this router. Do not open a PR after a read-only task or impose a full design panel on a small edit.

Before implementation, identify the input/output data shape and affected callers. Use how for unfamiliar subsystems, architect for consequential interface choices, and interrogate when an independent adversarial review adds value. Use tdd for a cheap regression path, benchmark-checklist for measured claims, and show-me-your-work for long or auditable tasks. Read relevant principle files before applying them; do not announce principles just to fill a reply.

For multi-step work, keep a plan with observable completion checks. Execute, inspect real output, and report the result, evidence, and remaining limits. Match the user's language. Read only the playbook and supporting skills the task needs.

## Playbooks
- [investigation](playbooks/investigation.md): A read-only question about existing behavior.
- [bug-fix](playbooks/bug-fix.md): Reproduce and fix a defect.
- [perf-issue](playbooks/perf-issue.md): Improve a measured performance problem.
- [hillclimb](playbooks/hillclimb.md): Improve one metric through bounded experiments.
- [runtime-forensics](playbooks/runtime-forensics.md): Diagnose a live leak, spin, or glitch.
- [trace-forensics](playbooks/trace-forensics.md): Diagnose an existing profile or trace.
- [feature](playbooks/feature.md): Add or change behavior.
- [refactoring](playbooks/refactoring.md): Change structure while preserving behavior.
- [prototype](playbooks/prototype.md): Resolve an empirical design question cheaply.
- [visual-parity](playbooks/visual-parity.md): Match two implementations visually.
- [authoring-a-skill](playbooks/authoring-a-skill.md): Write or modify a skill.
- [eval](playbooks/eval.md): Evaluate a prompt or skill change.
- [babysit](playbooks/babysit.md): Inspect or repair PR review and CI state.
- [shipping](playbooks/shipping.md): Verify and land explicitly authorized changes.
- [autonomous-run](playbooks/autonomous-run.md): Complete a long task within agreed limits.
- [orchestrate](playbooks/orchestrate.md): Coordinate a multi-phase project.
- [autopilot-full](playbooks/autopilot-full.md): Drive authorized independent PR work to completion.
- [autopilot-stack](playbooks/autopilot-stack.md): Build a dependency-ordered PR stack for review.
- [session-pickup](playbooks/session-pickup.md): Resume work using evidence from a prior session.
- [pause-safely](playbooks/pause-safely.md): Pause at the user's explicit request.
- [multi-phase-plan](playbooks/multi-phase-plan.md): Plan verifiable dependent phases.
- [worktree-cleanup](playbooks/worktree-cleanup.md): Inspect and clean up explicitly targeted worktrees.
- [opening-a-pr](playbooks/opening-a-pr.md): Publish a reviewable PR when in scope.

## Principles
- [attack-the-premise](../principle-attack-the-premise/SKILL.md)
- [boundary-discipline](../principle-boundary-discipline/SKILL.md)
- [build-the-lever](../principle-build-the-lever/SKILL.md)
- [encode-lessons-in-structure](../principle-encode-lessons-in-structure/SKILL.md)
- [exhaust-the-design-space](../principle-exhaust-the-design-space/SKILL.md)
- [experience-first](../principle-experience-first/SKILL.md)
- [explain-the-number](../principle-explain-the-number/SKILL.md)
- [fix-root-causes](../principle-fix-root-causes/SKILL.md)
- [foundational-thinking](../principle-foundational-thinking/SKILL.md)
- [guard-the-context-window](../principle-guard-the-context-window/SKILL.md)
- [laziness-protocol](../principle-laziness-protocol/SKILL.md)
- [make-operations-idempotent](../principle-make-operations-idempotent/SKILL.md)
- [migrate-callers-then-delete-legacy-apis](../principle-migrate-callers-then-delete-legacy-apis/SKILL.md)
- [minimize-reader-load](../principle-minimize-reader-load/SKILL.md)
- [model-the-domain](../principle-model-the-domain/SKILL.md)
- [never-block-on-the-human](../principle-never-block-on-the-human/SKILL.md)
- [outcome-oriented-execution](../principle-outcome-oriented-execution/SKILL.md)
- [prove-it-works](../principle-prove-it-works/SKILL.md)
- [redesign-from-first-principles](../principle-redesign-from-first-principles/SKILL.md)
- [separate-before-serializing-shared-state](../principle-separate-before-serializing-shared-state/SKILL.md)
- [sequence-verifiable-units](../principle-sequence-verifiable-units/SKILL.md)
- [subtract-before-you-add](../principle-subtract-before-you-add/SKILL.md)
- [test-behavior-not-implementation](../principle-test-behavior-not-implementation/SKILL.md)
- [type-system-discipline](../principle-type-system-discipline/SKILL.md)
