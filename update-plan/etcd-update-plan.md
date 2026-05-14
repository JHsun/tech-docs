# etcd 更新計劃

## 文件概覽

| 路徑 | 檔案數 |
|------|--------|
| `reports/etcd-quickstart/` | 5 |

## 文件版本確認

從文件內容取得：
- **版本**：v3.5（badge），程式碼範例使用 v3.5.21
- **來源**：`etcd.io 官方文件`（`https://etcd.io/docs/v3.5/`）
- **產製日期**：未明確標示

## 官方版本查證

查詢 `etcd.io` 官網 + GitHub Releases：

| Branch | 狀態 | 最新版號 |
|--------|------|---------|
| v3.7 | DRAFT（開發中） | — |
| **v3.6** | **latest stable** | **v3.6.11** (2026-05-01) |
| v3.5 | maintained（文件基礎） | v3.5.30 |
| v3.4 | maintained | v3.4.44 |

etcd 不使用 LTS 命名，同時維護多個穩定分支。**v3.6** 為目前最新穩定版。

## 版本差異

| 文件使用 | 同分支最新 | 最新穩定版 | 差距 |
|---------|-----------|-----------|------|
| v3.5.21 | v3.5.30 | **v3.6.11** | 跨一個穩定世代 |

### v3.5 → v3.6 主要變更

從 v3.6 CHANGELOG 提取：

**安全性修正（重要）：**
- CVE-2026-33413: 多個 API 授權繞過修正
- CVE-2026-33343: 巢狀 transaction RBAC 繞過修正
- RBAC read bypass via PrevKv/lease in txn

**功能變更：**
- `--max-snapshots` flag 延後至 v3.8 移除
- `--snapshot-count` flag 取消棄用
- OTEL gRPC interceptor 更新（`NewServerHandler` 取代舊版）
- clientv3 naming/endpoints Metadata 欄位標記 deprecated
- Prometheus metrics 強化
- golang 版本升級（go 1.25.x）

**Breaking Changes：**
- V2 discovery protocol 標記 deprecated
- `etcdctl defrag --data-dir` 移除
- `etcdctl snapshot status` / `etcdctl snapshot restore` 移除（改用 `etcdutl`）
- `SetKeepAlive` / `SetKeepAlivePeriod` 移除
- gRPC resolver API 變更（`Addresses` → `Endpoint.Addresses`）

## 建議更新範圍

### 全部 5 份文件

1. **Overview & Commands** — 更新版本號、Docker image tag、安裝指令
2. **Data Model & API** — 確認 v3.6 API 相容性（無重大 API 格式變更）
3. **Cluster & Security** — 更新安全設定最佳實踐（有 CVE 修補）
4. **Config & Recovery** — 注意 deprecated flag，更新建議配置
5. **Tuning, Metrics & Upgrade** — 更新 metrics、新增升級指南

### 優先級

- 🟡 中優先級 — v3.6 功能變動不大，但安全性修補重要
- 如果文件僅供參考而非教學實作，可暫緩更新

## 參考資源

- 官方文檔：https://etcd.io/docs/v3.6/
- GitHub Releases：https://github.com/etcd-io/etcd/releases
- CHANGELOG 3.6：https://github.com/etcd-io/etcd/blob/main/CHANGELOG/CHANGELOG-3.6.md
- 從 3.5 升級至 3.6：https://etcd.io/docs/v3.6/upgrade/
