# etcd 更新計劃

## 文件概覽
| 路徑 | 檔案數 |
|------|--------|
| `reports/etcd-quickstart/` | 5 |

## 文件版本確認
從文件內容取得：
- **版本**：etcd v3.5
- **來源**：`etcd.io/docs/v3.5`（footer embedded URL）
- **產製日期**：v3.5.21 參照

## 官方版本查證
| Branch | 類型 | 最新版號 |
|--------|------|---------|
| v3.6 | Current release | v3.6.11 |
| v3.5 | LTS / maintained | v3.5.30 |
| v3.4 | Legacy | v3.4.44 |

## 版本差異
| 文件使用 | 同分支最新 | LTS/Stable 最新 | 差距判定 |
|---------|-----------|----------------|---------|
| v3.5.x | v3.5.30 | v3.6.11 | 🔴 大版本（v3.5 → v3.6） |

## 版本變更內容（v3.5 → v3.6）
- v3.6 新增身分驗證強化（mTLS by default）
- Watch 效能大幅提升（stream multiplexing）
- 新的儲存引擎（bbolt 更新）+ 更快的 defrag
- 更好的 Kubernetes 整合（structured logging）
- 部分 API 棄用需要遷移

## 建議更新範圍
### 全部 5 份文件
- 速查表① — 安裝指令更新至 v3.6
- 速查表② — 資料模型 / API 變更確認
- 速查表③ — TLS 安全章節大幅更新（mTLS）
- 速查表④ — 組態參數新增
- 速查表⑤ — 效能調校、Prometheus 指標更新

## 參考資源
- [etcd GitHub Releases](https://github.com/etcd-io/etcd/releases)
- [etcd v3.6 Docs](https://etcd.io/docs/v3.6/)
- [CHANGELOG](https://github.com/etcd-io/etcd/blob/main/CHANGELOG)
