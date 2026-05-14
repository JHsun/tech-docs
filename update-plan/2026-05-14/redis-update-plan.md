# Redis 更新計劃

## 文件概覽
| 路徑 | 檔案數 |
|------|--------|
| `reports/redis-cheat-sheet/` | 8 |

## 文件版本確認
從文件內容取得：
- **版本**：Redis 7.4
- **來源**：無明確資料來源 footer，程式碼範例使用 `redis/go-redis`
- **產製日期**：未標註

## 官方版本查證
| Branch | 類型 | 最新版號 |
|--------|------|---------|
| 8.6 | Current | 8.6.3 |
| 8.4 | LTS-ish | 8.4.x |
| 7.4 | Legacy | 7.4.x |

## 版本差異
| 文件使用 | 同分支最新 | 最新穩定版 | 差距判定 |
|---------|-----------|-----------|---------|
| v7.4 | 7.4.x | 8.6.3 | 🔴 大版本（7→8） |

## 版本變更內容（7.4 → 8.6）
- Redis 8.0：向量資料庫整合（RedisVL）、新版 RESP3 協議、Triggers & Functions GA
- Redis 8.2：Cluster 效能大幅提升、Sharded Pub/Sub 改進
- Redis 8.4：搜尋索引強化、JSON 路徑 V2
- Redis 8.6：多線程處理再優化、新的記憶體效率模式

## 建議更新範圍
### 全部 8 份文件
- cheatsheet-01-core — 更新版本號，檢查 RESP3 相關命令差異
- cheatsheet-02-datatypes-1 / 03-datatypes-2 — 確認新資料型別（Vector）
- cheatsheet-04-commands — 核對新命令是否存在
- cheatsheet-05-persistence-ha — 確認 cluster 配置有無變化
- cheatsheet-06-programmability-pubsub — Triggers & Functions GA
- cheatsheet-07-security-performance — 安全性改進
- cheatsheet-08-ecosystem-search-ai — 搜尋/AI 功能大幅擴充

## 參考資源
- [Redis GitHub Releases](https://github.com/redis/redis/releases)
- [Redis 8.0 Release Notes](https://raw.githubusercontent.com/redis/redis/8.0/00-RELEASENOTES)
- [Redis 8.6 Release Notes](https://raw.githubusercontent.com/redis/redis/8.6/00-RELEASENOTES)
