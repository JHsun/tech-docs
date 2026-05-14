# Keepalived 更新計劃

## 文件概覽

| 路徑 | 檔案數 |
|------|--------|
| `reports/keepalived-cheat-sheet/` | 3 |

## 版本差異

| 文件採用版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| v1.4 | 2.3.4 | ⚠️ 大版本跳躍 (1.x → 2.x) |

## 主要變更 (1.x → 2.x)

Keepalived 從 v1 到 v2 有大量變化：

- **核心重構**：VRRP 實作重大更新
- **設定語法變更**：部分 v1 設定格式不再支援
- **新的健康檢查類型**：更多 check 選項
- **IPv6 支援強化**
- **SNMP 監控增強**
- **新的通知機制**

## 建議更新範圍

### 全部 3 份文件需重寫

1. **Part 1: Concepts, Architecture, Installation**
   - 更新 VRRP 實作說明
   - 安裝步驟改用 v2.3.x 版本
   - 重新審視核心概念是否仍然準確

2. **Part 2 & Part 3**
   - 全面更新設定範例 (v1 語法可能不相容)
   - 新增 v2 特有功能說明
   - 健康檢查設定更新
   - 通知與監控設定更新

## 參考資源

- Keepalived 官網：https://www.keepalived.org/
- 版本歷史：https://www.keepalived.org/changelog.html
