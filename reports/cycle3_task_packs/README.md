# Cycle 3 任务包总索引（9 份 · 一人一章 · 责权到人）

> 这一目录是给 **9 位组员** 的作业包。每人一个文件，找到自己的学号，直接照做。
> 上游总计划见 [`../cycle3_master_plan.md`](../cycle3_master_plan.md)；组会问答答案见 [`../supervisor_qa_defense_library.md`](../supervisor_qa_defense_library.md)。
>
> **⚠️ 全部章节结构以官方 Brief 为准**：`D:\jc2001\JC2001-GroupProjectDescription-and-Requirements-2026-27.txt`。Technical Report 必含七章，顺序固定、不得增删。

---

## 1. 为什么要这样分工（一句话）

Technical Report 占课程 **50%**，目前进度是 **0 页**。软件基线已冻结（8 个 API 端点 + 145 个测试用例全绿 + 3 张 UML 图 + 12 题 36 陷阱），**缺的只是把已经存在的事实写成文字**。一个人写 40–60 页会死，十个人一人 4–5 页刚刚好。

因此本周期：**不写新功能，只写报告**。每人只负责自己那一章，素材全部在仓库里，不需要自己编。

---

## 2. 任务包索引（对应官方七章）

| # | 成员 | 学号 | 角色 | 章节（官方编号） | 页数 | 文件 |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- |
| 01 | 林泳桐 | 50106038 | Lead BA | **Ch1** Introduction and Project Context | 5–6 | [01](01-ch1-introduction-lin-yongtong.md) |
| 02 | 张梓健 | 50106035 | BA | **Ch2** Functional and Non-Functional Requirements | 6–7 | [02](02-ch2-requirements-moscow-zhang-zijian.md) |
| 09 | 谢炜昕 | 50106034 | QA / 报告 Lead | **Ch3** Use Cases and Requirements Modelling ＋附录 B ＋全篇统稿 | 6–7 | [09](09-ch3-use-cases-xie-weixin.md) |
| 04 | 王思鉴 | 50106045 | 架构 | **Ch4** System Design and Architecture | 9–11 | [04](04-ch4-architecture-wang-sijian.md) |
| 05 | 江昊 | 50106065 | PoC Lead Dev | **Ch5.1–5.2** 技术栈与软件结构 ＋ API 契约与领域模型 ＋附录 D | 5–6 | [05](05-ch5-1-2-implementation-jiang-hao.md) |
| 06 | 董思钦 | 50106060 | PoC 逻辑 | **Ch5.3–5.4** 题库陷阱工程 ＋ 诊断算法 | 5–6 | [06](06-ch5-3-4-trap-diagnosis-dong-siqin.md) |
| 03 | 习羽赛 | 50105989 | UI/UX | **Ch5.5** Graphical User Interface | 3–4 | [03](03-ch5-5-gui-xi-yusai.md) |
| 08 | 梁子铉 | 50106037 | 部署 / 媒体 | **Ch5.6** Deployment and Reproducibility ＋ 演示视频与 PPT | 3–4 | [08](08-ch5-6-deployment-liang-zixuan.md) |
| 07 | 杨明杰 | 50106061 | 测试 | **Ch6** Testing and Evaluation ＋附录 C ＋ PoC User Manual | 7–8 | [07](07-ch6-testing-yang-mingjie.md) |
| — | 吴宇轩 | 50106070 | PM / Lead | 前置页（Title / Declaration / Abstract / TOC）+ **Ch7** Conclusions and Future Work ＋ **附录 A** Group Workload Profile ＋ 总集成 | 6–7 | （组长自留） |

**正文合计 48–59 页**（官方要求 40–60 页，从此 Introduction 到 Conclusions 计）。

---

## 3. 两步交付节奏（不要等到最后一天才交）

| 阶段 | 时间 | 交付物 | 判定标准 |
| :--- | :--- | :--- | :--- |
| **Step 1 骨架** | Week A 周日 23:59 | `reports/final_report/ch0X_<你的名字>/outline.md`：≥12 行三级标题 + 素材清单（用了哪些仓库文件/图/数据） | 打字不超过 90 分钟，但要能讲 3–4 分钟 |
| **Step 2 初稿** | Week B 周日 23:59 | 同目录下 `draft.md`（或 .docx）：达到目标页数的 60% | 表格已填、图已嵌入、引用已标注 |
| **Step 3 终稿** | Week C | 按审稿意见修订 + 格式统稿 | 通过 G2 门禁 |

