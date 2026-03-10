# Handover Document
**Topic:** /handover スキルの継続改善（サブコマンド体系・インデックス・フィルタ・エイリアス・作業ディレクトリ・ステータス表示・コンテクスト推定・Celebrationバナー・自動保存）
**Date:** 2026-02-23（最終更新: 2026-03-10）
**Status:** 進行中

---

## 背景
`/handover` スキルは過去のAIセッションの引き継ぎドキュメント管理に使用している。従来は `/handover [keyword]` で読み込み、`/handover save [topic]` で保存という暗黙的なモード判定だったが、より明示的なサブコマンド体系が求められた。その後、リスト表示の高速化・検索性向上・作業ディレクトリ連携のための改善を段階的に実施している。

## 現在の状況

### 完了した変更（2026-02-23）
スキル定義ファイル `/Users/saitshug/.claude/skills/handover/SKILL.md` を以下のように更新:

- **コマンド体系の変更:**
  - `/handover` — 対話式でSave/List選択（デフォルト動作を維持）+ サブコマンドのリマインド表示
  - `/handover list [keyword]` — 過去トピックの検索・読み込み（旧 `/handover [keyword]`）
  - `/handover save [topic]` — handover生成・保存（変更なし）

- **モード判定ロジックの更新:**
  - `list` → 読み込みモード
  - `save` → 保存モード
  - サブコマンドなし → 対話モード（Step I1）で AskUserQuestion によるSave/List選択

- **対話モード（Step I1）の新設:**
  - AskUserQuestion でList/Saveを選択
  - 選択後に対応モードのStep 1へ遷移
  - リマインドメッセージ表示

### 完了した変更（2026-02-25）
- **`/handover XXX` ショートカット対応:** `list` / `save` 以外の引数は暗黙的にlist検索として処理
- **SKILL.md のモード判定ロジック追加・使い方セクション更新**
- **`~/.claude/settings.local.json` の更新:** `mkdir -p` を pre-approved bash に追加

### 完了した変更（2026-02-26）
Director modeとの相性問題を修正:
- **問題:** バックグラウンドagentのBash実行コンテキストからGoogle Drive CloudStorageマウントポイントへのアクセスが制限される
- **修正:** `~/.claude/CLAUDE.md` に `/handover` スキルをagent委任の例外として追加

### 完了した変更（2026-02-27 前半）

#### 1. handover.md なしディレクトリのリスト表示
- **変更:** handover.md が存在しないディレクトリも一覧に表示するよう修正（`(no handover)` マーカー付き）
- **Step R1:** ディレクトリ走査を `ls -1d` ベースに変更し、handover.md有無で分岐表示
- **Step R4:** handover.md が無い場合はファイル一覧を表示し、作成するか確認する分岐を追加
- **共通注意事項:** 「表示しない」ルールを「マーカー付きで表示する」に変更

#### 2. .index.json インデックスファイルの導入
- **ファイル:** `$AI_BASE/.index.json` を新規作成
- **内容:** 全19トピック（18件handoverあり + 1件なし）のメタデータ（dir, date, slug, hasHandover, title, status, summary, tags）
- **効果:** リスト時にGoogle Driveの各ディレクトリを走査する代わりに、1ファイル読み込みで済む（高速化）
- **Step R1 更新:** .index.json 存在時はそこからトピック一覧を取得するロジックを追加

#### 3. フィルタ機能の追加（Step R2 大幅更新）
- **`--active`** — status が「完了」以外のトピックのみ表示
- **`--tag <タグ名>`** — 指定タグを持つトピックのみ表示
- **`--recent <N>`** — 直近N日以内のトピックのみ表示（デフォルト7日）
- **キーワード検索の強化:** .index.json の tags, title, summary, slug に対してマッチ（ディレクトリ名だけでなく）

#### 4. エイリアス/ショートコードシステム
- **仕組み:** .index.json に `aliases` オブジェクトを追加。キーワードがエイリアスと完全一致する場合、対応ディレクトリに直接アクセス
- **登録済みエイリアス:** tax, parking, myer, bed, mcp, pest, cockroach, oauth, qbr, bil, fidelity, spaces, weekly, gemini, meshclaw, survey, sse, tex-sse, slack-mcp, outlook-mcp（20個）
- **Step R2 更新:** エイリアス解決ロジックを追加

