#!/usr/bin/env python3
"""
update_index.py — 遞迴掃描 reports/ 資料夾（含子目錄），自動產生 index.html

支援結構：
  reports/file.html              → 歸入「未分類」
  reports/linux/file.html        → 歸入「linux」分類
  reports/ai/deep-learning.html  → 歸入「ai」分類
"""

import re
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent
REPORTS_DIR = REPO_ROOT / "reports"
INDEX_PATH = REPO_ROOT / "index.html"

# 分類的簡短顯示名稱
CATEGORY_DISPLAY = {
    "claude-code-quickstart": "Claude Code",
    "etcd-quickstart": "etcd",
    "linux-cheat-sheet": "Linux",
    "postgresql-quickstart": "PostgreSQL",
    "redis-cheat-sheet": "Redis",
    "_uncategorized": "其他",
}


def category_display_name(cat):
    return CATEGORY_DISPLAY.get(cat, cat)


def extract_title(filepath):
    try:
        content = filepath.read_text(encoding="utf-8")
        match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return filepath.stem.replace("_", " ").replace("-", " ")


def extract_date(filename):
    match = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    return match.group(1) if match else ""


def scan_reports():
    """遞迴掃描 reports/ 下所有 .html，回傳按分類分組的字典"""
    groups = OrderedDict()
    if not REPORTS_DIR.exists():
        return groups

    html_files = sorted(REPORTS_DIR.rglob("*.html"), key=lambda f: f.name, reverse=True)

    for f in html_files:
        rel = f.relative_to(REPORTS_DIR)
        parts = rel.parts
        if len(parts) >= 2:
            category = parts[0]
        else:
            category = "_uncategorized"

        if category not in groups:
            groups[category] = []

        groups[category].append({
            "filename": f.name,
            "rel_path": str(rel),
            "date": extract_date(f.name),
            "title": extract_title(f),
            "category": category,
        })

    # 把未分類放最後，其他按字母排序
    sorted_groups = OrderedDict()
    for k in sorted(groups.keys()):
        if k != "_uncategorized":
            sorted_groups[k] = groups[k]
    if "_uncategorized" in groups:
        sorted_groups["_uncategorized"] = groups["_uncategorized"]

    return sorted_groups


def build_card_html(report, num=""):
    tag = category_display_name(report["category"])
    return (
        '          <a class="report-card" href="reports/' + report["rel_path"] + '"'
        ' data-category="' + report["category"] + '">\n'
        '            <span class="report-num">' + str(num) + '</span>\n'
        '            <span class="report-title">' + report["title"] + '</span>\n'
        '            <span class="report-tag" data-tag="' + report["category"] + '">' + tag + '</span>\n'
        '            <span class="report-arrow">&rarr;</span>\n'
        '          </a>\n'
    )


