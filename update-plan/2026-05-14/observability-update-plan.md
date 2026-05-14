# Observability / Prometheus-Grafana 更新計劃

## 文件概覽
| 路徑 | 檔案數 | 備註 |
|------|--------|------|
| `reports/Observability/` | 61 | ⚠️ 與 Prometheus-Grafana 完全重複 |
| `reports/Prometheus-Grafana/` | 61 | ⚠️ 與 Observability 完全重複 |

---

## Prometheus

### 文件版本確認
- **範圍版本**：Prometheus 2.x ~ 3.x（文件中提到 2.40, 2.47, 2.54, 3.0, 3.11）
- **主要參考**：Prometheus 3.11（ch00 learning path）

### 官方版本查證
| Branch | 最新版號 |
|--------|---------|
| v3.x | v3.11.3 |

### 版本差異
| 文件使用 | 最新版 | 差距判定 |
|---------|--------|---------|
| 3.11（主要） | 3.11.3 | 🟢 僅 patch |

### 建議（✅ 已完成）
- 若以 v3.11 為主要版本，patch 更新無實質影響 ✅
- 注意文件中穿插的 2.x 範例可能需要統一至 3.x（內容為歷史說明，OK）✅
- ch00 版本參考更新 ✅

---

## Grafana

### 文件版本確認
- **版本**：Grafana 12.4（ch00 learning path）
- **也有提到**：Grafana 11.5（ch53 Azure integrations）

### 官方版本查證
| Branch | 最新版號 |
|--------|---------|
| v13.x | v13.0.1+security-01 |

### 版本差異
| 文件使用 | 最新版 | 差距判定 |
|---------|--------|---------|
| 12.4 | 13.0.1 | 🔴 大版本（12→13） |

### 版本變更內容（12→13）
- Grafana 13 引入全新 Navigation UI
- Scenes（新的 dashboard engine）GA
- 全新的 Alerting 架構
- Grafana 13 移除舊版 Angular 元件（v12 已警告）
- 大量 plugin API 變更

### 建議更新（✅ 已完成）
- ch00 產品表格與版本參考更新至 v13.0.1 ✅
- ch29 §5 擴充 v13 內容（Scenes GA、Navigation Redesign、Dynamic Dashboards GA）✅
- Grafana 章節 14 份加入版本標記 ✅
- ch53 Azure 更新 11.5+ → 13+ ✅

---

## Alertmanager

### 文件版本確認
- **版本**：Alertmanager 0.27 ~ 0.32（範圍）

### 官方版本查證
| 最新版號 |
|---------|
| v0.32.1 |

### 差距判定
🟢 僅 patch（0.32 為上界）✅ 已確認

---

## 重複問題
**Observability/ 與 Prometheus-Grafana/ 為完全相同拷貝**（md5 一致），建議：
- 移除其中一個目錄
- 或建立 symlink
- 或合併後保留一個

## 整體建議優先級：🟡 中（Grafana v13 為主要項目）