#### 5. インクリメンタルインデックス更新（Step S6 新設）
- **仕組み:** `save` 実行時に .index.json の該当エントリのみ更新（全スキャン不要）
- **フロー:** .index.json読み込み → 該当dirのエントリ検索 → 更新or追加 → 上書き保存
- **抽出ルール:** title/status/summary/tagsをhandover.mdから自動抽出

#### 6. tex-survey-analysis の handover.md 作成
- 既存ディレクトリ `2026-02-25_tex-survey-analysis` にhandover.mdが未作成だったため、notesとartifactsの内容を読み込んで新規作成

### 完了した変更（2026-02-27 後半）

#### 7. Step R3: AskUserQuestion UI制限の回避
- **問題:** AskUserQuestion ツールは最大4選択肢の制限があり、20件以上のトピック全リスト表示ができなかった
- **修正:** 結果件数に応じて選択UIを切り替える4分岐ロジックを導入:
  - **5件以上:** 番号付きテキストリストを表示（AskUserQuestion不使用）。ユーザーは番号・トピック名・エイリアスを自由入力
  - **2〜4件:** AskUserQuestion で選択（4オプション制限内に収まる）
  - **1件:** 確認なしで直行（変更なし）
  - **0件:** エラーメッセージ + 全一覧をテキスト表示

#### 8. Step 0: Working Directory Detection（新設）
- **目的:** 各トピックが持つ外部作業ディレクトリ（`$AI_BASE` 外）を検知し、スマートデフォルトを提供
- **検出ロジック:**
  1. `pwd` を取得（ホームディレクトリ `/Users/saitshug` の場合はスキップ）
  2. 優先順: `.index.json` の `workdir` フィールドとマッチ → `$AI_BASE/YYYY-MM-DD_*/` パスマッチ
  3. マッチすれば `$CURRENT_TOPIC` として保持

#### 9. workdir フィールドの導入
- **`.index.json` に `workdir` オプションフィールドを追加:**
  ```json
  {
    "dir": "2026-02-26_tex-prime-video-sse-initiative",
    "workdir": "~/Library/CloudStorage/OneDrive-amazon.com/Projects/2026/TEX/Research/Prime Video",
    ...
  }
  ```
- `workdir` は `$AI_BASE` 外の実際の作業ディレクトリ（データやアーティファクトの場所）
- `~` はホームディレクトリに展開して比較
- 登録方法: `.index.json` 直接編集 or `/handover save` 時の自動提案

#### 10. $CURRENT_TOPIC と各サブコマンドの統合
- **モード判定を拡張:**
  - `/handover`（引数なし）+ `$CURRENT_TOPIC` あり → Step R4 直行（自動読み込み）
  - `/handover save`（引数なし）+ `$CURRENT_TOPIC` あり → Step S3 直行（S1/S2スキップ）
- **Step R3:** `$CURRENT_TOPIC` 設定時、該当トピックに `◀ 現在` マーカー表示
- **Step R5:** workdir 設定済みかつ現在そこにいない場合、`cd` での移動を提案
- **Step S5b（新設）:** `pwd` がホームでなく workdir 未登録なら紐付けを自動提案

#### 11. `/handover status` サブコマンドの実装
- **目的:** Step 0 の Working Directory Detection（`$CURRENT_TOPIC` 自動検出）の結果を確認する手段がなかったため、明示的にステータスを表示するサブコマンドを追加
- **SKILL.md への変更:**
  - 使い方セクションに `/handover status` 行を追加
  - モード判定セクションに `status` → ステータス表示モード（Step T1 へ）を追加
  - 新セクション「ステータス表示モード — Step T1」を新設:
    - Step 0 (Working Directory Detection) を実行して `$CURRENT_TOPIC` を判定
    - workdir マッチ / $AI_BASE マッチ / マッチなしの3パターンの表示フォーマット
    - 表示後に処理終了（他のステップには進まない）
- **動作確認:** ホームディレクトリで `/handover status` を実行 → 「なし」が正しく表示されることを確認

