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
- cheatsheet-01-core — 更新版本號、授權、架構描述 ✅
- cheatsheet-02-datatypes-1 — 無版本相關內容需變動 ✅
- cheatsheet-03-datatypes-2 — 內建模組標籤、JSON Path V2、IDMP、NaN ✅
- cheatsheet-04-commands — HOTKEYS、HGETDEL/HGETEX/HSETEX、Search 內建 ✅
- cheatsheet-05-persistence-ha — 8.0 複製改良、8.2 Cluster 效能 ✅
- cheatsheet-06-programmability-pubsub — Sharded Pub/Sub 8.2 改善 ✅
- cheatsheet-07-security-performance — 新逐出策略、TLS 憑證認證、HOTKEYS ✅
- cheatsheet-08-ecosystem-search-ai — 命名/授權更新、模組內建標示 ✅

## 執行備註
### 與原始計劃差異
- **RESP3**：Redis 8.0 release notes 未提及 RESP3 協議重大變更（RESP3 自 Redis 6.0 引入），無需更新
- **Triggers & Functions GA**：查核官方 release notes 後確認 Redis 8.0 未正式提及 Triggers & Functions GA；Redis Functions 自 7.0 已可用，文件已涵蓋
- **HGETDEL / HGETEX / HSETEX**：Redis 8.0 新增 Hash 命令，補充至 #2 但該檔案無版本依賴，最終無需變動

## 參考資源
- [Redis GitHub Releases](https://github.com/redis/redis/releases)
- [Redis 8.0 Release Notes](https://raw.githubusercontent.com/redis/redis/8.0/00-RELEASENOTES)
- [Redis 8.6 Release Notes](https://raw.githubusercontent.com/redis/redis/8.6/00-RELEASENOTES)
