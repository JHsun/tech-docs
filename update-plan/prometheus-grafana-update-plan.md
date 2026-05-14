# Prometheus / Grafana / Observability 更新計劃

## 文件概覽

| 路徑 | 檔案數 | 說明 |
|------|--------|------|
| `reports/Observability/` | 60 | 主要教學系列 |
| `reports/Prometheus-Grafana/` | 60 | ⚠️ 與 Observability 內容完全相同 (推測是 duplicate/copy) |

**兩者檔案內容一致**，應確認是否需移除其中一份。

## 版本差異

### Prometheus
| 文件提及版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| 2.40 / 3.0 (transitional) | v3.11.3 (2026-04-27) | 需要審視 3.x 系列變更 |

### Grafana
| 文件提及版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| Grafana 11 / 12 | v13.0.1 (2026-05-12) | 落後 1 大版本 (11→13) |

### Alertmanager
| 文件提及版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| 未明確標示 | v0.32.1 | 無法精確比對 |

## 主要變更

### Prometheus 3.0 → 3.11
- **新 UI** (v3.0)：React-based 新 UI 取代舊版
- **OTLP 原生支援**：native OTLP ingestion
- **Remote Write 2.0**：新的 remote write 協定
- **PromQL 增強**：新函數、`@` modifier
- **service discovery 擴充**：新的目標來源
- **TSDB 持續優化**

### Grafana 11 → 13
- **Grafana 12**：新的 dashboard 編輯器 UI、 enhanced Explore、Scenes 正式版
- **Grafana 13**：Alerting 管理介面大改、新的 visualizations、強化 RBAC
- **資料來源更新**：每個版本皆有新的資料來源整合

## 建議更新範圍

1. **Duplicate 清理** 📌
   - 確認是否需保留 `Prometheus-Grafana/`，或改 symlink 指向 `Observability/`

2. **Prometheus 相關文件** (ch05–ch28)
   - 更新 Service Discovery 章節 (3.x 有新增發現機制)
   - Remote Write 改成 2.0 協定說明
   - 新增 OTLP ingestion 說明
   - PromQL 新增函數補充
   - 更新 Alertmanager 設定 (v0.32)

3. **Grafana 相關文件** (ch29–ch44)
   - Dashboard 設計章節：反映新 UI/編輯器
   - 資料來源章節：新增支援的資料來源
   - RBAC/授權章節：更新 v13 權限模型
   - Alerting 章節：大幅更新 (v13 有重大變更)

4. **LGTM Stack** (ch45–ch48)
   - Loki: v3.7.2 (logQL 新增功能)
   - Tempo: v2.10.5 (分散式追蹤)
   - Mimir: 3.0.6 (持續演進)
   - Pyroscope: v2.0.2 (持續分析)

5. **Ecosystem 章節** (ch49–ch60)
   - Alloy: v1.16.1 (取代 Agent 的架構更新)
   - k6: v2.0.0 (重大版本更新)
   - Cloud integrations (AWS/GCP/Azure): 更新服務列表

## 優先級

- 清理 duplicate：🔴 高
- Prometheus 3.x 系列更新：🟡 中
- Grafana 13 更新：🟡 中
- LGTM 組件更新：🟢 低
