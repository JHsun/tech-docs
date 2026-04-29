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

### 共用設計系統（2026/04 起）

新報告一律引用 `reports/shared/` 下的共用檔案，不再自行定義色彩 token：

```html
<head>
  <!-- 1. Google Fonts（統一載入） -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&family=JetBrains+Mono:wght@400;500;700&display=swap">

  <!-- 2. 統一 token 層（Calm Teal 主色，OKLCH 色彩系統） -->
  <link rel="stylesheet" href="https://jhsun.github.io/tech-docs/reports/shared/tokens.css">

  <!-- 3. 主題切換（選用，有 light/dark 切換需求才加） -->
  <script src="https://jhsun.github.io/tech-docs/reports/shared/theme-toggle.js" defer></script>
</head>
```

#### 可用的 CSS 變數

```css
/* 色彩 */
var(--color-primary)      /* Calm Teal 主色 */
var(--color-success)      /* #16a34a / dark: #4ade80 */
var(--color-warning)      /* #d97706 / dark: #fbbf24 */
var(--color-danger)       /* #dc2626 / dark: #f87171 */
var(--color-info)         /* #0891b2 / dark: #22d3ee */

/* 背景 */
var(--bg-canvas)          /* 頁面背景 */
var(--bg-surface)         /* 卡片背景 */
var(--bg-muted)           /* 次層背景 */
var(--bg-code)            /* 程式碼區塊背景 */

/* 文字 */
var(--text-primary)       /* 主文字 */
var(--text-secondary)     /* 次要文字 */
var(--text-muted)         /* 輔助說明 */

/* 邊框與陰影 */
var(--border-soft)        /* 淡邊框 */
var(--border-mid)         /* 中等邊框 */
var(--shadow-sm)  var(--shadow-md)

/* 字型 */
var(--font-sans)          /* DM Sans + Noto Sans TC */
var(--font-mono)          /* JetBrains Mono */
var(--font-serif)         /* Playfair Display（長篇標題用） */

/* 間距（4px 基準） */
var(--space-1) ~ var(--space-9)   /* 4px ~ 96px */

/* 圓角 */
var(--radius-sm/md/lg/xl)         /* 4/8/12/16px */
```

#### light/dark 主題切換

使用 `data-theme-toggle` 屬性即可，JS 自動接管：

```html
<button data-theme-toggle></button>
<script src="../../shared/theme-toggle.js" defer></script>
```

HTML 根元素預設 light，`theme-toggle.js` 載入後自動讀取 `localStorage` 和 `prefers-color-scheme`。

### 報告 HTML 風格

**新報告（2026/04 起）**：使用共用設計系統（見上節），色彩全用 token 變數，不寫死 hex 值。

**舊報告（歷史存檔）**：維持原有 inline CSS 不動。

- 暗色主題（`#0f1117` 背景）
- 字型：JetBrains Mono（程式碼）+ DM Sans（UI）+ Noto Sans TC（中文）
- 三欄 grid 佈局，卡片式組件
- 色彩分類：blue/green/yellow/red/cyan/purple 漸層頂邊
- 語言：繁體中文

### Mermaid 圖表

**新報告**（2026/04 起）使用全域共用 init：
```html
<script src="shared/mermaid.min.js"></script>
<script src="../../shared/mermaid-init.js" defer></script>
```

**舊報告**仍用 `reports/[category]/shared/mermaid.min.js`（不動）。

共用規範（新舊皆適用）：
- **HTML labels 必須用 entities**：`&lt;br/&gt;`、`&lt;b&gt;`、`&lt;i&gt;`
- 用 `dataset.mermaidSrc = textContent` 儲存原始 source（不用 innerHTML）
- 切換主題後自動重渲染（`mermaid-init.js` 已內建，監聽 `jhsun:theme-changed` 事件）

### Git

- Commit message 使用英文
- 報告類 commit 前綴 `docs:`
- 不要 force push main 分支

## Key Files

- `update_index.py` — 索引生成器，包含 HTML 模板、CSS、JS、分類色標邏輯
- `index.html` — 自動生成的首頁（勿直接編輯）
- `.github/workflows/update-index.yml` — CI 配置
- `reports/shared/tokens.css` — **統一設計 token 層**（Calm Teal，OKLCH）；新報告必須引用
- `reports/shared/theme-toggle.js` — light/dark/system 切換模組
- `reports/shared/mermaid-init.js` — Mermaid 主題整合（訂閱 `jhsun:theme-changed`）

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
