# HAProxy 系列更新計劃

## 文件概覽

在 `tech-docs` 中有 3 套 HAProxy 相關文件：

| 文件集 | 路徑 | 文件採用版本 | 檔案數 |
|--------|------|-------------|--------|
| HAProxy Configuration Manual Cheat Sheet | `reports/haproxy-configuration-manual-cheat-sheet/` | HAProxy 3.0 | 13 |
| HAProxy ACL Cheat Sheet | `reports/haproxy-acl-cheatsheet/` | HAProxy 3.2 | 2 |
| HAProxy Starter Management Guide | `reports/haproxy-starter-management-guide-cheat-sheet/` | HAProxy 3.2 | 11 |

## 版本差異

HAProxy 版本制度：偶數版號 = LTS（~5年維護），奇數版號 = stable（~1年維護）

| 文件集 | 文件版本 (分支) | 同分支最新 | LTS 最新版 | 差距 |
|--------|----------------|-----------|-----------|------|
| Config Manual | HAProxy **3.0** (LTS) | 3.0.23 | **3.2.19** (LTS) | 落後 1 個 LTS 世代 |
| ACL Cheat Sheet | HAProxy **3.2** (LTS) | 3.2.19 | **3.2.19** (LTS) | 🟢 同分支最新 |
| Starter Guide | HAProxy **3.2** (LTS) | 3.2.19 | **3.2.19** (LTS) | 🟢 同分支最新 |

### 影響範圍

- **Config Manual (13 份文件)**：需要自 HAProxy 3.0 升級至 3.2 LTS。跨了一個 LTS 世代。
- **ACL + Starter Guide (13 份文件)**：3.2 LTS 只有點版本差異（3.2.0 → 3.2.19），無重大 API 變更，更新優先級低。

### HAProxy 3.0 → 3.2 LTS 主要變更

**3.0 → 3.2 跨世代變更：**

**3.1 (stable) — 2025-03：**
- 故障排除強化
- 設定可靠性改善
- QUIC 與 H2 效能提升
- 新的 SPOE 引擎
- 更細緻的錯誤報告

**3.2 (LTS) — 2025-05：**
- ACME & SSL 管理
- CPU 可擴展性改善
- QUIC 效能優化
- 故障排除強化

## 建議更新範圍

### Config Manual (reports/haproxy-configuration-manual-cheat-sheet/)

**高優先級** — 跨 LTS 世代，需要全面更新 13 份文件：

1. **Ch.1 HTTP 基礎**：更新 QUIC/HTTP/3 內容
2. **Ch.3 Global Parameters**：更新 ACME 相關 global 參數
3. **Ch.4 Proxies**：新增 `http-after-response`、新的 `http-reuse` 選項
4. **Ch.5 Bind & Server**：更新 SSL/TLS 設定章節，ACME 自動證書功能
5. **Ch.7 ACL & Samples**：新增取樣提取器
6. **Ch.8 Logging**：更新日誌格式內容

### ACL Cheat Sheet (reports/haproxy-acl-cheatsheet/)

**低優先級** — 僅點版本差異：
1. 檢查 ACL fetch 方法是否有新增/棄用
2. 更新 converter 參考

### Starter Management Guide (reports/haproxy-starter-management-guide-cheat-sheet/)

**低優先級** — 僅點版本差異：
1. Part 1 (架構)：更新架構圖提及 QUIC
2. Part 5 (Runtime/Security)：更新 ACME/SSL 最佳實踐
3. SSL Cookbook：更新 TLS 設定

## 參考資源

- HAProxy 官方版本支援表：https://www.haproxy.org/
- HAProxy 3.2 LTS 設定文件：https://www.haproxy.org/download/3.2/doc/configuration.txt
- HAProxy 3.2 LTS 原始碼：https://www.haproxy.org/download/3.2/src/
