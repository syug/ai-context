# Handover Document
**Topic:** MeshClaw（個人AIエージェント）のセットアップ・導入
**Date:** 2026-02-25
**Status:** 完了

---

## 背景
MeshClawはAmazon社内エンジニア向けの個人AIエージェント。kiro-cli + builder-mcpを使い、チャット・タスク自動化・cron・サブエージェント等を提供する。CLI (`meshclaw`) とWebダッシュボード (`localhost:7777`) の2つのインターフェースを持つ。

bolichenが開発。Wiki: https://w.amazon.com/bin/view/Users/bolichen/MeshClaw/

## 現在の状況

### ローカルMac（fish shell） — セットアップ完了
- Brazil workspace: `/Users/saitshug/Development/repos/brazil-ws/MeshClaw/src/MeshClaw`
- `bash setup.sh` で初期セットアップ完了（toolbox, kiro-cli, builder-mcp, brazil-build等）
- fishのPATH設定済み: `fish_add_path .../MeshClaw/src/MeshClaw/bin`
- workspace: `~/.meshclaw/workspace`
- `meshclaw setup` 完了
- **注意**: `source setup.sh` はfish非対応。`bash setup.sh` で実行する必要がある

### Cloud Desktop — セットアップ完了
- **ホスト名**: `dev-dsk-saitshug-2a-284406f6.us-west-2.amazon.com`
- OS: Amazon Linux 2 x86_64, リージョン: us-west-2
- Brazil workspace: `/home/saitshug/MeshClaw/src/MeshClaw`
- workspace: `/home/saitshug/workplace/meshclaw-workspace`（デフォルト）
- kiro-cli: Pro license でログイン済み（Start URL: `https://amzn.awsapps.com/start`, Region: `us-east-1`）
- ダッシュボード動作確認済み
- デフォルトシェルを bash に変更済み（`sudo usermod -s /bin/bash saitshug`）
- `~/.bashrc` に `export TERM=xterm-256color` 追加済み
- カーネルアップデート完了（`sudo reboot` 実施済み）

#### Cloud Desktop 起動手順
1. SSHセッション1（Gateway起動用）:
   ```bash
   ssh dev-dsk-saitshug-2a-284406f6.us-west-2.amazon.com
   cd ~/MeshClaw/src/MeshClaw && meshclaw gateway
   ```
2. ローカルMacからSSHトンネル:
   ```fish
   ssh -N -L 7778:localhost:7777 dev-dsk-saitshug-2a-284406f6.us-west-2.amazon.com
   ```
3. ブラウザ: `http://localhost:7778`

#### Cloud Desktop 環境メモ
- デフォルトシェル: bash に変更済み（`echo 'exec bash --login' >> ~/.zshrc`）。`usermod` は LDAP/NIS でログイン時にリセットされるため `.zshrc` で対応。
- TERM: `~/.bashrc` と `~/.zshrc` で `xterm-256color` に設定済み（Ghostty対策）
- PATH: `~/.toolbox/bin` は toolbox インストール時に `.bashrc` に追加済み
- リモートURLは直接アクセス不可 → SSHトンネル必須

## 成果物一覧
```
artifacts/
├── meshclaw-setup-guide-en.md   # 英語セットアップガイド
└── meshclaw-setup-guide-ja.md   # 日本語セットアップガイド
```

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | — | ローカルMacセットアップ | ✅ 完了 |
| 2 | — | Cloud Desktopセットアップ | ✅ 完了 |
| 3 | — | ダッシュボードアクセス確認 | ✅ 完了（SSHトンネル経由） |
| 4 | — | セットアップガイド作成（英語・日本語） | ✅ 完了 |
| 5 | — | Cloud Desktop カーネルアップデート | ✅ 完了 |
| 6 | — | Cloud Desktop デフォルトシェルをbashに変更 | ✅ 完了 |
| 7 | — | ローカルMac `meshclaw gateway` 動作確認 | 未確認 |

## 重要な判断ログ

- **workspace pathにクラウドストレージを使わない**: MeshClawはSQLite (FTS5)・JSONL・PIDファイルに頻繁書き込みするため、OneDrive/Google Driveの同期がファイルロック競合やデータ破損を起こすリスクがある。ローカルMacは `~/.meshclaw/workspace`、Cloud Desktopはデフォルト `/home/saitshug/workplace/meshclaw-workspace` を選択。
- **fish shell対応（ローカルMac）**: setup.shはbash/POSIX前提。fishでは `bash setup.sh` で実行し、PATH追加は `fish_add_path` を使う。`.bashrc`/`.zshrc` への自動追加はfishには効かない。
- **Cloud Desktopのシェルをbashに変更**: デフォルトがzshだったが、`.bashrc` に `shopt`（bash専用）があるためエラーが出る。`sudo usermod -s /bin/bash` はローカル `/etc/passwd` を変更するが、Cloud Desktop は LDAP/NIS からユーザー情報を取得するためログイン時にリセットされる。恒久対策として `echo 'exec bash --login' >> ~/.zshrc` で zsh 起動時に即 bash へ切り替える方式を採用。
- **Cloud Desktop の `chsh` 不在**: Amazon Linux 2 には `chsh` がインストールされていない。`usermod` も LDAP 環境では永続しない。
- **Cloud Desktopのターミナル**: ローカルGhosttyからSSH接続すると `TERM=xterm-ghostty` が渡されるが、Cloud Desktop側にterminfo定義がない。`~/.bashrc` に `export TERM=xterm-256color` を追加して恒久対応。
- **Cloud Desktopダッシュボードへのアクセス**: リモートURL (`http://<hostname>:7777`) は直接アクセスできない。SSHトンネル (`ssh -N -L 7778:localhost:7777`) 経由で `http://localhost:7778` からアクセスする。ポート7777はローカルMacのMeshClawと競合する可能性があるため7778を使用。
- **kiro-cli ライセンス**: Amazon社員は「Use with Pro license」を選択する（Builder IDではない）。Start URL: `https://amzn.awsapps.com/start`, Region: `us-east-1`。
- **SSH鍵**: Cloud Desktopに `~/.ssh/id_ecdsa` がないとgit.amazon.comへの接続が `Permission denied` になる。`ssh-keygen -t ecdsa -f ~/.ssh/id_ecdsa -N ""` → `mwinit -o` で解決。
- **builder-mcp の追加**: setup.sh で自動インストールされなかった場合、`aim mcp install builder-mcp` で手動インストール。ダッシュボードの Auto-Sync または Gateway 再起動で反映される。