def generate_index(groups):
    today = datetime.now().strftime("%Y-%m-%d")
    total = sum(len(v) for v in groups.values())
    categories = [k for k in groups.keys() if k != "_uncategorized"]

    # --- build grouped view ---
    grouped_html = ""
    for cat, reports in groups.items():
        display_name = category_display_name(cat)
        grouped_html += '      <div class="category-group" data-category="' + cat + '">\n'
        grouped_html += '        <div class="category-header">\n'
        grouped_html += '          <div class="category-icon" data-cat="' + cat + '">&#9670;</div>\n'
        grouped_html += '          <span class="category-title">' + display_name + '</span>\n'
        grouped_html += '          <span class="category-count">' + str(len(reports)) + '</span>\n'
        grouped_html += '        </div>\n'
        grouped_html += '        <div class="report-list">\n'
        for i, r in enumerate(reports):
            grouped_html += build_card_html(r, len(reports) - i)
        grouped_html += '        </div>\n'
        grouped_html += '      </div>\n'

    # --- build flat view ---
    all_reports = []
    for reports in groups.values():
        all_reports.extend(reports)
    all_reports.sort(key=lambda r: r["filename"], reverse=True)

    flat_html = ""
    for i, r in enumerate(all_reports):
        flat_html += build_card_html(r, i + 1)

    # --- build filter buttons ---
    filter_html = '        <button class="filter-btn active" data-filter="all" onclick="filterBy(this)">全部</button>\n'
    for cat in categories:
        display = category_display_name(cat)
        filter_html += '        <button class="filter-btn" data-filter="' + cat + '" onclick="filterBy(this)">' + display + '</button>\n'
    if "_uncategorized" in groups:
        filter_html += '        <button class="filter-btn" data-filter="_uncategorized" onclick="filterBy(this)">其他</button>\n'

    if total == 0:
        grouped_html = '      <div class="empty">尚無報告，請新增第一份報告。</div>\n'
        flat_html = grouped_html

    # --- assemble page ---
    html = """<!DOCTYPE html>
<html lang="zh-TW" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Report Hub</title>
  <style>
    :root {
      --bg: #f5f5f7;
      --bg-secondary: #eeeef0;
      --card-bg: #ffffff;
      --card-hover: #ffffff;
      --text: #1d1d1f;
      --text-secondary: #6e6e73;
      --text-muted: #86868b;
      --accent: #6c5ce7;
      --accent-hover: #5a4bd1;
      --accent-glow: rgba(108, 92, 231, 0.12);
      --accent-subtle: rgba(108, 92, 231, 0.08);
      --border: rgba(0, 0, 0, 0.06);
      --border-hover: rgba(108, 92, 231, 0.3);
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.06), 0 1px 4px rgba(0, 0, 0, 0.04);
      --tag-claude: #e8e0ff; --tag-claude-text: #5a4bd1;
      --tag-etcd: #d4f5e9; --tag-etcd-text: #0f7b5f;
      --tag-linux: #ffecd2; --tag-linux-text: #b8651a;
      --tag-pg: #dbeafe; --tag-pg-text: #1e40af;
      --tag-redis: #fee2e2; --tag-redis-text: #b91c1c;
      --tag-other: #e8e8ed; --tag-other-text: #6e6e73;
      --header-bg: rgba(245, 245, 247, 0.8);
      --radius-sm: 10px;
      --transition: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    [data-theme="dark"] {
      --bg: #0d0d0f;
      --bg-secondary: #161618;
      --card-bg: #1c1c1e;
      --card-hover: #222224;
      --text: #f5f5f7;
      --text-secondary: #a1a1a6;
      --text-muted: #6e6e73;
      --accent: #a78bfa;
      --accent-hover: #b9a0fc;
      --accent-glow: rgba(167, 139, 250, 0.15);
      --accent-subtle: rgba(167, 139, 250, 0.08);
      --border: rgba(255, 255, 255, 0.06);
      --border-hover: rgba(167, 139, 250, 0.35);
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.2);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.3);
      --tag-claude: rgba(108, 92, 231, 0.2); --tag-claude-text: #b9a0fc;
      --tag-etcd: rgba(16, 185, 129, 0.15); --tag-etcd-text: #6ee7b7;
      --tag-linux: rgba(251, 191, 36, 0.15); --tag-linux-text: #fcd34d;
      --tag-pg: rgba(59, 130, 246, 0.15); --tag-pg-text: #93c5fd;
      --tag-redis: rgba(239, 68, 68, 0.15); --tag-redis-text: #fca5a5;
      --tag-other: rgba(255, 255, 255, 0.08); --tag-other-text: #a1a1a6;
      --header-bg: rgba(13, 13, 15, 0.85);
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
      background: var(--bg); color: var(--text); line-height: 1.6;
      -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
      transition: background var(--transition), color var(--transition);
    }
    .container { max-width: 920px; margin: 0 auto; padding: 0 1.5rem 3rem; }
    .site-header {
      position: sticky; top: 0; z-index: 100;
      background: var(--header-bg);
      backdrop-filter: blur(20px) saturate(180%);
      -webkit-backdrop-filter: blur(20px) saturate(180%);
      border-bottom: 1px solid var(--border);
      margin-bottom: 2rem;
      transition: background var(--transition), border-color var(--transition);
    }
    .header-inner {
      max-width: 920px; margin: 0 auto; padding: 1rem 1.5rem;
      display: flex; align-items: center; justify-content: space-between;
    }
    .logo { display: flex; align-items: center; gap: 0.6rem; }
    .logo-icon {
      width: 36px; height: 36px; position: relative;
      background: linear-gradient(135deg, #6c5ce7 0%, #a78bfa 50%, #c4b5fd 100%);
      border-radius: 10px; display: flex; align-items: center; justify-content: center;
      box-shadow: 0 2px 10px rgba(108, 92, 231, 0.35), inset 0 1px 0 rgba(255,255,255,0.15);
      overflow: hidden;
    }
    .logo-icon::before {
      content: ''; position: absolute; inset: 0;
      background: linear-gradient(180deg, rgba(255,255,255,0.18) 0%, transparent 50%);
      border-radius: inherit;
    }
    .logo-icon svg { width: 20px; height: 20px; position: relative; z-index: 1; }
    .logo-text { font-size: 1.15rem; font-weight: 700; letter-spacing: -0.02em; }
    .theme-toggle {
      width: 52px; height: 28px;
      background: var(--bg-secondary); border: 1px solid var(--border);
      border-radius: 14px; cursor: pointer; transition: all var(--transition);
      display: flex; align-items: center; padding: 0 3px;
    }
    .theme-toggle:hover { border-color: var(--border-hover); }
    .theme-toggle-thumb {
      width: 22px; height: 22px; background: var(--card-bg);
      border-radius: 50%; box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
      transition: transform var(--transition);
      display: flex; align-items: center; justify-content: center; font-size: 0.7rem;
    }
    [data-theme="dark"] .theme-toggle-thumb { transform: translateX(24px); }
    .theme-toggle-thumb::after { content: "\\2600"; }
    [data-theme="dark"] .theme-toggle-thumb::after { content: "\\263D"; }
    .hero { text-align: center; margin-bottom: 2.5rem; }
    .hero h1 {
      font-size: 2.2rem; font-weight: 800; letter-spacing: -0.03em;
      background: linear-gradient(135deg, var(--text) 0%, var(--text-secondary) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text; margin-bottom: 0.5rem;
    }
    .hero p { color: var(--text-muted); font-size: 1rem; margin-bottom: 1.25rem; }
    .stats-row { display: flex; gap: 0.6rem; justify-content: center; flex-wrap: wrap; }
    .stat-chip {
      display: inline-flex; align-items: center; gap: 0.4rem;
      background: var(--accent-subtle); color: var(--accent);
      padding: 0.35rem 0.85rem; border-radius: 20px;
      font-size: 0.82rem; font-weight: 600;
    }
    .search-wrapper { position: relative; margin-bottom: 1rem; }
    .search-input {
      width: 100%; padding: 0.7rem 1rem 0.7rem 2.6rem;
      border: 1px solid var(--border); border-radius: var(--radius-sm);
      background: var(--card-bg); color: var(--text);
      font-size: 0.9rem; outline: none; transition: all var(--transition); font-family: inherit;
    }
    .search-input::placeholder { color: var(--text-muted); }
    .search-input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-glow); }
    .search-icon {
      position: absolute; left: 0.85rem; top: 50%; transform: translateY(-50%);
      color: var(--text-muted); font-size: 0.9rem; pointer-events: none;
    }
    .toolbar {
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.5rem;
    }
    .filter-bar { display: flex; gap: 0.35rem; flex-wrap: wrap; flex: 1; }
    .filter-btn {
      background: var(--card-bg); border: 1px solid var(--border); border-radius: 20px;
      padding: 0.3rem 0.8rem; font-size: 0.8rem; cursor: pointer;
      color: var(--text-secondary); transition: all var(--transition);
      font-weight: 500; font-family: inherit;
    }
    .filter-btn:hover { border-color: var(--border-hover); color: var(--accent); background: var(--accent-subtle); }
    .filter-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 2px 8px var(--accent-glow); }
    .view-toggle { display: flex; background: var(--bg-secondary); border-radius: 8px; padding: 2px; gap: 2px; }
    .view-btn {
      background: transparent; border: none; padding: 0.3rem 0.65rem;
      font-size: 0.8rem; cursor: pointer; color: var(--text-muted);
      transition: all var(--transition); border-radius: 6px; font-weight: 500; font-family: inherit;
    }
    .view-btn:hover { color: var(--text); }
    .view-btn.active { background: var(--card-bg); color: var(--text); box-shadow: var(--shadow-sm); }
    .report-list { display: flex; flex-direction: column; gap: 0.5rem; }
    .report-card {
      display: flex; align-items: center; gap: 1rem;
      padding: 0.85rem 1.15rem; background: var(--card-bg);
      border: 1px solid var(--border); border-radius: var(--radius-sm);
      text-decoration: none; color: inherit; transition: all var(--transition); position: relative;
    }
    .report-card::before {
      content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%);
      width: 3px; height: 0; background: var(--accent);
      border-radius: 0 3px 3px 0; transition: height var(--transition);
    }
    .report-card:hover {
      border-color: var(--border-hover); box-shadow: var(--shadow-md);
      background: var(--card-hover); transform: translateY(-1px);
    }
    .report-card:hover::before { height: 60%; }
    .report-card.hidden { display: none; }
    .report-num {
      font-size: 0.7rem; color: var(--text-muted); background: var(--bg-secondary);
      width: 26px; height: 26px; display: flex; align-items: center; justify-content: center;
      border-radius: 7px; font-weight: 600; flex-shrink: 0; font-variant-numeric: tabular-nums;
    }
    .report-title { font-weight: 500; flex: 1; font-size: 0.92rem; letter-spacing: -0.01em; }
    .report-tag {
      font-size: 0.72rem; padding: 0.2rem 0.6rem; border-radius: 12px;
      font-weight: 600; white-space: nowrap;
    }
    .report-tag[data-tag="claude-code-quickstart"] { background: var(--tag-claude); color: var(--tag-claude-text); }
    .report-tag[data-tag="etcd-quickstart"] { background: var(--tag-etcd); color: var(--tag-etcd-text); }
    .report-tag[data-tag="linux-cheat-sheet"] { background: var(--tag-linux); color: var(--tag-linux-text); }
    .report-tag[data-tag="postgresql-quickstart"] { background: var(--tag-pg); color: var(--tag-pg-text); }
    .report-tag[data-tag="redis-cheat-sheet"] { background: var(--tag-redis); color: var(--tag-redis-text); }
    .report-tag[data-tag="_uncategorized"] { background: var(--tag-other); color: var(--tag-other-text); }
    .report-arrow {
      color: var(--text-muted); font-size: 0.85rem; opacity: 0;
      transform: translateX(-4px); transition: all var(--transition);
    }
    .report-card:hover .report-arrow { opacity: 1; transform: translateX(0); }
    .category-group { margin-bottom: 1.75rem; }
    .category-group.hidden { display: none; }
    .category-header {
      display: flex; align-items: center; gap: 0.6rem;
      margin-bottom: 0.6rem; padding-left: 0.15rem;
    }
    .category-icon {
      width: 28px; height: 28px; border-radius: 8px;
      display: flex; align-items: center; justify-content: center; font-size: 0.85rem;
    }
    .category-icon[data-cat="claude-code-quickstart"] { background: var(--tag-claude); color: var(--tag-claude-text); }
    .category-icon[data-cat="etcd-quickstart"] { background: var(--tag-etcd); color: var(--tag-etcd-text); }
    .category-icon[data-cat="linux-cheat-sheet"] { background: var(--tag-linux); color: var(--tag-linux-text); }
    .category-icon[data-cat="postgresql-quickstart"] { background: var(--tag-pg); color: var(--tag-pg-text); }
    .category-icon[data-cat="redis-cheat-sheet"] { background: var(--tag-redis); color: var(--tag-redis-text); }
    .category-icon[data-cat="_uncategorized"] { background: var(--tag-other); color: var(--tag-other-text); }
    .category-title { font-size: 0.95rem; font-weight: 700; letter-spacing: -0.01em; }
    .category-count {
      font-size: 0.7rem; font-weight: 600; background: var(--accent-subtle);
      color: var(--accent); padding: 0.1rem 0.5rem; border-radius: 10px;
    }
    footer {
      text-align: center; margin-top: 3rem; padding-top: 1.5rem;
      border-top: 1px solid var(--border); color: var(--text-muted); font-size: 0.8rem;
    }
    footer a { color: var(--accent); text-decoration: none; }
    .empty { text-align: center; padding: 3rem; color: var(--text-muted); font-size: 0.9rem; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .report-card { animation: fadeIn 0.3s ease both; }
    .category-group:nth-child(1) .report-card { animation-delay: 0s; }
    .category-group:nth-child(2) .report-card { animation-delay: 0.05s; }
    .category-group:nth-child(3) .report-card { animation-delay: 0.1s; }
    .category-group:nth-child(4) .report-card { animation-delay: 0.15s; }
    @media (max-width: 640px) {
      .hero h1 { font-size: 1.6rem; }
      .container { padding: 0 1rem 2rem; }
      .header-inner { padding: 0.75rem 1rem; }
      .report-card { padding: 0.75rem 0.9rem; gap: 0.6rem; }
      .report-num { display: none; }
      .report-tag { font-size: 0.65rem; padding: 0.15rem 0.45rem; }
      .stats-row { gap: 0.4rem; }
    }
  </style>
</head>
<body>
  <div class="site-header">
    <div class="header-inner">
      <div class="logo">
        <div class="logo-icon"><svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5z" fill="rgba(255,255,255,0.15)" stroke="white" stroke-width="1.5"/><path d="M8 7h8M8 11h5" stroke="white" stroke-width="1.5" stroke-linecap="round"/><circle cx="16" cy="16" r="3.5" fill="white" fill-opacity="0.2" stroke="white" stroke-width="1.5"/><path d="M14.5 16l1 1 2-2" stroke="white" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <span class="logo-text">AI Report Hub</span>
      </div>
      <div class="theme-toggle" onclick="toggleTheme()" title="切換 Light/Dark 模式" role="button" tabindex="0">
        <div class="theme-toggle-thumb"></div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="hero">
      <h1>AI Report Hub</h1>
      <p>由 Claude AI 產製的 HTML 分析報告彙整</p>
      <div class="stats-row">
        <span class="stat-chip">&#128196; 共 """ + str(total) + """ 份報告</span>
        <span class="stat-chip">&#128193; """ + str(len(categories)) + """ 個分類</span>
        <span class="stat-chip">&#128337; 最後更新：""" + today + """</span>
      </div>
    </div>

    <div class="search-wrapper">
      <span class="search-icon">&#128269;</span>
      <input type="text" class="search-input" placeholder="搜尋報告..." oninput="onSearch()">
    </div>

    <div class="toolbar">
      <div class="filter-bar">
""" + filter_html + """      </div>
      <div class="view-toggle">
        <button class="view-btn active" data-view="grouped" onclick="switchView(this)">分組</button>
        <button class="view-btn" data-view="flat" onclick="switchView(this)">列表</button>
      </div>
    </div>

    <div id="grouped-view" class="report-list">
""" + grouped_html + """    </div>

    <div id="flat-view" class="report-list" style="display:none">
""" + flat_html + """    </div>

    <footer>
      Powered by <a href="#">Claude AI</a> &bull; Hosted on GitHub Pages
    </footer>
  </div>

  <script>
    (function() {
      var saved = localStorage.getItem('theme');
      if (saved) {
        document.documentElement.setAttribute('data-theme', saved);
      } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-theme', 'dark');
      }
    })();
    function toggleTheme() {
      var current = document.documentElement.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }
    function switchView(btn) {
      document.querySelectorAll('.view-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var v = btn.getAttribute('data-view');
      document.getElementById('grouped-view').style.display = v === 'grouped' ? '' : 'none';
      document.getElementById('flat-view').style.display = v === 'flat' ? '' : 'none';
      applyFilter();
    }
    function filterBy(btn) {
      document.querySelectorAll('.filter-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');
      applyFilter();
    }
    function applyFilter() {
      var active = document.querySelector('.filter-btn.active');
      var filter = active ? active.getAttribute('data-filter') : 'all';
      var search = document.querySelector('.search-input').value.toLowerCase();
      document.querySelectorAll('.report-card').forEach(function(card) {
        var cat = card.getAttribute('data-category');
        var title = card.querySelector('.report-title').textContent.toLowerCase();
        var catMatch = filter === 'all' || cat === filter;
        var searchMatch = !search || title.indexOf(search) !== -1;
        card.classList.toggle('hidden', !catMatch || !searchMatch);
      });
      document.querySelectorAll('.category-group').forEach(function(g) {
        var cat = g.getAttribute('data-category');
        var catMatch = filter === 'all' || cat === filter;
        if (!catMatch) { g.classList.add('hidden'); return; }
        var visibleCards = g.querySelectorAll('.report-card:not(.hidden)');
        g.classList.toggle('hidden', visibleCards.length === 0);
      });
    }
    function onSearch() { applyFilter(); }
  </script>
</body>
</html>
"""
    return html


def main():
    if not REPORTS_DIR.exists():
        REPORTS_DIR.mkdir(parents=True)
        print("建立 reports/ 資料夾")

    groups = scan_reports()
    total = sum(len(v) for v in groups.values())
    index_html = generate_index(groups)
    INDEX_PATH.write_text(index_html, encoding="utf-8")
    print("✅ index.html 已更新，共 " + str(total) + " 份報告，" + str(len(groups)) + " 個分類")


if __name__ == "__main__":
    main()
