# AI Report Hub

由 Claude AI 產製的 HTML 分析報告彙整平台，託管於 GitHub Pages。

## 架構

```
tech-docs/
├── index.html                  ← 自動產生的索引頁
├── update_index.py             ← 索引產生器
├── reports/                    ← AI 產製的 HTML 報告
├── .github/workflows/          ← 自動更新索引的 CI
└── README.md
```

## 使用方式

在 Claude Desktop（已設定 GitHub MCP）中，直接說：

> 幫我寫一份關於 XX 的分析報告，存到 `JHsun/tech-docs` repo 的 `reports/YYYY-MM-DD_slug.html`

Claude 會自動產製 HTML 並推送到 repo，GitHub Actions 會自動重建索引頁。

## 報告檔名慣例

`YYYY-MM-DD_描述性slug.html`，例如：
- `2026-03-26_ai-trend-analysis.html`
- `2026-03-26_q1-revenue-review.html`

## 授權

Apache License 2.0