#### 12. `/handover status` のコンテクスト推定機能追加（Step T1b 新設）
- **目的:** pwd ベースの `$CURRENT_TOPIC` 判定だけでは、ホームディレクトリにいる時やスキルディレクトリ（`~/.claude/skills/handover/`）で作業している時にトピックを検出できなかった問題を解決
- **Step T1b「コンテクスト推定」を新設:**
  - 会話コンテクストから3種類のシグナルを収集してトピックを推定:
    1. **ファイルパス** — workdir / `$AI_BASE` パスとの一致
    2. **キーワード** — `.index.json` の tags / title / summary / slug とマッチ
    3. **ツール呼び出し** — 対象ディレクトリやファイルからの推定
  - マッチ強度を3段階で判定（強い / 中程度 / 弱い）— 弱いシグナルのみの場合は提案しない
- **`$CONTEXT_TOPIC` は表示専用:**
  - `$CURRENT_TOPIC`（pwd ベース）の動作には一切影響しない
  - あくまで `/handover status` の追加情報として表示するのみ
- **表示パターンを3ケースから4ケースに拡張:**
  1. pwd マッチあり + コンテクスト一致 → 従来通り
  2. pwd マッチなし + コンテクスト推定あり → 根拠付きで提案（`/handover {slug}` で読み込み案内）
  3. pwd マッチあり + コンテクスト別トピック → ミスマッチ通知
  4. 両方なし → 従来の「なし」表示

### 完了した変更（2026-03-01）

#### 13. `/handover history` サブコマンドとセッション履歴保持機能

- **目的:** handover.md を上書き保存するたびに、旧バージョンが失われる問題を解決。過去セッションのコンテキストを参照可能にする。
- **SKILL.md への変更:**
  - 使い方セクションに `/handover history [キーワード]` を追加
  - モード判定に `history` → 履歴モード（Step H1 へ）を追加
  - **Step S2b（新設）「旧バージョンのアーカイブ」:**
    - handover.md 上書き前に、既存バージョンの `**Date:**` から日付を抽出
    - `history/` ディレクトリに `{Date}_handover.md` として保存（同日複数回は連番）
    - 圧縮ルール: ヘッダー・アクションアイテム・判断ログは全文保持、背景は1段落、現在の状況は各サブセクション冒頭のみ
    - `<!-- archived: {ISO 8601} | original_date: {Date} | compressed: true -->` メタ行を先頭に追加
  - **履歴モード（Step H1〜H3）新設:**
    - H1: トピック特定（キーワード or $CURRENT_TOPIC or 対話選択）
    - H2: `history/` 走査・一覧表示（日付・アクションアイテム件数・判断ログ件数のサマリ付き）
    - H3: 選択されたアーカイブを読み込み・表示（圧縮済みの旨を注記）
- **ディレクトリ構造の変更:** 各トピックディレクトリに `history/` サブディレクトリが追加される（初回アーカイブ時に自動作成）

### 完了した変更（2026-03-02）
※ 旧トピック `2026-03-02_handover-save-ux-improvement` からマージ

#### 14. Celebration バナー（SKILL.md Step S7 新設）
- 保存完了時に罫線ボックス + 絵文字の大きなバナーを表示
- `🎉 HANDOVER SAVED! 🎉` + トピック名・日付・成果物数・判断ログ数
- `📌 Next:` セクションで未完了アクションアイテムを最大3件表示（忘れ防止）
- 「お疲れさまでした！閉じてOKです 🍵」で達成感 + 行動許可（UX Celebration）
- 前後に空行3行で通常テキストから視覚的に完全分離
- 失敗時のエラーバナーも設計
- 自動保存時は簡潔版バナー（Next 1件のみ表示）

#### 15. 自動保存ディレクティブ（CLAUDE.md 追加）
- `/handover` でトピック読み込み済み → 常に自動保存（やり取り回数不問）
- `$CURRENT_TOPIC` 検出済み → 常に自動保存
- トピック未設定 + Write/Edit ツール使用あり → 自動保存
- トピック未設定 + Read/Grep のみ + 5回未満 → スキップ（Quick Q&A）
- Tier 1: 終了宣言→通常版で保存、Tier 2: タスク完了→簡潔版で自動保存（提案→実行に格上げ）
- メインスレッド限定、全agent完了待ち、「保存不要」宣言でスキップ可

