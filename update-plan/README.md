# Tech-Docs 更新計劃總表

生成日期：2026-05-14（v2，全面查證版）
掃描範圍：`reports/` 下 45 個分類目錄，652 份 HTML 教學文件
方法：逐文件讀取標題與版本標籤 → 識別所有內含技術 → 查證官方穩定/LTS版 → 比對差異

## 技術清單與版本對照

### 🔴 高優先級（大版本落後，需較大更新）

| 分類目錄 | 內含技術 | 文件版本 | 最新穩定/LTS版 | 差距說明 | 文件數 |
|---------|---------|---------|---------------|---------|--------|
| haproxy-configuration-manual-cheat-sheet | HAProxy | 3.0 LTS | **3.2.19** (LTS) | 跨 1 個 LTS 世代 | 13 |
| etcd-quickstart | etcd | v3.5.21 | **v3.6.11** (stable) | 含 CVE 修補 + flag 移除 | 5 |
| redis-cheat-sheet | Redis | 7.4 | **8.6.3** (stable) | 大版本 7→8 | 8 |
| keepalived-cheat-sheet | Keepalived | v1.4.3 | **2.3.4** (stable) | 大版本 1→2 | 3 |
| k8s-ecosystem | Kubernetes | v1.24–1.32 | **v1.36.1** | 落後 4 版 | 6 |
| k8s-ecosystem | Helm | 3.8 | **3.21.0** (3.x) / **v4.2.0** | 落後多版 + 有 4.x | 1 |
| k8s-ecosystem | k3s | v1.10–1.30 | **v1.36.0+k3s1** | 落後多版 | 1 |
| gsd-cheat-sheet | GSD | v1.38.5 | **v1.41.2** | 小版落後 | 4 |

### 🟡 中優先級（落後 1 大版或多次小版）

| 分類目錄 | 內含技術 | 文件版本 | 最新穩定版 | 差距說明 | 文件數 |
|---------|---------|---------|-----------|---------|--------|
| Observability | Prometheus | 3.11.2 | **v3.11.3** | 極小差距 | 60* |
| Observability | Grafana | v12.4 | **v13.0.1** | 落後 1 大版 | 60* |
| Observability | Alertmanager | —（無明確版號） | v0.32.1 | — | 60* |
| Observability | Loki | — | v3.7.2 | — | 60* |
| Observability | Tempo | — | v2.10.5 | — | 60* |
| Observability | Mimir | — | 3.0.6 | — | 60* |
| Observability | Pyroscope | — | v2.0.2 | — | 60* |
| Observability | Alloy | — | v1.16.1 | — | 60* |
| Observability | k6 | — | v2.0.0 | — | 60* |
| python-tutorial | Python | 3.14 | **3.15.0** | 落後 1 小版 | 30 |
| elasticsearch | Elasticsearch | 9.x | **v9.4.1** | 需確認子版本 | 78 |
| OpenTofu | OpenTofu | 1.6–1.11 | **v1.12.0** | 落後 1 小版 | 22 |
| etcd-quickstart | etcd | v3.5.21 | v3.5.30（同分支） | 點版本落後 | 5 |
| haproxy-acl-cheatsheet | HAProxy | 3.2 LTS | 3.2.19（同分支） | 僅點版本 | 2 |
| haproxy-starter-management-guide-cheat-sheet | HAProxy | 3.2 LTS | 3.2.19（同分支） | 僅點版本 | 11 |

*\* Observability/ 與 Prometheus-Grafana/ 完全重複，實際為 60 份。*

### 🟢 低優先級（點版本或版本中性）

| 分類目錄 | 內含技術 | 文件版本 | 最新版 | 判定 |
|---------|---------|---------|-------|------|
| playwright-cheat-sheet | Playwright | v1.59 | v1.60.0 | 小版 |
| Infisical | Infisical | v0.158 | v0.159.28 | 小版 |
| nginx-cheat-sheet | Nginx | 未標示 | **1.30.1 (Stable)** | 需審視 |
| mysql-8_4-cheat-sheet | MySQL | 8.4 | 8.4.9 | 同系列 |
| claude-code-quickstart | Claude Code | v2.1.114 | v2.1.141 | 小版 |
| ai-agent | Hermes Agent | — | v2026.5.7 | 持續迭代 |
| bifrost-cheat-sheet | Bifrost AI Gateway | v1.5.0 | npm 1.6.2 | 需釐清對應 |
| OpenTelemetry | OTel Collector | v0.150.0 | v0.152.0 | 小版 |
| postgresql-quickstart | PostgreSQL | 18 | **18.3** ✅ | 同系列 |
| go-tutorial | Go | 1.26 | **1.26.3** ✅ | 同系列 |
| linux-cheat-sheet | tmux | 3.6a | **3.6a** ✅ | 一致 |
| js-ecosystem | nvm | v0.40.4 | **v0.40.4** ✅ | 一致 |
| netowkring-guide | WireGuard | kernel 版號 | v1.0.20260223 | 概念性 |
| ai-skills-workflows | OpenSpec | v1.1 | — | 無法確認上游 |
| ai-skills-workflows | Superpowers | v5.0.5 | — | 無法確認上游 |

### ✅ 無需更新（版本中性或一致）

Ansible (ansible-core 2.20)、Kafka 4.2、Bash 5.3、AWK、sed、Linux commands、ECMAScript 2025、OpenBao v2.5.3、bpftrace 0.25、FastAPI、Node.js、Discord API、cgroup-v2、eBPF、proxy-guide、markdown、shell-script、GitLab、Redmine

## ⚠️ 重要額外發現

1. **Observability/ 與 Prometheus-Grafana/ 完全重複** — 60 份 identical copies，建議擇一保留
2. **haupgrade-configuration-manual-cheat-sheet/ 內含兩套子集** — 01-06 與 07-13 涵蓋相同章節
3. **Helm 有雙線發展** — 3.x 仍在維護（最新 v3.21.0），同時有 v4.x
4. **Claude Code doc 已自帶 v2.1.114** — 更新頻率高，文件迭代速度接近官版
5. **Superpowers 與 OpenSpec** — 無法從 GitHub 找到明確上游 repo

## 建議處理順序

1. **清理 duplicate**：Prometheus-Grafana/ vs Observability/
2. **🔴 高優先**：HAProxy Config (3.0→3.2) → etcd → Redis → Keepalived → K8s/Helm/k3s → GSD
3. **🟡 中優先**：Grafana (12→13) → Python → Elasticsearch → OpenTofu
4. **🟢 低優先**：其餘點版本更新 + 無法確認上游者

詳細分析及更新範圍請參閱各 `*-update-plan.md`。
