# Elasticsearch 更新計劃

## 文件概覽

| 路徑 | 檔案數 |
|------|--------|
| `reports/Elasticsearch/` | 66 (教學手冊) |
| `reports/Elasticsearch-Self-managed-CheatSheet/` | 12 (速查表) |

## 版本差異

| 文件涵蓋範圍 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| Elasticsearch 9.x | v9.4.1 (2026-05-12) | 需確認具體子版本差異 |

## 主要變更 (9.0 → 9.4 系列)

Elasticsearch 9.x 持續演化中：

- **ES|QL 持續強化**：9.3/9.4 新增函數與指令
- **向量搜尋優化**：新的 dense/sparse 向量索引演算法
- **Inference API 擴充**：更多 machine learning 模型支援
- **Connector 更新**：更多第三方資料來源
- **安全性更新**：TLS 設定最佳實務變更
- **ILM/data stream lifecycle 改善**

## 建議更新範圍

### 教學手冊 (66 份文件) — 選擇性更新
- ES|QL 相關章節 (ch06–07, ch39)：更新新函數與指令
- 向量搜尋章節 (ch08, ch40, ch60)：更新索引演算法
- ML 相關章節 (ch44)：更新新整合
- Connector 章節 (ch61)：新增支援的來源

### 速查表 (12 份文件) — 選擇性更新
- ES|QL 命令 (ch06)：確認新命令
- 向量/RAG (ch08)：更新語法
- Troubleshooting/Upgrade (ch11)：更新升級建議

## 優先級

- 🟡 中 — ES|QL 部分可能有較大變更 (ES|QL 仍在快速演化)
- 🟢 低 — 其他章節內容普遍通用