#### 16. マルチエージェントUXレビュー
- UXレビューと技術レビューを並行実施
- 「無応答」トリガーは削除（誤判定リスク）
- バナーデザインは視認性重視（16セッション並行のユースケース）
- Race Condition 対策（全agent完了待ち）
- `/memory` との棲み分け確認: Memory=安定パターン・好み、Handover=タスク状態・引き継ぎ

### 完了した変更（2026-03-03）

#### 17. `handover-save-ux-improvement` トピックのマージ
- 旧トピック `2026-03-02_handover-save-ux-improvement` を本トピックに統合
- ディレクトリ削除、.index.json からエントリ除去、エイリアス再マッピング
- 旧バージョンを `history/2026-03-01_handover.md` にアーカイブ

#### 18. Celebration バナーのリデザイン（Step S7 全面改訂）
- **問題:** 右ボーダー（┃ ┓ ┛）が日本語・絵文字の可変幅でずれる
- **解決:** マルチエージェントブレスト（Minimalist / Bold-Expressive / Practical-Engineering の3エージェント並行）で9案を比較検討
- **採用:** Left Accent Bar スタイル（┃ のみ左側に縦線、右ボーダーなし）
- **追加変更:**
  - `🎉` → `✨` に変更（前後スペース不均等問題も解消）
  - `{dir-name}`（英語スラッグ）と `{topic-name}`（日本語タイトル）を分離表示（📂 + 🏷️）
  - 内部セパレーター ━━━ を Next: の前に移動（メタ情報とアクションの視覚的分離）
  - 通常版・簡潔版・失敗版の3バリアント全て更新

#### 19. バナーヘッダーの最終調整
- `✨ HANDOVER SAVED` → サンドイッチスタイル（上下セパレーター挟み）に変更
- `✅ HANDOVER SAVED ✨` — 左に完了感（✅）、右に祝い（✨）の非対称デザイン
- 全行の頭揃え: `┃  ` + 絵文字で統一（✅と📂の左端が揃う）

#### 20. 簡潔版バナーのリデザイン
- 全行 `┃  ` 2スペースインデント + 絵文字先頭で頭揃え
- サンドイッチヘッダー付き（通常版と統一感）
- `🍵 お疲れさまでした！閉じてOKです` を削除（簡潔版は迅速クローズ用）
- `📂 {dir-name} — {topic-name}` で1行にまとめ

#### 21. 自動保存 Tier 1/2 の動作変更（CLAUDE.md 更新）
- **Tier 1:** 終了宣言 → 通常版バナーで保存（`/handover save` と同等に格上げ）
- **Tier 2:** タスク完了後 → 簡潔版で自動保存（提案→実行に格上げ）

#### 22. ARGUMENTS 引数解釈バグの修正
- **問題:** `/handover skill` と入力 → ARGUMENTS: "skill" を「引数なし」と誤判定 → 対話モードに入ってしまう
- **原因:** 一度「`skill` はデフォルト値だから引数なし扱い」というサニタイズルールを追加してしまった（誤修正）
- **修正:** サニタイズルールを削除し、ARGUMENTS に値がある場合は全て有効なキーワードとして扱うルールに変更

### 完了した変更（2026-03-10）

#### 23. $AI_BASE パス移行（Google Drive → Git リポジトリ）
- **変更:** ai-context フォルダを Google Drive (`~/Library/CloudStorage/GoogleDrive-syugo3hz@gmail.com/My Drive/.ai/`) から git リポジトリ (`~/Development/repos/ghq/github.com/syug/ai-context/`) に移行
- **更新ファイル:**
  - `~/.claude/CLAUDE.md` — ベースパス更新 + Git auto-push permission 追加
  - `~/.claude/skills/handover/SKILL.md` — $AI_BASE パス更新 + Step S6b（Git Commit & Push）追加
  - `~/.claude/settings.local.json` — 6箇所のパス更新

#### 24. Git 自動 Commit & Push（Step S6b 新設）
- **目的:** handover save 完了時に自動で git commit → push する
- **SKILL.md に Step S6b を追加:**
  - Step S6（インデックス更新）と Step S7（Celebration バナー）の間に配置
  - `git add` で handover.md, .index.json, history/ をステージ
  - コミットメッセージ: 新規 `new: {slug}` / 更新 `save: {slug}`
  - `git push origin main`（SSH経由）
  - push 失敗時はエラー表示しつつ続行
