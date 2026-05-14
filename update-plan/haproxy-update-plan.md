# HAProxy 系列更新計劃

## 文件概覽

| 文件集 | 路徑 | 文件版本 | 檔案數 |
|--------|------|---------|--------|
| HAProxy Configuration Manual Cheat Sheet | `reports/haproxy-configuration-manual-cheat-sheet/` | HAProxy **3.0 LTS** | 13 |
| HAProxy ACL Cheat Sheet | `reports/haproxy-acl-cheatsheet/` | HAProxy **3.2 LTS** | 2 |
| HAProxy Starter Management Guide | `reports/haproxy-starter-management-guide-cheat-sheet/` | HAProxy **3.2 LTS** | 11 |

**資料來源確認**：從文件 footer 取得 — `docs.haproxy.org/3.0/configuration.html`
**產製日期**：2026-04-03

## 官方版本查證

查詢 `haproxy.org` 官方版號表：

| Branch | 類型 | 釋出日 | EOL | 最新版號 |
|--------|------|--------|-----|---------|
| 3.4-dev | 未來 LTS | ~2026-Q2 | 2031-Q2 | 3.4-dev12 |
| 3.3 | stable（短週期） | 2025-11-26 | 2027-Q1 | 3.3.10 |
| **3.2** | **LTS（最新）** | **2025-05-28** | **2030-Q2** | **3.2.19** |
| 3.1 | unmaintained | 2024-11-26 | 2026-Q1 | 3.1.17 |
| **3.0** | **LTS（舊）** | **2024-05-29** | **2029-Q2** | **3.0.23** |
| 2.9 | unmaintained | 2023-12-05 | 2025-Q1 | 2.9.15 |
| 2.8 | LTS | 2023-05-31 | 2028-Q2 | 2.8.24 |

**HAProxy 版本制度**：偶數版號 = LTS（~5年維護），奇數版號 = stable（~1年維護）

## 版本差異

| 文件集 | 文件使用 | 同分支最新 | LTS 最新版 | 差距判定 |
|--------|---------|-----------|-----------|---------|
| Config Manual | HAProxy **3.0** (LTS) | 3.0.23 | **3.2.19** (LTS) | 🔴 可選擇：同分支更新 or 升級 3.2 |
| ACL Cheat Sheet | HAProxy **3.2** (LTS) | 3.2.19 | **3.2.19** (LTS) | 🟢 已在最新 LTS，僅點版本差異 |
| Starter Guide | HAProxy **3.2** (LTS) | 3.2.19 | **3.2.19** (LTS) | 🟢 已在最新 LTS，僅點版本差異 |

### 版本變更內容（from haproxy.org）

**HAProxy 3.0 功能集（文件基礎）：**
crt-stores、persistent stats、syslog load balancing、JSON & CBOR log encoding、virtual maps & ACLs、zero-copy from cache、H2/H3 protocol-level protections

**v3.1 → v3.2（跨 LTS 世代變更）：**

| v3.1 (stable, 2024-11) | v3.2 (LTS, 2025-05) |
|------------------------|---------------------|
| 故障排除強化 | ACME & SSL 管理 |
| 設定可靠性改善 | CPU 可擴展性改善 |
| QUIC 與 H2 效能提升 | QUIC 效能優化 |
| 新的 SPOE 引擎 | 故障排除強化 |
| 更細緻的錯誤報告 | |

## 建議更新範圍

### Config Manual（13 份，兩套子集）

**方案 A（建議）：升級至 HAProxy 3.2 LTS**
需要全面更新，主要變更影響以下章節：

1. **Ch.3 Global Parameters** — ACME 自動證書相關參數新增
2. **Ch.4 Proxies** — CPU 可擴展性相關設定、QUIC 效能調校
3. **Ch.5 Bind & Server** — SSL 管理強化、ACME 整合
4. **Ch.7 ACL & Samples** — 錯誤報告改進相關 fetch
5. **Ch.8 Logging** — 如有新增日誌格式

**方案 B（最低更新）：同分支更新至 3.0.23**
僅修補 bug fixes，無功能變更。更新 footer 中的產製日期。

### ACL Cheat Sheet（2 份）

無需功能更新。3.2 LTS 僅點版本差異，內容仍適用。

### Starter Management Guide（11 份）

無需功能更新。3.2 LTS 僅點版本差異，內容仍適用。

## 參考資源

- HAProxy 官方版號表：https://www.haproxy.org/
- HAProxy 3.2 LTS 設定文件：https://docs.haproxy.org/3.2/configuration.html
- HAProxy 3.2 LTS 原始碼：https://www.haproxy.org/download/3.2/src/
- HAProxy 3.2 changelog：https://www.haproxy.org/download/3.2/src/CHANGELOG