> **G1 门禁规矩（请提前知道）**：Week A 逾期未交 outline，PM 将回收该章节自行代写，并在报告 **附录 A · Group Workload Profile**（MyAberdeen 官方模板）中如实记录 `0%` 贡献。这不是威胁，是课程要求我们如实申报分工。
>
> **附录 A 是全员签署文件**：对贡献比例有异议的人不签字，并在截止前邮件 Course Coordinator。所以每个人交的东西都会被真实记账——早交早安全。

---

## 4. 群内分发话术（可直接复制粘贴）

```text
【Cycle 3 · Technical Report 分工通知】

这周期我们不写新代码了。软件已经封版：8 个 API 端点、145 个测试全绿、12 题 36 个陷阱、3 张 UML 图都在仓库里。
现在唯一缺的是报告，而报告占期末成绩的 50%（课程总分 = 报告 25% + 软件 15% + 演示 10%），目前是 0 页。

我按人拆了 9 个任务包，每个包里写清了：你负责哪章（按官方 Brief 的章节编号）、多少页、每小节写什么、
素材在仓库的哪个文件、哪些写法会被退回、以及老师可能会问你哪 3 个问题。
文件在仓库：reports/cycle3_task_packs/，找自己的学号打开就行。

两步交付，不要拖：
1) 本周日 23:59 前交一页 outline（章节三级标题 + 你要用的素材清单），90 分钟内能完成；
2) 下周日 23:59 前交初稿（写到目标的 60% 就行）。

素材全是现成的：题库、测试清单、UML 图、竞品分析、MMLU 实验数据都在仓库，不需要你从零编，也不需要编。

另外两个硬约束先说清楚：
· 报告正文不许贴源码（官方 Brief 明令），伪代码/JSON/表格可以；
· 所有数字必须能追到仓库文件，写不出出处的一律删掉——报告会被 Turnitin 查重，也会被当面提问。

这周末组会我会按每人负责的章节点名提问，问题都在 reports/supervisor_qa_defense_library.md 里。
```

---

## 5. 全组通用写作规范（每份任务包里都会重复强调）

| 项 | 规定 |
| :--- | :--- |
| 语言 | **英文**（报告正文）。中文只用于 outline 与群内沟通 |
| 纸张格式 | **A4**、四边页边距 **2.54 cm**、**单栏**、字号 **12 pt**、字体 **Times New Roman**（或 Arial）、行距 **1.5** |
| 提交 | 单一 PDF，Turnitin 查重 |
| 拼写 | **英式**：organisation / prioritise / behaviour / analyse / programme |
| 标题层级 | `1.` / `1.1` / `1.1.1`，最多三级；一级加粗，二三级常规 |
| 图表 | 图下方 `Figure N: <caption>. (Source: <file/field>)`；表上方 `Table N: caption.` |
| 引用 | Harvard：正文 `(Sommerville, 2020)`；文末按姓氏字母排序；**卷期页码自己核对，不许凭记忆写 DOI** |
| 数字 | **正文每个数字必须能追到仓库文件**，写不出出处的一律删掉 |
| 人称 | 第一人称复数 `we`；被动语态不超过 30% |
| 时态 | 设计与实现用过去时（we chose / we implemented）；事实性结论用现在时 |
| 单句长度 | ≤30 词；长句拆开 |
| 源码 | **正文禁止贴源码**（Brief 硬规定）；伪代码（≤20 行）、JSON 示例、表格、目录树可以 |
| 禁用词 | 中文：赋能 / 闭环 / 生态 / 全方位 / 深度融合 / 综上所述；英文：leverage（除金融语境）/ cutting-edge / state-of-the-art（除非有引用支撑）/ seamlessly / revolutionise |
| 交付格式 | Markdown 或 DOCX 均可，但**必须附一份 `sources.md`** 列出你引用到的仓库文件路径 |

