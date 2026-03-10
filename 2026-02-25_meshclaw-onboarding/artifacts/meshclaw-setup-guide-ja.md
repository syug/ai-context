# MeshClaw セットアップガイド

Amazon ビルダー向けパーソナルAIエージェント。Wiki: https://w.amazon.com/bin/view/Users/bolichen/MeshClaw/

## 前提条件

- Brazil CLI (`brazil`)
- `kiro-cli` が PATH に入っていること
- 有効な Midway セッション (`mwinit -o`)

---

## パターンA: Cloud Desktop（推奨）

### 1. Cloud Desktop に SSH 接続

```bash
ssh dev-dsk-<alias>-<id>.<region>.amazon.com
```

**Ghostty ユーザー**: `tput: unknown terminal "xterm-ghostty"` エラーが出る場合:
```bash
export TERM=xterm-256color
```

### 2. デフォルトシェルを bash に変更（初回のみ）

Cloud Desktop のデフォルトが zsh の場合、`.bashrc` の bash 専用コマンド（`shopt`）でエラーが出る。

> **注意**: `sudo usermod -s /bin/bash` は永続しない — Cloud Desktop は LDAP/NIS を使っており、ログイン時に `/etc/passwd` がリセットされる。`chsh` も Amazon Linux 2 にはない。

恒久対策 — ログイン時に自動で bash に切り替え:

```bash
echo 'exec bash --login' >> ~/.zshrc
```

Ghostty ターミナル互換性も両シェルに設定（初回のみ）:

```bash
echo 'export TERM=xterm-256color' >> ~/.bashrc
echo 'export TERM=xterm-256color' >> ~/.zshrc
source ~/.bashrc
```

再接続して bash が有効になっていることを確認。

### 3. Midway認証 + ツールの確認

```bash
mwinit -o
```

`brazil` コマンドが見つからない場合:
```bash
# Builder Toolbox をインストール
curl -s https://toolbox.corp.amazon.com/install.sh | bash
export PATH="$HOME/.toolbox/bin:$PATH"

# Brazil CLI をインストール
toolbox install brazilcli
```

git clone で `Permission denied` エラーが出る場合:
```bash
# SSH鍵を生成（git.amazon.com 接続に必要）
ssh-keygen -t ecdsa -f ~/.ssh/id_ecdsa -N ""
mwinit -o
```

### 4. セットアップ & 起動

```bash
brazil ws create -n MeshClaw && cd MeshClaw && brazil ws use -p MeshClaw -vs live && cd src/MeshClaw && source setup.sh && meshclaw gateway
```

`setup.sh` が対話的に以下を実行:
1. Midway 認証の確認/更新
2. toolbox 依存のインストール（kiro-cli, aim, node20）
3. kiro-cli SSO ログイン（ブラウザが開く）
4. MCP サーバーのインストール（builder-mcp, ai-community-slack-mcp）
5. `brazil-build` 実行
6. `bin/` を PATH に追加
7. エージェント設定

**kiro-cli ログイン**: プロンプトで **「Use with Pro license」を選択**（Builder ID ではない）。
- Start URL: `https://amzn.awsapps.com/start`
- Region: `us-east-1`

間違えて Builder ID を選んだ場合、後から修正可能:
```bash
kiro-cli logout && kiro-cli login
```

### 5. ダッシュボードにアクセス

Gateway 起動時に2つの URL が表示される:
- `http://localhost:7777` — Cloud Desktop 内ブラウザ用
- `http://<hostname>:7777` — 直接アクセスできない場合あり

**ノートPC のブラウザからアクセスするには SSH トンネルを使う:**

ターミナル1（Gateway — ステップ4で起動済み）

ターミナル2（トンネル — ローカルマシンの新しいタブ）:
```bash
ssh -N -L 7778:localhost:7777 dev-dsk-<alias>-<id>.<region>.amazon.com
```

ブラウザで:
```
http://localhost:7778
```

> ローカルにも MeshClaw をインストールしている場合、ポート7777が競合するため7778を使用。

### 6. 次回以降の起動手順

