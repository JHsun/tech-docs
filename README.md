# AI Report Hub

由 Claude AI 產製的 HTML 分析報告彙整平台，託管於 GitHub Pages。

## 架構

```
tech-docs/
├── index.html                          ← 自動產生的索引頁（支援分組/列表/搜尋/深淺色主題）
├── update_index.py                     ← 索引產生器（遞迴掃描子目錄，自動分配色標）
├── CLAUDE.md                           ← Claude Code 專案記憶
├── reports/
│   ├── claude-code-quickstart/         ← Claude Code 速查表系列 (8 篇)
│   ├── etcd-quickstart/                ← etcd 速查表系列 (5 篇)
│   ├── linux-cheat-sheet/              ← Linux 工具教學 (3 篇)
│   ├── playwright-cheat-sheet/         ← Playwright 速查表系列 (13 篇)
│   ├── postgresql-quickstart/          ← PostgreSQL 18 速查表系列 (10 篇)
│   ├── redis-cheat-sheet/              ← Redis 速查表系列 (8 篇)
│   └── redmine-cheat-sheet/            ← Redmine 速查表系列 (9 篇)
├── .github/workflows/update-index.yml  ← 自動更新索引的 CI
└── README.md
```

## 使用方式

在 Claude Desktop（已設定 GitHub MCP）中，直接說：

> 幫我寫一份關於 XX 的分析報告，存到 `JHsun/tech-docs` repo 的 `reports/主題/YYYY-MM-DD_slug.html`

例如：
- `reports/claude-code-quickstart/01-project-architecture.html`
- `reports/etcd-quickstart/etcd-cheatsheet-1-overview-commands.html`
- `reports/postgresql-quickstart/pg18-cheatsheet-01-sql-syntax-ddl.html`

Claude 會自動產製 HTML 並推送到 repo，GitHub Actions 會自動重建索引頁。

## 目錄結構規則

- `reports/` 根目錄的檔案歸入「其他」分類
- `reports/子目錄/` 下的檔案歸入該子目錄名稱的分類
- 子目錄名稱即為分類名稱，常見後綴 `-quickstart`、`-cheat-sheet` 會在顯示時自動去除

## 檔案命名規則

分組檢視按檔名**正序**排列，因此檔名前綴決定顯示順序。

### 格式

```
[NN]-[topic-slug].html              ← 通用格式
[prefix]-[NN]-[topic-slug].html     ← 帶系列前綴
```

### 規則

| 規則 | 說明 | 範例 |
|------|------|------|
| 零填充兩位數 | 確保 1~99 正確排序 | `01-`, `02-`, `10-` |
| 補充篇用字母後綴 | 插入在原編號之後 | `02b-commands-complete.html` |
| 帶系列前綴 | 同分類內保持一致 | `pg18-cheatsheet-01-sql-syntax-ddl.html` |
| 避免純描述名 | 無編號會導致排序不可控 | ~~`awk-tutorial.html`~~ → `02-awk-tutorial.html` |

### 各分類範例

```
claude-code-quickstart/   01-project-architecture.html
                          02-cli-commands.html
                          02b-commands-complete.html
                          07-plugin-skills-guide.html

postgresql-quickstart/    pg18-cheatsheet-01-sql-syntax-ddl.html
                          pg18-cheatsheet-10-programming-advanced.html

redis-cheat-sheet/        cheatsheet-01-core.html
                          cheatsheet-08-ecosystem-search-ai.html
```

## 索引頁功能

- **分組檢視**：按主題分類顯示，每組有標題和數量
- **列表檢視**：所有報告攤平成一個列表
- **分類篩選**：點擊分類按鈕快速過濾
- **即時搜尋**：輸入關鍵字即時篩選報告
- **Light/Dark 模式**：手動切換深淺色主題，偏好自動儲存於 localStorage

## 授權

Apache License 2.0
