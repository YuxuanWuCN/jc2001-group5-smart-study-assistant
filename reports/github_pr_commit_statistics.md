# GitHub Pull Request & Commit Statistics Report
## JC2001 Group 5 · SmartStudy Console · 2026-10-29

---

## 一、Pull Request 统计（Repository: YuxuanWuCN/jc2001-group5-smart-study-assistant）

### 1.1 PR 总览

| 指标 | 数值 |
| :--- | ---: |
| **PR 总数** | **5** |
| 已合并 (MERGED) | 2 |
| 开放中 (OPEN) | 2 |
| 已关闭未合并 (CLOSED) | 1 |

### 1.2 PR 详细清单

| # | 标题 | 作者 | 状态 | 创建时间 | 合并/关闭时间 |
| :-: | :--- | :--- | :---: | :--- | :--- |
| **#5** | docs(cycle3): startup-grade technical report plan and team task packs | Yuxuan Wu | **OPEN** | 2026-10-17 | — |
| **#4** | feat(frontend): 学生登录界面与交互工作台门户实现 (Student Login Portal & Workspace UI) | Yuxuan Wu | **OPEN** | 2026-10-16 | — |
| **#3** | feat(knowledge): 大二上全学科知识点本体与拓扑图谱导入 (OR, MIS, Math, MKT, ENG) | Yuxuan Wu | CLOSED | 2026-10-16 | 2026-10-16 |
| **#2** | feat(architecture): add UML context model, use case diagram, and sequence diagram | Yuxuan Wu | **MERGED** | 2026-10-09 | 2026-10-09 |
| **#1** | feat(portal-ui): introduce product landing portal, student authentication, and full bilingual i18n support | Yuxuan Wu | **MERGED** | 2026-10-09 | 2026-10-09 |

### 1.3 PR 分析

#### ✅ **已合并 PR（2 个）**

1. **#1 — Portal UI & i18n Support**  
   - 引入产品落地页、学生认证、双语 i18n 支持  
   - 合并时间：2026-10-09（创建后 1h 13m）

2. **#2 — UML Architecture Diagrams**  
   - 添加 UML 上下文模型、用例图、时序图  
   - 合并时间：2026-10-09（创建后 20m）

#### 🟡 **开放中 PR（2 个）**

3. **#4 — Student Login & Workspace UI** ⚠️  
   - 创建于 2026-10-16（**已开放 13 天**）  
   - 建议：Week A 门禁前决定是否合并或关闭

4. **#5 — Cycle 3 Report Plan & Task Packs** ⚠️  
   - 创建于 2026-10-17（**已开放 12 天**）  
   - 建议：与报告进度绑定，Week A 完成后合并

#### ❌ **已关闭未合并 PR（1 个）**

5. **#3 — Knowledge Ontology Import**  
   - 创建于 2026-10-16，同日关闭（未合并）  
   - 分析：可能因知识图谱范围调整或与 ADR-05（Neo4j 移出演示链路）决策相关

---

## 二、Commit 统计

### 2.1 总体数据

| 指标 | 数值 |
| :--- | ---: |
| **Commit 总数（不含 merge）** | **51** |
| **文件变更总数** | **451** |
| **代码新增行数** | **+71,200** |
| **代码删除行数** | **−14,294** |
| **净增长** | **+56,906** |

### 2.2 贡献者分布

| 排名 | 贡献者 | Commit 数 | 占比 |
| :-: | :--- | ---: | ---: |
| 🥇 | **Yuxuan Wu** | **34** | **66.7%** |
| 🥈 | xin-315（谢炜昕） | 6 | 11.8% |
| 🥉 | yhdmcst（张梓健） | 5 | 9.8% |
| 4 | Cindy（早期协作者） | 3 | 5.9% |
| 5 | Siqin Dong（董思钦） | 1 | 2.0% |
| 6 | u02yx25（习羽赛） | 1 | 2.0% |
| 7 | Zhang Zijian（张梓健） | 1 | 2.0% |
| **总计** | **7 位贡献者** | **51** | **100%** |

### 2.3 关键里程碑 Commit