```bash
# ターミナル1: SSH + Gateway（bash + TERM は設定済み）
ssh dev-dsk-<alias>-<id>.<region>.amazon.com
cd ~/MeshClaw/src/MeshClaw && meshclaw gateway

# ターミナル2: SSHトンネル（ローカルマシン）
ssh -N -L 7778:localhost:7777 dev-dsk-<alias>-<id>.<region>.amazon.com

# ブラウザ
http://localhost:7778
```

### 7. 動作確認

```bash
meshclaw doctor    # 依存関係・設定・接続をチェック
meshclaw status    # 稼働中の Gateway の統計情報
```

---

## パターンB: macOS（ローカル）

### 1. セットアップ（setup.sh は bash 必須）

```bash
brazil ws create -n MeshClaw && cd MeshClaw && brazil ws use -p MeshClaw -vs live && cd src/MeshClaw && bash setup.sh
```

> **注意**: `source setup.sh` ではなく `bash setup.sh` を使うこと。fish などの非 POSIX シェルでは動作しない。

### 2. PATH を追加

**fish shell の場合**:
```fish
fish_add_path /path/to/MeshClaw/src/MeshClaw/bin
```

**bash/zsh の場合**: `setup.sh` が `.bashrc`/`.zshrc` への追加を自動で提案してくれる。

### 3. ワークスペースの設定

プロンプトで workspace path を聞かれたら、**ローカル**ディレクトリを指定:
```
~/.meshclaw/workspace
```

> **クラウド同期ディレクトリは使わないこと**（OneDrive, Google Drive）— MeshClaw は SQLite/JSONL/PID ファイルに頻繁に書き込むため、同期競合やデータ破損のリスクがある。

### 4. kiro-cli ログイン

プロンプトで **「Use with Pro license」を選択**:
- Start URL: `https://amzn.awsapps.com/start`
- Region: `us-east-1`

### 5. 起動

```bash
meshclaw gateway
```

ダッシュボード: `http://localhost:7777` または `http://mesh.claw:7777`（`meshclaw setup` 実行後）

---

## トラブルシューティング

| 問題 | 解決策 |
|------|--------|
| fish で `source setup.sh` が失敗する | `bash setup.sh` を使う |
| `tput: unknown terminal "xterm-ghostty"` | `export TERM=xterm-256color` |
| `brazil: command not found` | `export PATH="$HOME/.toolbox/bin:$PATH"` |
| git clone で `Permission denied` | SSH鍵を生成: `ssh-keygen -t ecdsa -f ~/.ssh/id_ecdsa -N ""` → `mwinit -o` |
| zsh で `.bashrc` の shopt エラー | `echo 'exec bash --login' >> ~/.zshrc` で再ログイン（`usermod` は LDAP でリセットされる、AL2に`chsh`はない） |
| リモートダッシュボード URL にアクセスできない | SSHトンネル: `ssh -N -L 7778:localhost:7777 <host>` → `http://localhost:7778` |
| kiro-cli 再ログイン後に `ACP init timed out` | Gateway を再起動: Ctrl+C → `meshclaw gateway` |
| kiro-cli で間違ったライセンスを選んだ | `kiro-cli logout && kiro-cli login` → 「Use with Pro license」を選択 |
| Cloud Desktop のカーネルアップデート通知 | MeshClaw セットアップ後で OK: `sudo reboot` |
| MCP サーバーに builder-mcp がない | `aim mcp install builder-mcp` → Auto-Sync または Gateway 再起動 |
| SSH 越しに Delete キーが効かない | `export TERM=xterm-256color`（`.bashrc` と `.zshrc` に追加して永続化） |

---

## 自動アップデート

MeshClaw は Gateway 再起動時に自動更新される。手動の場合:

```bash
meshclaw update    # git pull + rebuild
```

## よく使うコマンド

```bash
meshclaw chat              # 対話 REPL
meshclaw chat -m "message" # ワンショット
meshclaw doctor            # ヘルスチェック
meshclaw status            # ランタイム統計
meshclaw cron list         # スケジュール済みジョブ
meshclaw learn list        # 学習済みの設定
```
