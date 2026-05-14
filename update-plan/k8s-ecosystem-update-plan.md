# K8s 生態系 (Helm + k3s + Kubernetes) 更新計劃

## 文件概覽

| 路徑 | 檔案數 | 說明 |
|------|--------|------|
| `reports/k8s-ecosystem/` | 8 | K8s 指南 (6章)、Helm 指南、k3s 手冊 |

## 版本差異

### Kubernetes 核心文件
| 文件涵蓋範圍 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| v1.24–v1.32 | v1.36.1 (2026-05) | ⚠️ 落後 4-5 版 |

### Helm
| 文件涵蓋版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| Helm 3.8 | v4.2.0 (2026-05-14) | ⚠️ 大版本跳躍 (3.x → 4.x) |

### k3s
| 文件涵蓋版本 | 官方最新版本 | 差距 |
|-------------|-------------|------|
| v1.20–v1.30 | v1.36.0+k3s1 (2026-05-06) | ⚠️ 落後 |

## 主要變更

### Kubernetes v1.32 → v1.36
各版本變更較多，重點包含：
- **Sidecar Containers 正式版** (v1.29 GA)
- **新的 API 版本** (部分舊 API 被移除)
- **Node 生命週期管理強化**
- **In-tree 儲存外掛移除**
- **PodSecurity 取代 PSP**
- **新排程器功能**
- **DRA (Dynamic Resource Allocation) 演進**

### Helm 3.8 → 4.x 主要變更
- **OCI 註冊表作為預設**
- **Chart 結構變更** (新的 apiVersion)
- **Helmfile / Helm Chart 依賴管理改進**
- **新的 linting 與驗證功能**
- **安全強化** (簽章驗證改進)

### k3s v1.30 → v1.36
- **嵌入式 etcd 升級**
- **新的 CNI 選項**
- **HelmController 更新**
- **Kubernetes API 同步更新**

## 建議更新範圍

### K8s 指南 (6 章，ch00–ch08)
1. **API 版本更新**：移除舊 beta API 參考，更新為新版
2. **Workloads 章節**：新增 Sidecar Containers
3. **Security 章節**：PodSecurity 取代 PSP，新的 NetworkPolicy 功能
4. **Storage 章節**：更新 CSI 驅動程式列表
5. **Scheduling 章節**：新增排程器功能
6. **kubectl Cheatsheet**：更新新版命令

### Helm 指南
🔴 **高優先** — 全面更新 Helm v4 內容
- Chart 結構變更
- OCI 作為預設 registry
- 指令與 flag 變更
- Helm 套件生態更新

### k3s 手冊
🟡 中優先 — 更新安裝步驟、embedded etcd、CNI 選項

## 參考資源
- K8s Changelog: https://github.com/kubernetes/kubernetes/tree/master/CHANGELOG
- Helm 4 升級指南: https://helm.sh/docs/topics/version-skew/
- k3s releases: https://github.com/k3s-io/k3s/releases
