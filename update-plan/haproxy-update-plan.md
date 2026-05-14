# HAProxy 系列更新計劃

## 文件概覽

在 `tech-docs` 中有 3 套 HAProxy 相關文件：

| 文件集 | 路徑 | 文件採用版本 | 檔案數 |
|--------|------|-------------|--------|
| HAProxy Configuration Manual Cheat Sheet | `reports/haproxy-configuration-manual-cheat-sheet/` | HAProxy 3.0 | 13 |
| HAProxy ACL Cheat Sheet | `reports/haproxy-acl-cheatsheet/` | HAProxy 3.2 | 2 |
| HAProxy Starter Management Guide | `reports/haproxy-starter-management-guide-cheat-sheet/` | HAProxy 3.2 | 11 |

## 版本差異

| 文件集 | 當前版本 | 最新穩定版 | 差距 |
|--------|---------|-----------|------|
| Config Manual | HAProxy 3.0 | HAProxy 3.3.0 | 落後 3 個大版本 (3.1 → 3.2 → 3.3) |
| ACL + Starter Guide | HAProxy 3.2 | HAProxy 3.3.0 | 落後 1 個小版本 |

### HAProxy 3.0 → 3.3 主要變更

**3.0 → 3.1：**
- 新增 `http-after-response` 規則
- QUIC 及 HTTP/3 改進
- OCSP stapling 增強
- 新的取樣提取器 (fetches)

**3.1 → 3.2：**
- `ssl` 初始化效能優化
- 連接池 (connection pool) 管理強化
- 新的 `set-var`/`unset-var` 動作
- 日誌格式擴充

**3.2 → 3.3：**
- 2026-03 釋出
- HTTP/3 預設啟用 (quic)
- 新的 `http-reuse` 模式
- 增強的路由匹配
- SSL/TLS 1.3 設定強化
- 動態 server 管理功能擴充

## 建議更新範圍

### Config Manual (reports/haproxy-configuration-manual-cheat-sheet/)

**高優先級** — 需要全面更新 13 份文件：

1. **Ch.1 HTTP 基礎**：更新 QUIC/HTTP/3 內容
2. **Ch.3 Global Parameters**：更新 QUIC 相關 global 參數
3. **Ch.4 Proxies**：新增 `http-after-response`、新 `http-reuse` 選項
4. **Ch.5 Bind & Server**：更新 SSL/TLS 設定章節，新增動態 server 管理
5. **Ch.7 ACL & Samples**：新增取樣提取器
6. **Ch.8 Logging**：更新日誌格式內容

### ACL Cheat Sheet (reports/haproxy-acl-cheatsheet/)

**低優先級** — 局部更新：

1. 檢查 ACL fetch 方法是否有新增/棄用
2. 更新 converter 參考
3. 如有新條件式範例可補充

### Starter Management Guide (reports/haproxy-starter-management-guide-cheat-sheet/)

**低優先級** — 局部更新：

1. Part 1 (架構)：更新架構圖提及 HTTP/3
2. Part 5 (Runtime/Security)：更新 SSL 最佳實踐
3. SSL Cookbook：更新 TLS 1.3 設定

## 參考資源

- HAProxy 官方文件：https://www.haproxy.org/download/3.3/doc/configuration.txt
- HAProxy 最新穩定版下載：https://www.haproxy.org/
- HAProxy 3.3 發行公告 (2026-03)
