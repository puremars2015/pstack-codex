---
name: create-verification-skill
description: 依現有測試與操作工具，建立能驗證真實應用行為的專案技能。
---

Read [the Codex runtime contract](../poteto-mode/references/codex-runtime.md) before executing this skill.

# Create behavioral verification

Inspect the actual application entry points, runnable environment, existing checks, and available UI/API drivers. Choose a small feature map with user action, expected observable result, data prerequisites, and cleanup. Prove one representative path on the real app before claiming a working harness.

Follow skill-creator guidance to write `.agents/skills/verify-<project>/SKILL.md` and only necessary scripts/references. Use the actual platform and installed tools, explicit environment requirements, repeatable fixtures, and safe cleanup. Distinguish browser, API, and database evidence. Do not mark a feature passed based only on compilation or a mock response. Run the resulting instructions and report any path that could not be exercised.
