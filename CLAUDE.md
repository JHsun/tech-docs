# CLAUDE.md — AI Report Hub

## Project Overview

AI Report Hub 是一個託管於 GitHub Pages 的 HTML 分析報告彙整平台。報告由 Claude AI 產製，`update_index.py` 自動掃描 `reports/` 目錄並生成 `index.html` 索引頁。

## Tech Stack

- 純 HTML/CSS/JS（無框架）
- Python 3 (`update_index.py` 索引產生器)
- GitHub Pages 靜態託管
- GitHub Actions CI 自動重建索引

## Architecture

```
reports/[category]/[NN]-[topic].html  → 報告檔案
update_index.py                       → 掃描 reports/ 生成 index.html
index.html                            → 自動生成，勿手動編輯
.github/workflows/update-index.yml    → push 時自動執行 update_index.py
```

## Conventions

### 檔案命名

- 格式：`[NN]-[topic-slug].html` 或 `[prefix]-[NN]-[topic-slug].html`
- NN 為零填充兩位數（01-99），確保正序排列
- 補充篇用字母後綴：`02a-`, `02b-`
- 禁止使用無編號的純描述名（會導致排序不可控）

### 分類目錄

- 目錄名即分類名，常見格式：`[topic]-quickstart`、`[topic]-cheat-sheet`
- `update_index.py` 會自動從目錄名推導顯示名稱（去除 `-quickstart`、`-cheat-sheet` 等後綴，首字母大寫）
- 特殊顯示名稱在 `CATEGORY_DISPLAY_OVERRIDE` 中手動覆蓋
- 色標從 `COLOR_PALETTE`（10 色）自動輪替分配，無需手動設定

### index.html

- **不要手動編輯** — 由 `update_index.py` 自動生成
- 所有設計變更（CSS、佈局、功能）必須修改 `update_index.py` 中的模板
- 功能：light/dark 模式切換、即時搜尋、分類篩選、分組/列表視圖

### 報告 HTML 風格

- 暗色主題（`#0f1117` 背景）
- 字型：JetBrains Mono（程式碼）+ DM Sans（UI）+ Noto Sans TC（中文）
- 三欄 grid 佈局，卡片式組件
- 色彩分類：blue/green/yellow/red/cyan/purple 漸層頂邊
- 語言：繁體中文

### Mermaid 圖表

- 共用本地 mermaid.min.js：`reports/[category]/shared/mermaid.min.js`，符合離線閱讀需求（不依賴 CDN）
- **HTML labels 必須用 entities 寫**：`&lt;br/&gt;`、`&lt;b&gt;`、`&lt;i&gt;`，否則 textContent 剝離後重渲染（例如切主題）會炸成單行
- 用 `dataset.source = textContent`（不是 `innerHTML`）儲存原始 source — 避開 XSS 安全 hook，且確保重渲染拿得到原始 mermaid source
- 雙主題重渲染：`toggleTheme()` 內呼叫 `renderMermaid()`；`getMermaidConfig(theme)` 提供 light/dark themeVariables
- 參考實作：`reports/proxy-guide/06-proxy-guide-part-5-ai-era.html`（CSS、script、figure 包裝範例齊全）

### Git

- Commit message 使用英文
- 報告類 commit 前綴 `docs:`
- 不要 force push main 分支

## Key Files

- `update_index.py` — 索引生成器，包含 HTML 模板、CSS、JS、分類色標邏輯
- `index.html` — 自動生成的首頁（勿直接編輯）
- `.github/workflows/update-index.yml` — CI 配置

## Common Tasks

### 新增報告

1. 在 `reports/[category]/` 下建立 `[NN]-[topic].html`
2. Push 後 GitHub Actions 自動重建 index.html

### 新增分類

1. 建立 `reports/[new-category]/` 目錄
2. 放入報告檔案，Push 即可
3. `update_index.py` 自動偵測新目錄、分配色標和顯示名稱
4. 若自動推導的名稱不理想，在 `CATEGORY_DISPLAY_OVERRIDE` 中覆蓋

### 修改索引頁設計

修改 `update_index.py` 中 `generate_index()` 的 HTML 模板，**不要直接改 index.html**。
