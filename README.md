# pstack for Codex

這是 pstack 的本機 Codex 相容版本，核心工作流程與 23 個 playbook 已改寫為 Codex 工具介面。保留上游工程原則與部分獨立技能的內容。不是上游官方發行版，未宣稱每一項原版機制都已移植。

## 內容

- 24 條核心工程原則。
- 23 套已改寫為 Codex 使用方式的工作流程。
- 31 個實用技能，連同核心原則共 55 個技能。
- 技能選單說明為繁體中文；供代理執行的詳細規則主要保留英文。

## 安裝

使用有 `plugin` 子指令的 Codex CLI：

```sh
codex plugin marketplace add https://github.com/puremars2015/pstack-codex.git
codex plugin add pstack-codex@pstack-codex-repo
```

安裝後開啟新聊天。私人 repository 需要 GitHub 存取權限及可用的 Git 登入憑證。若未提供 Codex CLI，可將 repository 下載後交給 Codex，要求從本機 marketplace 安裝。

## 使用

安裝後在新聊天輸入：

```text
$pstack-codex:poteto-mode 重現這個 bug，找出根因，修正並驗證。
$pstack-codex:how 說明這個模組的資料流。
$pstack-codex:architect 比較這個 API 的兩種設計。
$pstack-codex:interrogate 審查目前 diff，只回報有證據的問題。
$pstack-codex:setup-pstack
```

預設繼承目前聊天的模型與推理設定。不需要 API key、外部模型、MCP server、Bun 或 bash。平行工作僅在目前會話允許且提供代理工具時執行；否則逐項執行並說明獨立性限制。原版手動觸發的技能保留為明確呼叫，不會自動啟用全域模式。

setup-pstack 的個人設定為 `$CODEX_HOME/pstack/config.json`，未指定 CODEX_HOME 時為 `~/.codex/pstack/config.json`。專案設定 `.agents/pstack.json` 優先。這些是技能讀取的工作流程偏好，不會改變 Codex 預設模型。

## 已移除

Cursor 指令、規則檔、自訂 agent 類型、Bugbot 與 Origin 整合、Benny／Cursor 自動化、Grok Bot UI，以及 cursor-team-kit 相依項目。不會偷偷排程、傳送訊息或自動合併。GitHub 相關工作只使用目前可用的連線或 gh，並遵守使用者授權。

## 安裝與維護

此 repository 已包含 `.agents/plugins/marketplace.json`，指向根目錄的外掛套件。使用真正的 Codex CLI；npm 上同名的 codex-cli 可能是無關工具。更新時修改來源套件、提高版本，再透過 Codex 重新安裝；不要修改快取。

檢查套件：`python scripts/validate.py`。開發驗證器需要 PyYAML 與 jsonschema，版本範圍見 scripts/requirements-dev.txt；技能執行不需要這兩個套件。決策記錄器是 Python 標準函式庫腳本，位於 `skills/show-me-your-work/scripts/log.py`。其他技能不會自動執行任何安裝或排程腳本。

## 來源與授權

上游為 [cursor/plugins 的 pstack](https://github.com/cursor/plugins/tree/main/pstack)，作者 Lauren Tan，MIT 授權。固定來源 commit、原始版本與移除範圍見 [UPSTREAM.json](UPSTREAM.json)，原授權見 [LICENSE](LICENSE)。本機改編保留來源聲明。模型多樣性、背景持續執行、UI 驗證與正式驗證皆取決於當下實際可用的工具，不會僅因安裝此套件就獲得。
