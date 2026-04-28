# `shared/` — JHsun TechDocs Unified Layer

統一所有技術文件頁面的設計 token、字型、Mermaid 主題與 light/dark 切換。
**v1.0 · Calm Teal**（hue 200° / chroma 0.11）

---

## 📦 檔案清單

| 檔案 | 用途 | 引用順序 |
|---|---|---|
| `fonts.html` | Google Fonts `<link>` 片段（7 套字型一次載入） | 1️⃣ `<head>` 最上方 |
| `tokens.css` | CSS 變數：色彩 / 字型 / 間距 / 圓角 / 陰影 / 暗色模式 | 2️⃣ 在 fonts 之後 |
| `theme-toggle.js` | light / dark / system 切換按鈕 + localStorage | 3️⃣ `<body>` 末尾 |
| `mermaid-init.js` | Mermaid 主題與 token 同步，theme 切換時自動重繪 | 4️⃣ 在 mermaid CDN 之後 |

---

## 🚀 一頁套用範本

```html
<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>My Page</title>

  <!-- 1. Fonts (paste contents of shared/fonts.html) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@400;500;700&family=Playfair+Display:wght@500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&display=swap" />

  <!-- 2. Tokens -->
  <link rel="stylesheet" href="shared/tokens.css" />
</head>
<body>
  <header>
    <button data-theme-toggle></button>
  </header>

  <main>
    <h1 style="font-family: var(--font-serif); color: var(--color-primary-text);">
      Hello, world.
    </h1>

    <pre class="mermaid">
graph LR
  A[Start] --> B{Decide}
  B -->|yes| C[Do it]
  B -->|no| D[Skip]
    </pre>
  </main>

  <!-- 3. Mermaid + Theme -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="shared/theme-toggle.js"></script>
  <script src="shared/mermaid-init.js"></script>
</body>
</html>
```

---

## 🎨 Token 速查

### 色彩
| 變數 | 用途 |
|---|---|
| `--color-primary` | 主色（CTA、強調、連結） |
| `--color-primary-hover` | 主色 hover 態 |
| `--color-primary-soft` | 主色背景（pill、tag、淡底） |
| `--color-primary-text` | 主色文字（在淺底上） |
| `--color-success` / `-soft` | ✅ 成功 |
| `--color-warning` / `-soft` | ⚠ 警告 |
| `--color-danger` / `-soft` | ⛔ 錯誤 / 破壞性 |
| `--color-info` / `-soft` | ℹ 資訊 |
| `--bg-canvas` | 頁面底色 |
| `--bg-surface` | 卡片、面板 |
| `--bg-muted` | 次要區塊 |
| `--bg-code` | 程式碼底色 |
| `--text-primary` / `-secondary` / `-muted` | 文字三層級 |
| `--border-soft` / `-mid` | 邊框 |

### 字型
| 變數 | 字型 |
|---|---|
| `--font-mono` | JetBrains Mono（程式碼、技術速查） |
| `--font-sans` | DM Sans + Noto Sans TC（介面、標題） |
| `--font-serif` | Playfair Display + Noto Serif TC（編輯式大標） |
| `--font-serif-body` | Source Serif 4 + Noto Serif TC（長文內文） |

### 字級 / 間距
- 字級：`--text-xs` ~ `--text-4xl`（12 → 64px）
- 間距：`--space-1` ~ `--space-9`（4 → 96px）
- 容器：`--container-narrow` (720px, editorial) / `--container-wide` (1280px, cheatsheet)
- 圓角：`--radius-sm/md/lg/xl`
- 陰影：`--shadow-sm/md/lg`

---

## 🌗 Theme toggle

`theme-toggle.js` 自動偵測任何 `[data-theme-toggle]` 元素並掛載：

```html
<button data-theme-toggle></button>
```

- 三段循環：**Light → Dark → System**
- `System` 模式跟隨 OS `prefers-color-scheme`
- 偏好存於 `localStorage['jhsun-theme']`
- 切換時觸發 `window` 事件 `jhsun:theme-changed`，`detail: { theme, mode }`

**程式 API：**
```js
JHsunTheme.get();       // 'light' | 'dark' | 'system'
JHsunTheme.set('dark');
JHsunTheme.toggle();
```

**自訂按鈕外觀**：在按鈕上加 `data-theme-toggle-styled="1"` 阻止內建內容填入，自己畫 icon。

---

## 📊 Mermaid

`mermaid-init.js` 會：

1. 讀取目前 token，產生 `themeVariables`
2. 自動 `mermaid.run()` 渲染所有 `.mermaid` 區塊
3. 監聽 `jhsun:theme-changed`，theme 切換時重繪
4. 內部把原始碼存在 `data-mermaid-src`，避免重繪後遺失來源

**程式 API：**
```js
JHsunMermaid.renderAll();           // 強制重繪
JHsunMermaid.getMermaidConfig();    // 取得目前 config（debug 用）
```

---

## 🔧 自訂主色（不建議常用）

預設為 Calm Teal。臨時覆寫：

```css
:root {
  --tk-hue: 270;       /* indigo violet */
  --tk-chroma: 0.13;
}
```

語意色（success/warning/danger/info）**永遠不變**——確保跨頁面一致。

---

## ✅ Checklist 遷移舊頁面

- [ ] 移除頁內 `<style>` 中的硬編碼色（hex / rgb）
- [ ] 替換為 `var(--color-*)` / `var(--text-*)` / `var(--bg-*)`
- [ ] 字型改為 `var(--font-sans/mono/serif/serif-body)`
- [ ] 間距、圓角、陰影改用 token
- [ ] 加入 `<button data-theme-toggle>`
- [ ] 確認 dark mode 下視覺正確

---

**版本**：v1.0 (Calm Teal)
**維護**：見 `Token Layer.html` 的 §06 設計決策紀錄
