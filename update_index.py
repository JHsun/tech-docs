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


def build_card_html(report):
    date_html = ""
    if report["date"]:
        date_html = '      <span class="report-date">' + report["date"] + "</span>\n"
    else:
        date_html = '      <span class="report-date">—</span>\n'

    return (
        '    <a class="report-card" href="reports/' + report["rel_path"] + '"'
        ' data-category="' + report["category"] + '">\n'
        + date_html
        + '      <span class="report-title">' + report["title"] + "</span>\n"
        '      <span class="report-tag">' + (report["category"] if report["category"] != "_uncategorized" else "其他") + "</span>\n"
        "    </a>\n"
    )


def generate_index(groups):
    today = datetime.now().strftime("%Y-%m-%d")
    total = sum(len(v) for v in groups.values())
    categories = [k for k in groups.keys() if k != "_uncategorized"]

    # --- build grouped view ---
    grouped_html = ""
    for cat, reports in groups.items():
        display_name = "其他" if cat == "_uncategorized" else cat
        grouped_html += '    <div class="category-group" data-category="' + cat + '">\n'
        grouped_html += '      <h2 class="category-title">' + display_name + ' <span class="category-count">' + str(len(reports)) + "</span></h2>\n"
        for r in reports:
            grouped_html += "  " + build_card_html(r)
        grouped_html += "    </div>\n"

    # --- build flat view ---
    all_reports = []
    for reports in groups.values():
        all_reports.extend(reports)
    all_reports.sort(key=lambda r: r["filename"], reverse=True)

    flat_html = ""
    for r in all_reports:
        flat_html += build_card_html(r)

    # --- build filter buttons ---
    filter_html = '      <button class="filter-btn active" data-filter="all" onclick="filterBy(this)">全部</button>\n'
    for cat in categories:
        filter_html += '      <button class="filter-btn" data-filter="' + cat + '" onclick="filterBy(this)">' + cat + "</button>\n"
    if "_uncategorized" in groups:
        filter_html += '      <button class="filter-btn" data-filter="_uncategorized" onclick="filterBy(this)">其他</button>\n'

    if total == 0:
        grouped_html = '    <div class="empty">尚無報告，請新增第一份報告。</div>\n'
        flat_html = grouped_html

    # --- assemble page ---
    html = (
        "<!DOCTYPE html>\n"
        '<html lang="zh-TW">\n'
        "<head>\n"
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        "  <title>AI Report Hub</title>\n"
        "  <style>\n"
        "    :root {\n"
        "      --bg: #faf9f6; --card-bg: #ffffff; --text: #2c2c2a;\n"
        "      --text-muted: #888780; --accent: #534AB7; --accent-light: #EEEDFE;\n"
        "      --border: #e8e6df; --tag-ai: #E1F5EE; --tag-ai-text: #0F6E56;\n"
        "    }\n"
        "    @media (prefers-color-scheme: dark) {\n"
        "      :root {\n"
        "        --bg: #1a1a1a; --card-bg: #252525; --text: #e0ddd5;\n"
        "        --text-muted: #9c9a92; --accent: #AFA9EC; --accent-light: #26215C;\n"
        "        --border: #3a3a38; --tag-ai: #04342C; --tag-ai-text: #5DCAA5;\n"
        "      }\n"
        "    }\n"
        "    * { margin: 0; padding: 0; box-sizing: border-box; }\n"
        "    body {\n"
        '      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;\n'
        "      background: var(--bg); color: var(--text);\n"
        "      line-height: 1.6; padding: 2rem 1rem; max-width: 860px; margin: 0 auto;\n"
        "    }\n"
        "    header { text-align: center; margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border); }\n"
        "    header h1 { font-size: 1.8rem; font-weight: 600; margin-bottom: 0.4rem; }\n"
        "    header p { color: var(--text-muted); font-size: 0.95rem; }\n"
        "    .stats { display: flex; gap: 1.5rem; justify-content: center; margin-top: 1rem; }\n"
        "    .stat { background: var(--accent-light); color: var(--accent); padding: 0.3rem 0.9rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500; }\n"
        "    .toolbar { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem; }\n"
        "    .filter-bar { display: flex; gap: 0.4rem; flex-wrap: wrap; flex: 1; }\n"
        "    .filter-btn {\n"
        "      background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px;\n"
        "      padding: 0.25rem 0.75rem; font-size: 0.82rem; cursor: pointer; color: var(--text-muted);\n"
        "      transition: all 0.2s;\n"
        "    }\n"
        "    .filter-btn:hover { border-color: var(--accent); color: var(--accent); }\n"
        "    .filter-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }\n"
        "    .view-toggle {\n"
        "      display: flex; gap: 0; border: 1px solid var(--border); border-radius: 8px; overflow: hidden;\n"
        "    }\n"
        "    .view-btn {\n"
        "      background: var(--card-bg); border: none; padding: 0.35rem 0.7rem; font-size: 0.82rem;\n"
        "      cursor: pointer; color: var(--text-muted); transition: all 0.2s;\n"
        "    }\n"
        "    .view-btn:not(:last-child) { border-right: 1px solid var(--border); }\n"
        "    .view-btn.active { background: var(--accent); color: #fff; }\n"
        "    .report-list { display: flex; flex-direction: column; gap: 0.75rem; }\n"
        "    .report-card {\n"
        "      display: flex; align-items: center; gap: 1rem;\n"
        "      padding: 1rem 1.2rem; background: var(--card-bg);\n"
        "      border: 1px solid var(--border); border-radius: 10px;\n"
        "      text-decoration: none; color: inherit;\n"
        "      transition: border-color 0.2s, box-shadow 0.2s;\n"
        "    }\n"
        "    .report-card:hover { border-color: var(--accent); box-shadow: 0 2px 12px rgba(83,74,183,0.08); }\n"
        "    .report-card.hidden { display: none; }\n"
        "    .report-date { font-size: 0.8rem; color: var(--text-muted); min-width: 90px; font-variant-numeric: tabular-nums; }\n"
        "    .report-title { font-weight: 500; flex: 1; }\n"
        "    .report-tag {\n"
        "      font-size: 0.75rem; padding: 0.2rem 0.6rem; border-radius: 12px;\n"
        "      background: var(--tag-ai); color: var(--tag-ai-text); font-weight: 500; white-space: nowrap;\n"
        "    }\n"
        "    .category-group { margin-bottom: 1.5rem; }\n"
        "    .category-group.hidden { display: none; }\n"
        "    .category-title {\n"
        "      font-size: 1.1rem; font-weight: 600; margin-bottom: 0.6rem;\n"
        "      padding-left: 0.3rem; display: flex; align-items: center; gap: 0.5rem;\n"
        "    }\n"
        "    .category-count {\n"
        "      font-size: 0.75rem; font-weight: 500; background: var(--accent-light);\n"
        "      color: var(--accent); padding: 0.1rem 0.5rem; border-radius: 10px;\n"
        "    }\n"
        "    footer { text-align: center; margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border); color: var(--text-muted); font-size: 0.82rem; }\n"
        "    .empty { text-align: center; padding: 3rem; color: var(--text-muted); }\n"
        "  </style>\n"
        "</head>\n"
        "<body>\n"
        "  <header>\n"
        "    <h1>\U0001f4ca AI Report Hub</h1>\n"
        "    <p>由 Claude AI 產製的 HTML 分析報告彙整</p>\n"
        '    <div class="stats">\n'
        '      <span class="stat">共 ' + str(total) + " 份報告</span>\n"
        '      <span class="stat">' + str(len(categories)) + " 個分類</span>\n"
        '      <span class="stat">最後更新：' + today + "</span>\n"
        "    </div>\n"
        "  </header>\n"
        '  <div class="toolbar">\n'
        '    <div class="filter-bar">\n'
        + filter_html
        + "    </div>\n"
        '    <div class="view-toggle">\n'
        '      <button class="view-btn active" data-view="grouped" onclick="switchView(this)">分組</button>\n'
        '      <button class="view-btn" data-view="flat" onclick="switchView(this)">列表</button>\n'
        "    </div>\n"
        "  </div>\n"
        '  <div id="grouped-view" class="report-list">\n'
        + grouped_html
        + "  </div>\n"
        '  <div id="flat-view" class="report-list" style="display:none">\n'
        + flat_html
        + "  </div>\n"
        "  <footer>\n"
        "    Powered by Claude AI &bull; Hosted on GitHub Pages\n"
        "  </footer>\n"
        "  <script>\n"
        "    function switchView(btn) {\n"
        "      document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));\n"
        "      btn.classList.add('active');\n"
        "      var v = btn.getAttribute('data-view');\n"
        "      document.getElementById('grouped-view').style.display = v === 'grouped' ? '' : 'none';\n"
        "      document.getElementById('flat-view').style.display = v === 'flat' ? '' : 'none';\n"
        "      applyFilter();\n"
        "    }\n"
        "    function filterBy(btn) {\n"
        "      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));\n"
        "      btn.classList.add('active');\n"
        "      applyFilter();\n"
        "    }\n"
        "    function applyFilter() {\n"
        "      var active = document.querySelector('.filter-btn.active');\n"
        "      var filter = active ? active.getAttribute('data-filter') : 'all';\n"
        "      document.querySelectorAll('.report-card').forEach(function(card) {\n"
        "        var cat = card.getAttribute('data-category');\n"
        "        card.classList.toggle('hidden', filter !== 'all' && cat !== filter);\n"
        "      });\n"
        "      document.querySelectorAll('.category-group').forEach(function(g) {\n"
        "        var cat = g.getAttribute('data-category');\n"
        "        g.classList.toggle('hidden', filter !== 'all' && cat !== filter);\n"
        "      });\n"
        "    }\n"
        "  </script>\n"
        "</body>\n"
        "</html>\n"
    )
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
