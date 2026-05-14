# etcd 更新計劃

## 文件概覽

| 路徑 | 檔案數 |
|------|--------|
| `reports/etcd-quickstart/` | 5 |

## 版本差異

| 文件採用版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| v3.5.21 | v3.6.11 (2026-05-01) | ⚠️ 大版本更新 (3.5 → 3.6) |

## 主要變更 (3.5 → 3.6)

etcd v3.6 是重要的版本更新，包含 **breaking changes**：

### Breaking Changes
- **v3 API 變更**：部分 v3 API 行為調整
- **棄用功能**：部分舊有 flag 與設定已被標記 deprecated
- **儲存引擎更新**：進一步最佳化 boltdb/bbolt 使用
- **TLS 設定強化**：最低 TLS 版本要求提高
- **watch 機制改進**：watch response 格式有調整

### 新功能
- 更好的並發控制與效能
- 更嚴格的權限檢查
- 改良的 compaction 機制
- 新的 metrics 端點

## 建議更新範圍

### 全部 5 份文件需更新：

1. **Overview & Commands** (`etcd-cheatsheet-1-overview-commands.html`)
   - 更新 `ETCD_VER=v3.6.11`
   - 更新安裝指令中的版本號與 Docker image tag
   - 檢查 CLI 指令是否有新增/變更

2. **Data Model & API** (`etcd-cheatsheet-2-datamodel-api.html`)
   - 🔴 **重點更新**：v3.6 API 變更
   - 檢查 watch API、lease API 是否有 breaking change
   - 檢查 v3 API 端點回應格式是否變更

3. **Cluster & Security** (`etcd-cheatsheet-3-cluster-security.html`)
   - 更新 TLS 最佳實踐 (v3.6 有強化)
   - 檢查安全設定參數

4. **Config & Recovery** (`etcd-cheatsheet-4-config-recovery.html`)
   - 檢查設定檔 flag 是否有 deprecated 項目
   - 更新建議配置

5. **Tuning, Metrics & Upgrade** (`etcd-cheatsheet-5-tuning-metrics-upgrade.html`)
   - 新增 3.5→3.6 升級指南
   - 更新 metrics 端點與 prometheus 配置
   - 效能調校建議更新 (儲存引擎改善)

## 參考資源

- Release: https://github.com/etcd-io/etcd/releases/tag/v3.6.11
- Upgrade guide: https://etcd.io/docs/v3.6/upgrade/
- 建議在 v3.6 環境完整測試後再更新文件
