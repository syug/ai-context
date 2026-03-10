# workspaces.json Google Drive同期 — マルチエージェントレビュー

**Date:** 2026-03-09
**Reviewers:** Kiro CLI, Claude Architect

## 背景

workspaces.json (当時 `~/.config/workspaces/workspaces.json`、現在 `~/Development/repos/ghq/github.com/syug/dotfiles/workspaces/workspaces.json`) がSSOT。
ローカルのみでGoogle Drive同期されていない問題の解決策を検討。

## 検討した構成: Google Drive原本 + symlink

$AI_BASE/artifacts/workspaces.json (原本) <- ~/.config/workspaces/workspaces.json (symlink)

## レビュー結果

### symlink構成のリスク (両者一致)
- GDriveマウント前のLaunchAgent起動でbridge.tsがクラッシュ（再起動毎にほぼ確実）
- hardlinkはクロスボリューム（FileProvider=別ボリューム）で不可
- writeFileSyncはsymlinkを安全にたどる。ただしatomic write(rename)はsymlinkを壊すのでNG

### Kiro CLI の見解
- 220行JSONにGDrive同期はオーバーキル
- 設定ファイルをGDriveに置く設計自体が不適切
- GDriveアプリフリーズ時にFileProvider無応答リスク
- 推奨: git管理 or ローカル原本+rsyncバックアップ

### Claude Architect の見解
- 条件付きGo（bridge.tsリトライ実装が前提）
- bridge.tsのトップレベル読み込みをmain()内に移動+リトライ必須
- bridge.shは既にフォールバック処理済みで変更不要
- LaunchAgentのThrottleInterval 10->30で起動時クラッシュループ軽減

### 代替案比較

| 方式 | メリット | デメリット | 判定 |
|------|---------|-----------|------|
| symlink | パス変更不要 | GDriveマウント依存、起動順序問題 | リスク>メリット |
| hardlink | マウント不要 | クロスボリュームで作成不可 | 不可 |
| 直接パス | シンプル | 全消費者パス変更、パス長大 | 非推奨 |
| **git管理** | バージョン管理、競合解決、オフライン完動 | 手動commit/push | **採用** |
| rsync cron | シンプルバックアップ | リアルタイム性なし | バックアップ目的なら可 |
| fswatch | リアルタイム | デーモン追加、複雑 | 複雑すぎる |

## 決定: git管理

- `~/.config/workspaces/` をgit repoにする
- private repoにpush
- 変更履歴が残る（GDriveにはない利点）
- オフラインで完全動作
- 全消費者のパス変更不要
- 同期は明示的（git push/pull）で競合なし

## 実装結果（3/10 完了）

当初計画の `~/.config/workspaces/` git化ではなく、dotfiles管理として `github.com/syug/dotfiles`（private, ghq管理下）に新リポジトリを作成。

**新パス:** `~/Development/repos/ghq/github.com/syug/dotfiles/workspaces/workspaces.json`

**更新した消費者（全4箇所）:**
1. rebuild-cmux.sh (L43)
2. bridge.ts (L41)
3. bridge.sh (L11)
4. parser.ts (L6)

**削除:** contexts.json（レガシー、全消費者が参照停止済み）
**未変更:** sesh.toml（seshがTOML直読み、手動同期継続）
