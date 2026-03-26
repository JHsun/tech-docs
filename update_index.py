#!/usr/bin/env python3
"""
update_index.py — 掃描 reports/ 資料夾，自動重新產生 index.html
"""

import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent
REPORTS_DIR = REPO_ROOT / "reports"
INDEX_PATH = REPO_ROOT / "index.html"

TEMPLATE_CSS = """    :root {
      --bg: #faf9f6; --card-bg: #ffffff; --text: #2c2c2a;
      --text-muted: #888780; --accent: #534AB7; --accent-light: #EEEDFE;
      --border: #e8e6df; --tag-ai: #E1F5EE; --tag-ai-text: #0F6E56;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #1a1a1a; --card-bg: #252525; --text: #e0ddd5;
        --text-muted: #9c9a92; --accent: #AFA9EC; --accent-light: #26215C;
        --border: #3a3a38; --tag-ai: #04342C; --tag-ai-text: #5DCAA5;
      }
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg); color: var(--text);
      line-height: 1.6; padding: 2rem 1rem; max-width: 860px; margin: 0 auto;
    }
    header { text-align: center; margin-bottom: 2.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border); }
    header h1 { font-size: 1.8rem; font-weight: 600; margin-bottom: 0.4rem; }
    header p { color: var(--text-muted); font-size: 0.95rem; }
    .stats { display: flex; gap: 1.5rem; justify-content: center; margin-top: 1rem; }
    .stat { background: var(--accent-light); color: var(--accent); padding: 0.3rem 0.9rem; border-radius: 20px; font-size: 0.85rem; font-weight: 500; }
    .report-list { display: flex; flex-direction: column; gap: 0.75rem; }
    .report-card {
      display: flex; align-items: center; gap: 1rem;
      padding: 1rem 1.2rem; background: var(--card-bg);
      border: 1px solid var(--border); border-radius: 10px;
      text-decoration: none; color: inherit;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .report-card:hover { border-color: var(--accent); box-shadow: 0 2px 12px rgba(83,74,183,0.08); }
    .report-date { font-size: 0.8rem; color: var(--text-muted); min-width: 90px; font-variant-numeric: tabular-nums; }
    .report-title { font-weight: 500; flex: 1; }
    .report-tag { font-size: 0.75rem; padding: 0.2rem 0.6rem; border-radius: 12px; background: var(--tag-ai); color: var(--tag-ai-text); font-weight: 500; white-space: nowrap; }
    footer { text-align: center; margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid var(--border); color: var(--text-muted); font-size: 0.82rem; }
    .empty { text-align: center; padding: 3rem; color: var(--text-muted); }"""


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
    return match.group(1) if match else "未知日期"


def generate_index(reports):
    today = datetime.now().strftime("%Y-%m-%d")
    count = len(reports)

    cards_html = ""
    for r in reports:
        cards_html += (
            '    <a class="report-card" href="reports/' + r["filename"] + '">\n'
            '      <span class="report-date">' + r["date"] + "</span>\n"
            '      <span class="report-title">' + r["title"] + "</span>\n"
            '      <span class="report-tag">Claude</span>\n'
            "    </a>\n"
        )

    if not cards_html:
        list_content = '    <div class="empty">尚無報告，請新增第一份報告。</div>\n'
    else:
        list_content = cards_html

    html = (
        "<!DOCTYPE html>\n"
        '<html lang="zh-TW">\n'
        "<head>\n"
        '  <meta charset="UTF-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        "  <title>AI Report Hub</title>\n"
        "  <style>\n"
        + TEMPLATE_CSS
        + "\n  </style>\n"
        "</head>\n"
        "<body>\n"
        "  <header>\n"
        "    <h1>📊 AI Report Hub</h1>\n"
        "    <p>由 Claude AI 產製的 HTML 分析報告彙整</p>\n"
        '    <div class="stats">\n'
        '      <span class="stat">共 ' + str(count) + " 份報告</span>\n"
        '      <span class="stat">最後更新：' + today + "</span>\n"
        "    </div>\n"
        "  </header>\n"
        '  <div class="report-list">\n'
        + list_content
        + "  </div>\n"
        "  <footer>\n"
        "    Powered by Claude AI &bull; Hosted on GitHub Pages\n"
        "  </footer>\n"
        "</body>\n"
        "</html>\n"
    )
    return html


def main():
    if not REPORTS_DIR.exists():
        REPORTS_DIR.mkdir(parents=True)
        print("建立 reports/ 資料夾")

    html_files = sorted(
        [f for f in REPORTS_DIR.iterdir() if f.suffix == ".html"],
        key=lambda f: f.name,
        reverse=True,
    )
    reports = []
    for f in html_files:
        reports.append(
            {
                "filename": f.name,
                "date": extract_date(f.name),
                "title": extract_title(f),
            }
        )

    index_html = generate_index(reports)
    INDEX_PATH.write_text(index_html, encoding="utf-8")
    print("✅ index.html 已更新，共 " + str(len(reports)) + " 份報告")


if __name__ == "__main__":
    main()