- **CLAUDE.md に auto-push permission を追加:**
  - ai-context リポジトリに限り git commit + push をユーザー確認なしで自動実行

#### 25. fzf ファジー検索機能（`ho` コマンド）
- **目的:** ターミナルから GHQ ライクに handover トピックをファジー検索・ナビゲート
- **設計:** Fish function `ho` → jq で .index.json パース → fzf (preview 付き) → cd
- **プラン:** `notes/fzf-topic-search-plan.md` に詳細記載
- **ステータス:** 実装中

## 成果物一覧
```
2026-02-23_handover-skill-update/
├── handover.md          ← このファイル
├── artifacts/           （なし）
└── notes/
    └── fzf-topic-search-plan.md
```

関連外部ファイル:
- `~/.config/fish/functions/ho.fish` — fzf ファジー検索 fish function

変更対象ファイル:
- `/Users/saitshug/.claude/skills/handover/SKILL.md` — スキル定義（直接編集済み）
- `$AI_BASE/.index.json` — トピックインデックス（aliases + workdir フィールド追加）
- `$AI_BASE/2026-02-25_tex-survey-analysis/handover.md` — 新規作成
- `~/.claude/settings.local.json` — pre-approved bash コマンド設定
- `~/.claude/CLAUDE.md` — Director mode例外設定 + 自動保存ディレクティブ

## アクションアイテム

| # | 期限 | アクション | ステータス |
|---|------|-----------|-----------|
| 1 | — | スキル定義ファイルの更新（サブコマンド体系） | 完了（2026-02-23） |
| 2 | — | ショートカット対応・モード判定追加・設定更新 | 完了（2026-02-25） |
| 3 | — | Director modeとの相性問題修正（CLAUDE.md例外追加） | 完了（2026-02-26） |
| 4 | — | handover.md なしディレクトリのリスト表示対応 | 完了（2026-02-27） |
| 5 | — | .index.json インデックスファイル導入 | 完了（2026-02-27） |
| 6 | — | フィルタ機能（--active, --tag, --recent）追加 | 完了（2026-02-27） |
| 7 | — | エイリアスシステム導入 | 完了（2026-02-27） |
| 8 | — | インクリメンタルインデックス更新（Step S6）追加 | 完了（2026-02-27） |
| 9 | — | tex-survey-analysis の handover.md 作成 | 完了（2026-02-27） |
| 10 | — | Step R3: AskUserQuestion UI制限の回避（件数別分岐） | 完了（2026-02-27） |
| 11 | — | Step 0: Working Directory Detection 新設 | 完了（2026-02-27） |
| 12 | — | workdir フィールド導入・$CURRENT_TOPIC 統合 | 完了（2026-02-27） |
| 13 | — | `/handover status` サブコマンドの実装 | 完了（2026-02-27） |
| 14 | — | `/handover status` コンテクスト推定機能（Step T1b）追加 | 完了（2026-02-27） |
| 15 | — | 既存トピックに workdir を登録する | 未着手（必要に応じて順次登録） |
| 16 | — | workdir 検出の実環境テスト（トピックディレクトリ内でhandover実行） | 未着手 |
| 17 | — | `/handover status` でスキルディレクトリ自体（`~/.claude/skills/handover/`）にいる時も検出できるようにする | 解決済み（コンテクスト推定で対応） |
| 18 | — | `/handover history` サブコマンドとセッション履歴保持（Step S2b + H1〜H3） | 完了（2026-03-01） |
| 19 | — | history 機能の実環境テスト（実際にsave→アーカイブ生成を確認） | 未着手 |
| 20 | — | Celebration バナー（Step S7）の実装 | 完了（2026-03-02） |
| 21 | — | 自動保存ディレクティブ（CLAUDE.md）の実装 | 完了（2026-03-02） |
| 22 | — | Celebration バナーの実表示を確認 | 未完了 |
| 23 | — | 自動保存の Tier 1 トリガーの精度を検証 | 未完了 |
| 24 | — | `handover-save-ux-improvement` トピックのマージ | 完了（2026-03-03） |
| 25 | — | Celebration バナーのリデザイン（Left Accent Bar） | 完了（2026-03-03） |
| 26 | — | バナーヘッダー最終調整（✅✨ + サンドイッチ + 頭揃え） | 完了（2026-03-03） |
| 27 | — | 簡潔版バナーのリデザイン（頭揃え + お疲れさま削除） | 完了（2026-03-03） |
| 28 | — | Tier 1/2 自動保存の動作変更（終了宣言→通常版、タスク完了→簡潔版実行） | 完了（2026-03-03） |
| 29 | — | ARGUMENTS 引数解釈バグ修正（"skill" を引数なしと誤判定する問題） | 完了（2026-03-03） |
| 30 | — | $AI_BASE パス移行（Google Drive → Git） | 完了（2026-03-10） |
| 31 | — | Git auto-commit & push（Step S6b）SKILL.md追加 | 完了（2026-03-10） |
| 32 | — | fzf ファジー検索 `ho` コマンドの実装 | 進行中 |
| 33 | — | Step S6b の実環境テスト（実際にsave→commit→push） | 未着手 |

