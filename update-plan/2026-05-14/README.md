# Tech-Docs 更新計劃總表

**審計日期**：2026-05-14
**來源**：44 個分類目錄，約 650+ 份 HTML 報告
**重複標記**：`Observability/` ↔ `Prometheus-Grafana/`（61 份完全相同）

---

## 🔴 高優先級（大版本落後）

| 分類 | 內含技術 | 文件版本 | 最新版 | 差距 | 文件數 |
|------|---------|---------|-------|------|-------|
| `redis-cheat-sheet` | Redis | 7.4 | 8.6.3 | 🔴 8.6 全新功能 | 8 |
| `etcd-quickstart` | etcd | v3.5.x | v3.6.11 | 🔴 v3.6 新分支 | 5 |
| `k8s-ecosystem` | Helm | 3.8 | v4.2.0 / v3.21.0 | 🔴 4.x 重大變化 | 11 |
| `k8s-ecosystem` | K3s | ~v1.31 | v1.36.0+k3s1 | 🔴 多版落後 | 11 |
| `Observability/` | Grafana | 12.4 | v13.0.1+security-01 | 🔴 v13 新 UI | 61(dup) |
| `python-tutorial` | Python | 3.14 | 3.14.5 | 🟢 僅 patch（3.15 尚未 GA） | 31 |
| `Infisical` | Infisical | v0.158 | v0.159.28 | 🔴 0.x 快速迭代 | 7 |
| `proxy-guide` | Caddy | v2.11.1 | (需確認最新) | 🟡 已提及最新 | 16 |

## 🟡 中優先級（落後 1 小版或功能重大）

| 分類 | 內含技術 | 文件版本 | 最新版 | 差距 | 文件數 |
|------|---------|---------|-------|------|-------|
| `gsd-cheat-sheet` | GSD | v1.38.5 | v1.41.2 | 🟡 功能新增 | 4 |
| `playwright-cheat-sheet` | Playwright | v1.59 | v1.60.0 | 🟡 新功能 | 13 |
| `Observability/` | Prometheus | 3.11 | v3.11.3 | 🟢 僅 patch | 61(dup) |
| `Observability/` | Alertmanager | 0.32 | v0.32.1 | 🟢 僅 patch | 61(dup) |
| `go-tutorial` | Go | 1.26.2 | 1.26.3 | 🟢 僅 patch | 23 |
| `Ansible` | ansible-core | 2.20 | v2.20.5 | 🟢 僅 patch | 45 |

## 🟢 低優先級（點版本或版本中性）

| 分類 | 內含技術 | 文件版本 | 最新版 | 差距 |
|------|---------|---------|-------|------|
| `haproxy-*` (3份) | HAProxy 3.2 LTS | 3.2.x | 3.2.19 | 🟢 patch |
| `haproxy-config-*` | HAProxy 3.0 LTS | 3.0.x | 3.0.23 | 🟢 patch |
| `mysql-8_4-cheat-sheet` | MySQL | 8.4 | 8.4.9 | 🟢 patch |
| `postgresql-quickstart` | PostgreSQL | 18 | 18.4 | 🟢 patch |
| `kafka-cheat-sheet` | Apache Kafka | 4.2 | 4.2.0 | ✅ 相同 |
| `openbao` | OpenBao | v2.5.3 | v2.5.3 | ✅ 相同 |
| `OpenTofu` | OpenTofu | (need check) | v1.12.0 | ✅ |
| `bpftrace` | bpftrace | 0.25 | 0.25.1 | 🟢 patch |
| `nginx-cheat-sheet` | Nginx | 無特定版本 | 1.30.1(stable) | 🟢 版本中性 |

## ✅ 無需更新（版本中性或概念性內容）

| 分類 | 原因 |
|------|------|
| `ai-agent` | Hermes Agent 架構說明，無版本依賴 |
| `ai-infrastructure` | MCP/MCP Proxy 概念研究報告 |
| `ai-model` | Gemma 4 單一模型架構分析 |
| `ai-skills-workflows` | Superpowers/OpenSpec 概念報告 |
| `cgroup-v2` | Linux kernel 功能，非應用層版本 |
| `discord-quickstart` | Discord 訊息系統研究報告 |
| `eBPF` | eBPF 核心功能教學，非版本特定 |
| `javascript` | ECMAScript 2025 標準參考 |
| `js-ecosystem` | ECMAScript 2025 + nvm 工具參考 |
| `linux-cheat-sheet` | Linux 命令通用速查 |
| `markdown` | Markdown 語法參考 |
| `networking-guide` | 網路概念教學 |
| `shell-script` | Shell 腳本教學 |

## ⚠️ 重要額外發現

1. **Observability / Prometheus-Grafana 完全重複** — 61 份檔案內容完全相同（不同 inode），建議合併或移除一個
2. **Elasticsearch / Elasticsearch-Self-managed-CheatSheet** — 部分重疊，CheatSheet 可能為子集
3. **helm/helm 雙版本線** — v3.21.0 與 v4.2.0 並行，文件基於 v3.8，需決定是否涵蓋 4.x
4. **Nginx 無特定版本** — 文件未繫結特定版號，但內容可能過時（對比 stable 1.30.1 / mainline 1.31.0）
5. **Prometheus-Grafana/Observability** — 涵蓋 Prometheus 2.x ~ 3.x 範圍，需確認內容準確性
