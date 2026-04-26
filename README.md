# JHsun × Claude TechDocs

由 JHsun 規劃、Claude AI 執行的技術文件平台，收錄 **250+ 篇**速查表、快速入門與系統管理指南，涵蓋 29 個技術分類，託管於 GitHub Pages。

## 架構

```
tech-docs/
├── index.html                          ← 自動產生的索引頁（支援分組/列表/搜尋/深淺色主題）
├── update_index.py                     ← 索引產生器（遞迴掃描子目錄，自動分配色標）
├── CLAUDE.md                           ← Claude Code 專案設定
├── reports/
│   ├── python-tutorial/                ← Python 教學系列 (31 篇)
│   ├── gitlab-administration/          ← GitLab 管理系列 (25 篇)
│   ├── go-tutorial/                    ← Go 語言教學系列 (23 篇)
│   ├── proxy-guide/                    ← Proxy 完全指南系列 (16 篇)
│   ├── claude-code-quickstart/         ← Claude Code 速查表系列 (14 篇)
│   ├── playwright-cheat-sheet/         ← Playwright 速查表系列 (13 篇)
│   ├── haproxy-configuration-manual-cheat-sheet/ ← HAProxy 設定手冊 (13 篇)
│   ├── mysql-8_4-cheat-sheet/          ← MySQL 8.4 速查表系列 (12 篇)
│   ├── postgresql-quickstart/          ← PostgreSQL 18 速查表系列 (11 篇)
│   ├── haproxy-starter-management-guide-cheat-sheet/ ← HAProxy 入門管理 (11 篇)
│   ├── redmine-cheat-sheet/            ← Redmine 速查表系列 (9 篇)
│   ├── kafka-cheat-sheet/              ← Kafka 速查表系列 (9 篇)
│   ├── redis-cheat-sheet/              ← Redis 速查表系列 (8 篇)
│   ├── bifrost-cheat-sheet/            ← Bifrost 速查表系列 (7 篇)
│   ├── ai-skills-workflows/            ← AI 技能與工作流程 (6 篇)
│   ├── ai-infrastructure/              ← AI 基礎建設 (6 篇)
│   ├── nginx-cheat-sheet/              ← Nginx 速查表系列 (5 篇)
│   ├── faastapi-quickstart/            ← FastAPI 快速入門 (5 篇)
│   ├── etcd-quickstart/                ← etcd 速查表系列 (5 篇)
│   ├── linux-cheat-sheet/              ← Linux 工具教學 (4 篇)
│   ├── gsd-cheat-sheet/                ← GSD 速查表系列 (4 篇)
│   ├── keepalived-cheat-sheet/         ← Keepalived 速查表 (3 篇)
│   ├── js-ecosystem/                   ← JavaScript 生態系 (2 篇)
│   ├── haproxy-acl-cheatsheet/         ← HAProxy ACL 速查表 (2 篇)
│   ├── ai-agent/                       ← AI Agent (2 篇)
│   ├── k8s-ecosystem/                  ← Kubernetes 生態系 (1 篇)
│   ├── javascript/                     ← JavaScript (1 篇)
│   ├── discord-quickstart/             ← Discord 快速入門 (1 篇)
│   └── ai-model/                       ← AI 模型 (1 篇)
├── .github/workflows/update-index.yml  ← 自動更新索引的 CI
└── README.md
```

## 使用方式

在 Claude Code（已設定 GitHub MCP）中，直接說：

> 幫我寫一份關於 XX 的技術報告，存到 `reports/主題/NN-slug.html`

Claude 會自動產製 HTML 並推送到 repo，GitHub Actions 自動重建索引頁。

## 目錄與命名規則

### 目錄

- `reports/子目錄/` 下的檔案歸入該子目錄為分類
- 子目錄名稱即分類名，常見後綴 `-quickstart`、`-cheat-sheet`、`-tutorial` 在顯示時自動去除

### 檔案命名

```
[NN]-[topic-slug].html              ← 通用格式
[prefix]-[NN]-[topic-slug].html     ← 帶系列前綴
```

| 規則 | 說明 | 範例 |
|------|------|------|
| 零填充兩位數 | 確保 1–99 正確排序 | `01-`, `02-`, `10-` |
| 補充篇用字母後綴 | 插入在原編號之後 | `02b-commands-complete.html` |
| 帶系列前綴 | 同分類保持一致 | `pg18-cheatsheet-01-sql-syntax-ddl.html` |
| 避免純描述名 | 無編號導致排序不可控 | ~~`awk-tutorial.html`~~ → `02-awk-tutorial.html` |

## 報告 HTML 規範

- **暗色主題**：背景 `#0f1117`
- **字型**：JetBrains Mono（程式碼）、DM Sans（UI）、Noto Sans TC（中文）
- **版型**：三欄 grid，卡片式組件，色彩分類頂邊漸層
- **語言**：繁體中文
- **Mermaid 圖表**：使用本地 `shared/mermaid.min.js`，支援 light/dark 雙主題重渲染

## 索引頁功能

| 功能 | 說明 |
|------|------|
| 分組檢視 | 按技術分類顯示，各組顯示篇數 |
| 列表檢視 | 所有報告攤平一覽 |
| 分類篩選 | 點擊標籤快速過濾 |
| 即時搜尋 | 輸入關鍵字即時篩選 |
| Light/Dark 模式 | 手動切換，偏好儲存於 localStorage |

## 授權

本作品採用 [Creative Commons 姓名標示-非商業性使用 4.0 國際授權條款 (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.zh-hant) 授權。

- 可自由複製、分享、改作
- 須標示原作者
- 非商業使用：商業用途須事先取得作者書面授權
