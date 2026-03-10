# workspaces.json Single Source of Truth 移行 (2026-03-09)

## 背景

WS名の定義が5箇所に分散（spaces.md, rebuild-cmux.sh, bridge.ts, contexts.json, sesh.toml）。
相互参照なし、名前不整合9件（WS12は3-way不整合）。一元化が必要と判断。

## 成果

`~/.config/workspaces/workspaces.json` を Single Source of Truth として全消費者を移行。
**→ 3/10にdotfilesリポジトリ (`~/Development/repos/ghq/github.com/syug/dotfiles/workspaces/workspaces.json`) に移行完了。**

### workspaces.json のスキーマ

```json
{
  "version": 1,
  "updated": "2026-03-09",
  "workspaces": [{
    "number": 1,
    "icon": "📊",
    "slackEmoji": ":bar_chart:",
    "name": "確定申告",
    "description": "青色申告・税務関連",
    "status": "常駐",
    "tabs": 1,
    "chromePatterns": ["確定申告", "freee", "jobcan", "青色申告"],
    "sessions": [{ "name": "1-1", "path": "~", "command": "claude" }]
  }]
}
```

### 消費者の移行

| 消費者 | ファイル | 変更内容 |
|--------|---------|---------|
| rebuild-cmux.sh | ~/Development/claude-slack-bridge/ | jqでJSON読み取り、ハードコード廃止 |
| bridge.ts | ~/Development/claude-slack-bridge/src/ | JSON.parseでWS_NAMES動的生成 |
| bridge.sh | ~/.config/project-focus/ | python3でJSON読み取り + 番号優先マッチ修正 |
| Raycast Extension | ~/raycast-extensions/spaces-manager/ | Markdownパーサー廃止→JSON CRUD |
| sesh.toml | ~/.config/sesh/ | 対象外（seshがTOML直読み要求） |

### 修正したバグ

1. **bridge.sh部分一致の誤マッチ**: `13pes-1`→core=`pes`がWS2 "Pest Control"に誤マッチ。番号優先マッチで解決。
2. **Raycast parser.tsのハードコードパス**: preference値を使わずL4でパスハードコード。getPreferenceValues()に修正。

### 名前の統一

短縮名（cmux/bridge用）と詳細名（description）を分離:
- `name`: 短縮名（cmuxタイトル、Slackメッセージ用）
- `description`: 詳細説明（Raycast UI表示用）

## 旧ファイル

- ~~`~/.config/project-focus/contexts.json`~~ — 削除済み（3/10、全消費者がworkspaces.json参照に移行完了）
- `$AI_BASE/2026-02-23_productivity-improvement-tools/artifacts/spaces.md` — 旧Raycastデータ（バックアップ）