### 5.1 图表编号已全组锁定（改编号必须先问吴宇轩）

- **Figure**：1.1 价值主张画布 / 1.2 竞品定位图 / 2.1 MoSCoW 分布 / 3.1 用例图 / 3.2 答题状态机 / 4.1 四层架构 / 4.2 context model / 4.3 类图 / 4.4 diagnose 时序 / 5.1 软件结构 / 5.2 陷阱因果链 / 5.3 Trap Drawer 截图 / 5.4 主控制台截图 / 5.5 部署拓扑 / 6.1 测试金字塔 / 6.2 MMLU Δ 柱状图 / 7.1 12 个月路线图（共 17 图）
- **Table**：1.1 竞品矩阵 / 1.2 SMART / 1.3 Personas / 2.1 需求来源 / 2.2 MoSCoW 14 行 / 2.3 NFR 规格 / 3.1 用例摘要 / 4.1 ADR / 5.1 技术栈 / 5.2 八端点契约 / 5.3 领域模型字段 / 5.4 12 题分布 / 5.5 TrapDetail 四字段 / 5.6 查表 vs LLM / 5.7 环境要求 / 6.1 测试文件清点 / 6.2 对抗性六组 / 6.3 MMLU 12 学科 / 6.4 RAGAS / 6.5 需求达标评估 / 7.1 商业化假设（共 21 表）

---

## 6. 需求编号已冻结（R01–R14）

| ID | 需求 | 优先级 |
| :--- | :--- | :-: |
| R01 | 按学科浏览题目 | Must |
| R02 | 提交作答 | Must |
| R03 | **选项级**诊断（非题目级） | Must |
| R04 | 五维能力雷达与趋势 | Must |
| R05 | 学情摘要卡 | Must |
| R06 | 登录与注册 | Must |
| R07 | 中英双语界面 | Should |
| R08 | 明/暗双主题 | Should |
| R09 | 离线零构建运行 | Must |
| R10 | GraphRAG 图谱增强（**部分满足**） | Should |
| R11 | 多用户 / 多租户隔离 | **Won't** |
| R12 | 移动原生 App | **Won't** |
| R13 | 社交功能（排行榜 / 分享） | **Won't** |
| R14 | 自动组卷 / 自适应出题 | **Won't** |

**引用规则**：R01–R14 的编号与措辞由张梓健（任务包 02）定义并冻结。谢炜昕（Ch3 Table 3.1 与附录 B）、杨明杰（Ch6 Table 6.5）必须**逐字引用**，不得改写。

---

## 7. 每人必须能回答的"抽查三问"机制

每份任务包末尾都有 **3 个导师可能问的问题 + 30 秒答法**。组会前 24 小时，PM 会随机抽人回答。答不上来的一律按"本章尚未完成"处理——因为报告里的字不是你写的，评审一问就露。

这不是形式主义：导师上次说我们**"太像 AI agent 做的"**，最直接的解药就是**换人来答也能答上来**。

---

## 8. 提交前全组必查清单（Week C 由谢炜昕统稿时逐项打勾）

- [ ] 正文 40–60 页（Ch1–Ch7），不含前置页/参考文献/附录
- [ ] 格式：A4 / 2.54 cm / 单栏 / 12 pt / Times New Roman / 1.5 倍行距
- [ ] **全文无源码**（搜索 `def ` / `import ` / ```python）
- [ ] 17 图 21 表编号连续、无重号，且每张图都在正文被引用过
- [ ] R01–R14 在 Ch2 / Ch3 / Ch6 三处编号与措辞一致
- [ ] 引用与文献列表一一对应（无孤儿引用、无缺项）
- [ ] 附录 A 用 **MyAberdeen 官方模板**，10 人签署
- [ ] PoC ZIP：源码 + 可运行版本 + 依赖 + **User Manual（PDF 8–12 页）**
- [ ] 演示：PPTX + **MP4 且全员出镜**，15 分钟
- [ ] 🔴 **凭证泄露已处理**：`graphrag（终）/real_graph_engine.py` 的 Neo4j 账号密码已移除、Aura 密码已重置、ZIP 内无明文凭证