| 日期 | Commit Hash | 作者 | 关键内容 |
| :--- | :--- | :--- | :--- |
| **2026-10-25** | `32a583d` | Yuxuan Wu | 同步测试基线至 147 用例、去除个人路径、精简文档 |
| **2026-10-25** | `6ca027c` | Yuxuan Wu | **清除 GraphRAG 脚本中残留的硬编码凭证** |
| **2026-10-25** | `61eba90` | Yuxuan Wu | **脱敏学号与邮箱信息** |
| **2026-10-24** | `194b91c` | Yuxuan Wu | 交付董思钦负责的 Ch5.3-5.4 outline + 素材 |
| **2026-10-23** | `3a315c7` | Yuxuan Wu | 在 README 中详细拆解 Cycle 1/2/3 各成员任务 |
| **2026-10-18** | `acded7f` | Yuxuan Wu | **Cycle 3 启动：技术报告蓝图 + 9 份任务包 + 督导答案库** |
| **2026-10-17** | `6342fb5` | Yuxuan Wu | 完成学生登录门户、模态认证流程与 API 端点 |
| **2026-10-16** | `2e86121` | Yuxuan Wu | 落地 Phase 2 Cycle 2 里程碑报告与 Week 6 UML 实验产物 |
| **2026-10-10** | `e575c7c` | xin-315 | 添加文件（组员贡献） |
| **2026-10-10** | `0feb82d` | Siqin Dong | **feat(diagnostics): 实时 LLM 密钥健康探针与故障分类** |
| **2026-10-09** | `66734a1` | Zhang Zijian | **添加用例文档与需求追溯矩阵** |
| **2026-10-09** | `35e6cd4` | Yuxuan Wu | 实现产品落地页、学生认证、双语 i18n 与可运行 MVP |
| **2026-10-08** | `7d83001` | u02yx25（习羽赛） | **添加前后端 API 接口映射表** |
| **2026-10-08** | `4b5c88c` | Yuxuan Wu | **交付端到端可运行 MVP PoC（FastAPI + 题库诊断）** |
| **2026-09-23** | `d73e548` | Yuxuan Wu | 初始化 JC2001 Group 5 项目仓库与 Week 1/2 基线 |

---

## 三、代码活跃度分析

### 3.1 时间线分布

| 时间段 | Commit 数 | 占比 | 关键里程碑 |
| :--- | ---: | ---: | :--- |
| **2026-09-23（Week 1）** | 4 | 7.8% | 项目初始化、Week 1/2 基线 |
| **2026-10-08–10（Week 5）** | 16 | 31.4% | **PoC MVP 交付、UML 图件、组员首次贡献** |
| **2026-10-16–17（Week 7）** | 5 | 9.8% | Phase 2 报告、登录门户 |
| **2026-10-18–20（Cycle 3 启动）** | 5 | 9.8% | **报告蓝图 + 任务包分发** |
| **2026-10-23–25（最近一周）** | 9 | 17.6% | **安全修复、测试基线同步、任务分配** |
| 其他时段 | 12 | 23.5% | UI 优化、文档补充 |

### 3.2 贡献类型分布（按 commit message 前缀）

| 类型 | 数量 | 占比 | 示例 |
| :--- | ---: | ---: | :--- |
| **feat** | 15 | 29.4% | Portal UI、认证系统、诊断算法 |
| **docs** | 18 | 35.3% | 报告、任务包、API 映射、README |
| **fix** | 10 | 19.6% | **凭证泄露修复**、缓存失效、PII 脱敏 |
| **chore** | 5 | 9.8% | 仓库整理、依赖隔离 |
| **其他** | 3 | 5.9% | 实验性功能、文件管理 |

---

## 四、关键发现与风险提示

### 4.1 ✅ 正向发现

1. **高密度开发周期**：Week 5（10-08 至 10-10）产出 16 个 commit，完成 PoC MVP 与 UML 交付，是项目核心里程碑。
2. **组员开始参与贡献**：
   - 董思钦（Siqin Dong）：诊断算法与 LLM 健康探针
   - 习羽赛（u02yx25）：前后端 API 映射表
   - 张梓健（yhdmcst / Zhang Zijian）：用例文档与需求追溯矩阵
   - 谢炜昕（xin-315）：6 次贡献（文件添加与组织）
3. **安全意识提升**：10-25 主动清除硬编码凭证、脱敏 PII，说明项目质量意识在成熟。

### 4.2 ⚠️ 风险与改进建议

#### **风险 1：贡献集中度过高**
- **现状**：Yuxuan Wu 贡献 66.7% 的 commit（34/51）
- **影响**：与 Appendix A（Group Workload Profile）的"10 人协同"叙事不符
- **建议**：
  - 在 Appendix A 中如实申报代码集中现象
  - 强调报告分工是"知识转移"手段（9 人各负责 1 章）
  - 组会演练时让其他成员能独立回答各自章节

