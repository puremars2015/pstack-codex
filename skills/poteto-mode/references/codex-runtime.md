# Codex runtime contract

This is a skills-only adaptation. Read this contract before executing a bundled workflow. User instructions, repository instructions, and host permissions take precedence. A skill does not grant permission to message people, merge, publish, delete data, or change unrelated configuration. Complete authorized, reversible work without unnecessary confirmation. Preserve user changes.

## Tools and models

Use tools actually exposed in this session. Use filesystem and shell tools for local work; prefer rg for discovery. Use the host plan tool when available or a short local checklist for substantive work. Use installed browser/computer skills for UI verification when available. If a capability is absent, report the specific gap and use an honest narrower check; never claim a simulated check as real execution.

Use collaboration.spawn_agent (or the host's exposed equivalent) only when delegation is permitted by the session's instructions. Workflow recommendations here do not override a host prohibition. Give each worker a complete task, exact source revision, owned files or output directory, acceptance checks, and required evidence. Agents share files; independent writable candidates need isolated directories or managed worktrees. Respect available concurrency slots and inspect artifacts yourself. Wait with the exposed wait tool; do not create user-owned chats as workers or send messages to other chats without user authorization. If delegation is unavailable, perform the passes sequentially and report that independent review was unavailable.

Default to inheriting the current chat model. Do not invent model identifiers or launch external model CLIs. A per-role model override is valid only when the user explicitly selects it and the host exposes it. A fresh pass on the same model is not a different-model panel. Model and effort overrides must use the current tool schema; do not encode effort into a model name.

## Optional configuration

Use `<repository>/.agents/pstack.json` when present; otherwise use `$CODEX_HOME/pstack/config.json` (default `~/.codex/pstack/config.json`). Do not read both as merged layers. Missing configuration means inherited model, host effort, two comparison candidates, and no background scheduling. See [config.schema.json](config.schema.json). Configuration is workflow data, not a replacement for Codex config.toml. Only setup-pstack writes it, on a setup/configuration request. Do not edit global AGENTS.md or change the user's default model.

## Boundaries and evidence

Run on the actual platform. In PowerShell use native literal-path file operations; do not assume bash, /tmp, Bun, Linux profilers, or macOS tools. Prefer Python for bundled scripts. Use work/ or a repository's established scratch directory. Never delete a checkout with user changes as incidental cleanup.

Changes invalidate affected verification. Record exact commit IDs for review and merge, and identify uncommitted edits. A green build does not prove behavior or authorize a merge. Use read-only GitHub tools or authenticated gh for inspection when available. Creating a PR may be part of a development request; merge, deployment, notifications, and recurring jobs require the user's applicable authorization. No skill silently schedules itself. Stop a loop when done, blocked by required input, explicitly stopped, or at its agreed time/cost boundary. Report the remaining work without inventing success.

## Skill resolution

Invoke bundled skills as `$pstack-codex:skill-name`, or read `../../<skill-name>/SKILL.md` from this reference's directory. From a skill entrypoint, siblings are `../<skill-name>/SKILL.md`. Load only relevant principles and playbooks. Paths are relative to the installed plugin, never to a cache version. Do not modify installed cache files; change the source package and reinstall. Use the bundled setup-pstack skill for configuration and poteto-help for workflow selection.
