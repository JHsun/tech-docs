# Redis 更新計劃

## 文件概覽

| 路徑 | 檔案數 |
|------|--------|
| `reports/redis-cheat-sheet/` | 8 |

## 版本差異

| 文件採用版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| Redis 7.4 | Redis 8.6.3 (2026-05-05) | ⚠️ 大版本跳躍 (7.x → 8.x) |

### Redis 7.4 → 8.6 主要變更

Redis 8.x 引入了多項重大變更與新功能：

**8.0 (2025 Q2)：**
- 新的序列化協定 (RESP3 完整支援)
- Cluster 功能強化
- 新的資料型態：JSON path 查詢改進
- ACL v2
- 新的複寫機制

**8.1–8.5：**
- 搜尋功能強化 (RediSearch 整合更深)
- 向量搜尋效能優化
- Cluster 管理介面改善
- 持續的安全性強化

**8.6 (2026-05)：**
- 最新的 HA 機制改善
- 效能優化
- 安全性修補

## 建議更新範圍

### 全部 8 份文件需審視更新

1. **Core Concepts** (`cheatsheet-01-core.html`) — 🔴 高優先
   - RESP3 協定改為預設
   - 核心架構更新 (cluster mode 改進)
   
2. **Data Types 1 & 2** (`cheatsheet-02/03-datatypes-*.html`) — 🟡 中
   - 檢查是否有新資料型態
   - 確認既有型態的指令變更

3. **Commands** (`cheatsheet-04-commands.html`) — 🟡 中
   - 新指令加入
   - 部分指令參數變更

4. **Persistence & HA** (`cheatsheet-05-persistence-ha.html`) — 🔴 高優先
   - Redis 8.x 複寫機制更新
   - Sentinel 設定變更
   - 新的 HA 模式

5. **Programmability & Pub/Sub** (`cheatsheet-06-programmability-pubsub.html`)
   - RESP3 pub/sub 變更
   - Lua 指令碼限制更新

6. **Security & Performance** (`cheatsheet-07-security-performance.html`)
   - ACL v2 更新
   - 新的安全設定

7. **Ecosystem & Search/AI** (`cheatsheet-08-ecosystem-search-ai.html`)
   - Redis 8 向量搜尋更新
   - 生態系工具變化

## 參考資源

- Redis 8.6 官方公告：https://redis.io/download/
- Redis 版本歷史：https://raw.githubusercontent.com/redis/redis/8.6/00-RELEASENOTES
