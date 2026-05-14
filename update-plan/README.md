# Tech-Docs 更新計劃總表

生成日期：2026-05-14
掃描範圍：`reports/` 下 45 個主題目錄，共 652 份 HTML 教學文件
版本查詢方式：GitHub Releases API (`gh api repos/.../releases/latest`) + 官方網站

## 版本比對一覽

### 🔴 高優先級 — 大版本落後，需較大更新

| 主題 | 文件版本 | 最新版本 | 差距 | 文件數 |
|------|---------|----------|------|--------|
| HAProxy Config Manual | 3.0 | 3.3.0 (2026-03) | 落後 3 大版本 | 13 |
| etcd | v3.5.21 | v3.6.11 (2026-05) | 含 breaking changes | 5 |
| Redis | 7.4 | 8.6.3 (2026-05) | 大版本跳躍 7→8 | 8 |
| Keepalived | v1.4 | 2.3.4 | 大版本跳躍 1→2 | 3 |
| GSD | v1.38.5 | v2.82.0 (2026-05) | 大幅落後 | 4 |
| Helm | 3.8 | v4.2.0 (2026-05) | 大版本跳躍 3→4 | 1 |
| Kubernetes | v1.24–1.32 | v1.36.1 (2026-05) | 落後 4–5 版 | 6 |

### 🟡 中優先級 — 落後 1 大版本或多次小版

| 主題 | 文件版本 | 最新版本 | 文件數 |
|------|---------|----------|--------|
| Grafana | 11–12 | 13.0.1 (2026-05) | 60* |
| Prometheus | 2.40/3.0 | 3.11.3 (2026-04) | 60* |
| Python | 3.14 | 3.15.0 | 30 |
| Elasticsearch | 9.x | 9.4.1 (2026-05) | 78 |
| OpenTofu | 1.6–1.11 | 1.12.0 (2026-05) | 22 |
| k3s | v1.20–1.30 | v1.36.0+k3s1 (2026-05) | 1 |

*\* Observability/ 與 Prometheus-Grafana/ 內容完全重複（60 份 × 2），實際應計為 60 份。*

### 🟢 低優先級 — 點版本落後或不確定

| 主題 | 文件版本 | 最新版本 | 說明 |
|------|---------|----------|------|
| HAProxy ACL/Starter | 3.2 | 3.3.0 | 小版落後 |
| Playwright | v1.59 | v1.60.0 (2026-05) | 小版落後 |
| Infisical | v0.158 | v0.159.28 (2026-05) | 小版落後 |
| Nginx | 未標示 | 1.31.0 (2026-05) | 需審視 |
| MySQL | 8.4 | 8.4.9 | 同系列點版本 |
| Claude Code | 2026-03 校對 | v2.1.141 (2026-05) | 2 個月迭代 |
| Hermes Agent | 未標示 | v2026.5.7 (2026-05) | 持續迭代 |
| Bifrost AI Gateway | v1.5 | 無法確認上游 | 需確認專案狀態 |
| OpenTelemetry | 未標示 | Collector v0.152.0 | 概念性內容 |

### ✅ 無需更新

| 主題 | 文件版本 | 最新版本 | 備註 |
|------|---------|----------|------|
| Ansible | ansible-core 2.10–2.20 | 2.20.5 | 上界一致 |
| bpftrace | 0.25 | 0.25.1 | 僅 patch |
| OpenBao | v2.5.3 | v2.5.3 | 完全一致 |
| Kafka | 4.2 | 4.2.0 | 完全一致 |
| PostgreSQL | 18 | 18.3 | 同系列 |
| ECMAScript | 2025 (16th) | es2025 (2025-06) | 無 ES2026 |
| Go | 1.22–1.26 | 1.26.3 | 上界一致 |
| Bash | 5.0–5.3 | 5.3 | 上界一致 |
| FastAPI | — | 0.136.1 | 版本中性 |
| Node.js | — | v26.1.0 | 版本中性 |
| GitLab | — | — | 版本中性 |
| cgroup-v2 | — | Kernel API | Stable |
| eBPF | — | Kernel API | Stable |
| proxy-guide | — | — | 概念性 |
| networking-guide | 2026 | — | 近期內容 |
| markdown | — | — | Spec 層級 |
| linux-cheat-sheet | — | — | 工具用法 |
| shell-script | — | Bash 5.3 | 上界一致 |
| discord-quickstart | — | — | API 層級 |
| MCP / AI Infrastructure | 近期 | — | 協定層級 |

## 建議處理順序

1. **清理 duplicate**：`Prometheus-Grafana/` 與 `Observability/` 擇一保留
2. **🔴 高優先**：HAProxy (config manual) → etcd → Redis → Keepalived → GSD → Helm → K8s
3. **🟡 中優先**：Grafana/Prometheus → Python → Elasticsearch → OpenTofu → k3s
4. **🟢 低優先**：其餘點版本更新

詳細差異分析與更新範圍，請參閱各主題對應的 `*-update-plan.md` 檔案。