## 重要な判断ログ

1. **デフォルト動作の維持（2026-02-23）**: 引数なしは対話式でSave/List選択する従来の動線を維持。
2. **リマインド表示（2026-02-23）**: 対話モード利用時にサブコマンドの存在をリマインド。
3. **暗黙的listショートカットの追加（2026-02-25）**: `/handover XXX` で即座に過去トピックを検索可能に。
4. **Director mode例外化（2026-02-26）**: スキル自体は正常動作、問題はDirector modeの委任にあるため、最小限の変更としてCLAUDE.mdに例外ルールを追加。
5. **handover.md なしも表示（2026-02-27）**: 成果物はあるがhandover.mdが未作成のディレクトリが発見しにくかった問題を解消。
6. **.index.json 導入（2026-02-27）**: Google Driveマウント上の各ディレクトリファイル存在チェックが遅いため、メタデータを1ファイルに集約。Readツール1回でリスト表示可能に。
7. **エイリアスはユーザーが手動追加可能（2026-02-27）**: .index.json のaliasesフィールドはユーザーが直接編集して追加できる設計。save時の自動登録は意図的に見送り（不要なエイリアスが増えるのを防止）。
8. **フィルタは.index.json依存（2026-02-27）**: --active/--tag/--recentは.index.jsonが存在する場合のみ有効。存在しない場合は従来のキーワード検索にフォールバック。
9. **sub-agentのGoogle Drive書き込み権限問題（2026-02-27）**: bypassPermissionsモードのsub-agentでもGoogle Driveパスへの書き込みが拒否される事象が繰り返し発生。最終的にメインスレッドから直接Write/Editで対応した。agentからの書き込みが必要な場合はローカルパスを使う等の回避策が必要。
10. **AskUserQuestion は最大4選択肢（2026-02-27）**: 全リスト表示にはテキスト表示、少数結果にはAskUserQuestionという件数別分岐で解決。
11. **workdir はpwd検出 + ホーム除外（2026-02-27）**: 起動時のpwdがほぼ常にホームディレクトリなので、ホームはマッチ対象から除外。workdir登録はsave時にpwdがホーム以外なら自動提案する設計。
12. **$CURRENT_TOPIC は明示引数に劣後（2026-02-27）**: 引数ありの場合は常にそちらを優先し、$CURRENT_TOPICはスマートデフォルトとしてのみ機能。既存動作を壊さない。
13. **statusサブコマンドは表示のみで終了（2026-02-27）**: `/handover status` は Step 0 の検出結果を表示して処理終了。他のステップ（save/list）には遷移しない。検出結果の確認専用のデバッグ的サブコマンドとして設計。
15. **セッション履歴は圧縮アーカイブで保持（2026-03-01）**: 完全な生ログは `.jsonl` に残るため、handover アーカイブは圧縮（背景1段落、状況はヘッダー+冒頭のみ）で十分と判断。アクションアイテムと判断ログは意思決定の記録として全文保持。
16. **sub-agentのWrite停止問題（2026-03-01）**: 大きなファイル全文書き換え（Write）をsub-agentに任せると出力生成中にフリーズする事象が再発。メインスレッドからEdit（差分更新）で対応するのが安定。
14. **$CONTEXT_TOPIC は表示専用で $CURRENT_TOPIC とは分離（2026-02-27）**: コンテクスト推定結果（`$CONTEXT_TOPIC`）は `$CURRENT_TOPIC`（pwd ベース）の動作に影響を与えない設計とした。理由: (a) 会話コンテクストからの推定は確実性が低く、暗黙的にsave先やlist対象を変えるとユーザーの意図と乖離するリスクがある。(b) pwd ベースの判定は「今いる場所」という明確な根拠があり、コンテクスト推定は「話題にしているかもしれないもの」という推測に過ぎない。(c) 将来的にユーザーが明示的に `$CONTEXT_TOPIC` を採用する操作（`/handover {slug}` で読み込み）を案内することで、ユーザーの意思決定を介在させる。
17. **バナーの視認性優先（2026-03-02）**: 16セッション並行の実ユースケースでは視認性が最優先。UXレビューの「過剰」指摘はシングルセッション前提だったため却下。罫線ボーダーに変更。
18. **UX Celebration の導入（2026-03-02）**: 「お疲れさまでした！🍵」と成果物数の可視化で達成感を演出。保存が義務作業にならないための行動設計。
19. **自動保存のQuick Q&Aスキップ（2026-03-02）**: `/handover` でトピック読み込み済みの場合は短いセッションでも保存すべきと判断。明示的にコンテキストを引き継いだセッション = 必ず保存。
20. **Next Steps をバナーに含める（2026-03-02）**: ユーザーが「すぐ忘れる」問題を解決。未完了アクションアイテムを最大3件表示。
21. **Memory vs Handover の棲み分け（2026-03-02）**: Memory は「パターン・好み」、Handover は「タスク状態・引き継ぎ」で目的が異なる。両方必要。
22. **右ボーダー廃止（2026-03-03）**: モノスペースフォントでも日本語・絵文字の文字幅が不均一なため、右側のボーダーは構造的に位置合わせ不可能。左アクセントバーのみで十分な視覚的分離が得られると全3エージェントが一致。
23. **マルチエージェントブレストの有効性（2026-03-03）**: Minimalist/Bold/Practicalの3視点から9案を出し、共通パターン（右ボーダー不要）を発見。単一視点では出にくい「Left Accent Bar」デザインが最終採用。
24. **✅✨ の非対称デザイン（2026-03-03）**: ✅（完了感）と✨（祝い）は意味が違うので非対称でOK。✅✨隣接は詰まるのでスペース挟む。
25. **簡潔版から「お疲れさまでした」削除（2026-03-03）**: 簡潔版はタスク完了後のチェックポイント用。セッション終了ではないので「閉じてOKです」は不適切。
26. **Tier 1/2 の役割変更（2026-03-03）**: 終了宣言は手動saveと同等（通常版）。タスク完了は自動チェックポイント（簡潔版）。提案→実行に格上げしたのは、ユーザーが毎回「はい」と答えるだけの無意味な確認を排除するため。
27. **ARGUMENTS サニタイズは不要（2026-03-03）**: 「`skill` をデフォルト値として除外」するルールは逆効果。ユーザーが `/handover skill` と入力して "skill" を検索したいケースを壊す。ARGUMENTS は常に額面通りに受け取るべき。
28. **Google Drive → Git 移行（2026-03-10）**: Google Drive のマウントポイントはバックグラウンドagentからのアクセスが不安定で、bypassPermissionsでもWrite/Bashが拒否される事象が繰り返し発生していた。git リポジトリに移行することで: (a) agent 権限問題を根本解決、(b) 変更履歴を git で自然に管理、(c) push で複数マシン間同期が可能に。
29. **auto-push は ai-context リポジトリ限定（2026-03-10）**: CLAUDE.md の通常ルールでは git push はユーザー確認必須。ai-context は handover 専用リポジトリで破壊リスクが低いため、このディレクトリに限り自動 push を許可した。
30. **fzf 検索は fish function として独立（2026-03-10）**: `/handover` スキル内ではなく、standalone の fish function `ho` として実装。理由: (a) Claude Code 外のターミナルでも使える、(b) fzf の対話UIはClaude Code内では動かない、(c) ghq + fzf と同じパターンで馴染みやすい。
