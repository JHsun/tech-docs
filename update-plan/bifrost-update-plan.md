# Bifrost AI Gateway 更新計劃

## 文件概覽

| 路徑 | 檔案數 |
|------|--------|
| `reports/bifrost-cheat-sheet/` | 7 |

## 版本差異

| 項目 | 內容 |
|------|------|
| 文件採用版本 | v1.5.0（2026-04） |
| 官方最新版 | GitHub release: ent-v1.4.2-stream-pause-base (2026-05-13) / npm: 1.6.2 |
| 差距 | 需要釐清版本對應關係 |
| 官方來源 | https://github.com/maximhq/bifrost |

## 分析

Bifrost AI Gateway 由 **maximhq/bifrost** 開發，是一個企業級 AI 閘道器。

版本狀況需注意：
- GitHub release tag 格式為 `ent-v*`，可能為企業版 tagging
- npm 版本號 (1.6.2) 與 GitHub 不完全同步
- Docker image tag `v1.3.9-arm64` 又與 npm/GitHub 不同

文件涵蓋 v1.5.0 的功能集（23+ Provider、Tool Calling、MCP 支援等）。

## 建議更新範圍

- 🟡 中優先級 — 需先釐清版本對應規則後更新
- 確認文件所述 v1.5.0 功能是否仍對應最新 npm package
- Provider 列表需更新（AI 領域 Provider 變動頻繁）
- MCP/工具調用章節可能有新增功能
