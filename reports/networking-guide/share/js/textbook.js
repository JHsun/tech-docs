/* =========================================================================
   防火牆穿越與 P2P 技術學習手冊 - 共用 JS
   功能：主題切換、Mermaid 主題同步、目錄產生
   ========================================================================= */

(function () {
  "use strict";

  // ---------- 主題切換 ----------
  const THEME_KEY = "p2p-textbook-theme";

  function getInitialTheme() {
    try {
      const saved = localStorage.getItem(THEME_KEY);
      if (saved === "light" || saved === "dark") return saved;
    } catch (e) { /* 忽略 */ }
    if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    }
    return "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    try { localStorage.setItem(THEME_KEY, theme); } catch (e) { /* 忽略 */ }
    updateThemeButton(theme);
    rerenderMermaid(theme);
  }

  function updateThemeButton(theme) {
    const btn = document.getElementById("themeToggle");
    if (!btn) return;
    if (theme === "dark") {
      btn.innerHTML = '<svg class="theme-icon" viewBox="0 0 24 24"><path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13l2 .01V11H2v2zm18 0l2 .01V11h-2v2zM11 2v2h2V2h-2zm0 18v2h2v-2h-2zM5.99 4.58l-1.41 1.41 1.79 1.79 1.41-1.41-1.79-1.79zm12.37 12.37l-1.41 1.41 1.79 1.79 1.41-1.41-1.79-1.79zm1.79-10.96l-1.41-1.41-1.79 1.79 1.41 1.41 1.79-1.79zM7.76 17.24l-1.41-1.41-1.79 1.79 1.41 1.41 1.79-1.79z"/></svg> 亮色';
    } else {
      btn.innerHTML = '<svg class="theme-icon" viewBox="0 0 24 24"><path d="M12 3a9 9 0 109 9c0-.46-.04-.92-.1-1.36a5.389 5.389 0 01-4.4 2.26 5.403 5.403 0 01-3.14-9.8c-.44-.06-.9-.1-1.36-.1z"/></svg> 暗色';
    }
  }

  function toggleTheme() {
    const cur = document.documentElement.getAttribute("data-theme") || "light";
    applyTheme(cur === "dark" ? "light" : "dark");
  }

  // ---------- Mermaid 設定 ----------
  function getMermaidConfig(theme) {
    const isDark = theme === "dark";
    return {
      startOnLoad: false,
      theme: "base",
      securityLevel: "loose",
      fontFamily: '"BookSans", "Noto Sans TC", sans-serif',
      themeVariables: isDark
        ? {
            // 暗色佈景
            background: "#1a1d23",
            primaryColor: "#252830",
            primaryTextColor: "#d6d2c8",
            primaryBorderColor: "#5a6478",
            lineColor: "#8a8478",
            secondaryColor: "#2a3a32",
            tertiaryColor: "#3a2a25",
            mainBkg: "#252830",
            secondBkg: "#1c1f25",
            tertiaryBkg: "#14161a",
            textColor: "#d6d2c8",
            nodeBorder: "#d97757",
            clusterBkg: "#1c1f25",
            clusterBorder: "#5a6478",
            edgeLabelBackground: "#1a1d23",
            // 序列圖
            actorBkg: "#252830",
            actorBorder: "#d97757",
            actorTextColor: "#d6d2c8",
            actorLineColor: "#8a8478",
            signalColor: "#d6d2c8",
            signalTextColor: "#d6d2c8",
            labelBoxBkgColor: "#252830",
            labelBoxBorderColor: "#d97757",
            labelTextColor: "#d6d2c8",
            loopTextColor: "#d6d2c8",
            noteBkgColor: "#3a2a25",
            noteTextColor: "#e6b450",
            noteBorderColor: "#e6b450",
            activationBkgColor: "#3a4a4a",
            activationBorderColor: "#6ec896",
            sequenceNumberColor: "#14161a",
            // 流程圖
            altBackground: "#1c1f25"
          }
        : {
            // 亮色佈景
            background: "#fbf6e9",
            primaryColor: "#efe7d3",
            primaryTextColor: "#2a1f12",
            primaryBorderColor: "#8a7456",
            lineColor: "#5a4a35",
            secondaryColor: "#dfe8d7",
            tertiaryColor: "#f5e1c0",
            mainBkg: "#efe7d3",
            secondBkg: "#e8dec5",
            tertiaryBkg: "#f6f1e7",
            textColor: "#2a1f12",
            nodeBorder: "#8b1a1a",
            clusterBkg: "#f6f1e7",
            clusterBorder: "#8a7456",
            edgeLabelBackground: "#fbf6e9",
            actorBkg: "#efe7d3",
            actorBorder: "#8b1a1a",
            actorTextColor: "#2a1f12",
            actorLineColor: "#5a4a35",
            signalColor: "#2a1f12",
            signalTextColor: "#2a1f12",
            labelBoxBkgColor: "#efe7d3",
            labelBoxBorderColor: "#8b1a1a",
            labelTextColor: "#2a1f12",
            loopTextColor: "#2a1f12",
            noteBkgColor: "#f5e1c0",
            noteTextColor: "#7a4818",
            noteBorderColor: "#b8761d",
            activationBkgColor: "#dfe8d7",
            activationBorderColor: "#2d5a3d",
            sequenceNumberColor: "#fbf6e9",
            altBackground: "#e8dec5"
          }
    };
  }

  function initMermaid() {
    if (typeof mermaid === "undefined") return;
    const theme = document.documentElement.getAttribute("data-theme") || "light";
    mermaid.initialize(getMermaidConfig(theme));

    // 將原始 source 保存到 data 屬性，方便切換主題時重繪
    document.querySelectorAll(".mermaid").forEach((el) => {
      if (!el.dataset.source) {
        el.dataset.source = el.textContent.trim();
      }
    });

    renderMermaidAll();
  }

  function renderMermaidAll() {
    if (typeof mermaid === "undefined") return;
    document.querySelectorAll(".mermaid").forEach((el, idx) => {
      const src = el.dataset.source || el.textContent.trim();
      const id = "mmd-" + Math.random().toString(36).slice(2, 9);
      try {
        mermaid.render(id, src).then(({ svg }) => {
          el.innerHTML = svg;
        }).catch((e) => {
          el.innerHTML = '<pre style="color:#a55;">Mermaid 渲染失敗：' + (e.message || e) + '</pre>';
        });
      } catch (e) {
        el.innerHTML = '<pre style="color:#a55;">Mermaid 渲染失敗：' + (e.message || e) + '</pre>';
      }
    });
  }

  function rerenderMermaid(theme) {
    if (typeof mermaid === "undefined") return;
    mermaid.initialize(getMermaidConfig(theme));
    renderMermaidAll();
  }

  // ---------- 事件繫結 ----------
  function init() {
    applyTheme(getInitialTheme());

    const btn = document.getElementById("themeToggle");
    if (btn) btn.addEventListener("click", toggleTheme);

    // 鍵盤快捷鍵：T 切換主題
    document.addEventListener("keydown", (e) => {
      if ((e.key === "t" || e.key === "T") &&
          !e.ctrlKey && !e.metaKey && !e.altKey &&
          !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
        toggleTheme();
      }
    });

    // 等 Mermaid 載入後初始化
    if (typeof mermaid !== "undefined") {
      initMermaid();
    } else {
      window.addEventListener("load", () => {
        if (typeof mermaid !== "undefined") initMermaid();
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