#### **风险 2：2 个 PR 长期开放未合并**
- **#4 和 #5 已开放 12–13 天**，未合并也未关闭
- **建议**：
  - Week A 门禁前决定是否合并或转为 draft
  - 避免"大量未完成 PR"的视觉印象（评审老师可能查看 GitHub）

#### **风险 3：部分组员仅有 1 次 commit**
- 董思钦、习羽赛、张梓健（作为 Zhang Zijian ID）各仅 1 次
- **建议**：
  - 鼓励组员提交自己章节的 outline.md 作为独立 commit
  - 在 Week A–B 通过 Git 记录报告编写过程

---

## 五、Cycle 3 GitHub 行动建议

### 5.1 Week A（本周）

| 任务 | 负责人 | 目标 |
| :--- | :--- | :--- |
| **合并或关闭 PR #4、#5** | Yuxuan Wu | 清理开放 PR，避免"半成品感" |
| **鼓励组员提交 outline** | 各章负责人 | 每人独立 commit 自己的 `reports/final_report/chXX/outline.md` |
| **建立进度看板** | 谢炜昕 | `progress_tracker.md` + 每日更新状态 |

### 5.2 Week B–C

| 任务 | 目标 |
| :--- | :--- |
| **每章初稿独立 PR** | 9 位组员各提交 1 个 PR（`feat(report): add ChX draft`） |
| **交叉审校记录** | 审稿人在 PR 评论中留下具体意见 |
| **最终合稿 PR** | 谢炜昕统稿后提交 1 个合并 PR（`docs(report): deliver Technical Report v1.0`） |

---

## 六、数据来源与验证

- **仓库**：`https://github.com/YuxuanWuCN/jc2001-group5-smart-study-assistant.git`
- **统计时间**：2026-10-29 00:10
- **命令**：
  - `gh pr list --state all --limit 100 --json number,title,author,state,createdAt,mergedAt,closedAt`
  - `git log --all --pretty=format:"%an" --no-merges | Group-Object`
  - `git log --all --shortstat --no-merges`
- **验证**：可在仓库中执行以下命令复现：
  ```powershell
  cd D:\jc2001
  git log --all --oneline --no-merges | Measure-Object -Line  # 应返回 51
  git log --all --pretty=format:"%an" --no-merges | Group-Object | Sort-Object Count -Descending
  ```

---

## 七、附录：完整 PR JSON 数据

```json
[
  {
    "number": 5,
    "title": "docs(cycle3): startup-grade technical report plan and team task packs",
    "author": {"login": "YuxuanWuCN", "name": "Yuxuan Wu"},
    "state": "OPEN",
    "createdAt": "2026-10-17T16:10:03Z",
    "mergedAt": null,
    "closedAt": null
  },
  {
    "number": 4,
    "title": "feat(frontend): 学生登录界面与交互工作台门户实现 (Student Login Portal & Workspace UI)",
    "author": {"login": "YuxuanWuCN", "name": "Yuxuan Wu"},
    "state": "OPEN",
    "createdAt": "2026-10-16T17:23:26Z",
    "mergedAt": null,
    "closedAt": null
  },
  {
    "number": 3,
    "title": "feat(knowledge): 大二上全学科知识点本体与拓扑图谱导入 (OR, MIS, Math, MKT, ENG)",
    "author": {"login": "YuxuanWuCN", "name": "Yuxuan Wu"},
    "state": "CLOSED",
    "createdAt": "2026-10-16T17:17:31Z",
    "mergedAt": null,
    "closedAt": "2026-10-16T17:20:42Z"
  },
  {
    "number": 2,
    "title": "feat(architecture): add UML context model, use case diagram, and sequence diagram",
    "author": {"login": "YuxuanWuCN", "name": "Yuxuan Wu"},
    "state": "MERGED",
    "createdAt": "2026-10-09T05:12:18Z",
    "mergedAt": "2026-10-09T05:12:38Z",
    "closedAt": "2026-10-09T05:12:38Z"
  },
  {
    "number": 1,
    "title": "feat(portal-ui): introduce product landing portal, student authentication, and full bilingual i18n support",
    "author": {"login": "YuxuanWuCN", "name": "Yuxuan Wu"},
    "state": "MERGED",
    "createdAt": "2026-10-09T03:38:26Z",
    "mergedAt": "2026-10-09T04:51:13Z",
    "closedAt": "2026-10-09T04:51:13Z"
  }
]
```

---

**统计编制**：Yuxuan Wu（PM / Team Lead）  
**统计日期**：2026-10-29  
**下次更新**：Week A 门禁后（2026-11-04）
