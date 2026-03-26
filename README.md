# AI Report Hub

由 Claude AI 產製的 HTML 分析報告彙整平台，託管於 GitHub Pages。

## 架構

```
tech-docs/
├── index.html                          ← 自動產生的索引頁（支援分組/列表切換）
├── update_index.py                     ← 索引產生器（遞迴掃描子目錄）
├── reports/
│   ├── linux-commands.html             ← 未分類報告
│   ├── ai/                             ← 按主題分類
│   │   ├── 2026-03-26_llm-overview.html
│   │   └── transformer-guide.html
│   ├── linux/
│   │   └── 2026-03-26_shell-tips.html
│   └── cloud/
│       └── aws-basics.html
├── .github/workflows/update-index.yml  ← 自動更新索引的 CI
└── README.md
```

## 使用方式

在 Claude Desktop（已設定 GitHub MCP）中，直接說：

> 幫我寫一份關於 XX 的分析報告，存到 `JHsun/tech-docs` repo 的 `reports/主題/YYYY-MM-DD_slug.html`

例如：
- `reports/ai/2026-03-26_llm-comparison.html`
- `reports/linux/2026-03-27_docker-guide.html`
- `reports/cloud/2026-03-27_aws-lambda.html`

Claude 會自動產製 HTML 並推送到 repo，GitHub Actions 會自動重建索引頁。

## 目錄結構規則

- `reports/` 根目錄的檔案歸入「其他」分類
- `reports/子目錄/` 下的檔案歸入該子目錄名稱的分類
- 子目錄名稱即為分類名稱（如 `ai`、`linux`、`cloud`）
- 檔名建議使用 `YYYY-MM-DD_描述性slug.html` 格式

## 索引頁功能

- **分組檢視**：按主題分類顯示，每組有標題和數量
- **列表檢視**：所有報告攤平成一個列表
- **分類篩選**：點擊分類按鈕快速過濾

## 授權

Apache License 2.0
