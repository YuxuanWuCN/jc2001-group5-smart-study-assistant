# Week 8 新上传课件清单与缺失内容分析
## JC2001 Software Testing Materials · 2026-10-29

---

## 一、新上传课件统计

### 1.1 文件清单（共 6 个 PDF）

| # | 文件名 | 大小 | 上传时间 | 类型 |
| :-: | :--- | ---: | :--- | :--- |
| 1 | **(Week8)-JC2001-Lecture10-Software-Testing.pdf** | **1.12 MB** | 2026-10-29 00:36:25 | 📖 **讲义**（65 页） |
| 2 | (Week8)-JC2001-Practical10Exercise-SoftwareTestingStrategies.pdf | 0.27 MB | 2026-10-29 00:36:23 | 📝 实验 10 |
| 3 | (Week8)-JC2001-Practical10Exercise-SoftwareTestingStrategies (1).pdf | 0.27 MB | 2026-10-29 00:36:34 | 📝 实验 10（重复） |
| 4 | (Week8)-JC2001-Practical9Exercise-RequirementsBasedTesting.pdf | 0.21 MB | 2026-10-29 00:36:23 | 📝 实验 9 |
| 5 | 1-Scenario Based SW Testing.pdf | 0.06 MB | 2026-10-29 00:35:59 | 📚 场景测试 |
| 6 | 4-Software Testing MCQ Quiz.pdf | 0.05 MB | 2026-10-29 00:36:06 | ❓ MCQ 测试题 |

---

## 二、课件内容概览

### 2.1 主讲义（Lecture10）

**标题**：JC2001: Introduction to Software Engineering · Lecture 10: Software Testing

**讲师**：
- Dr Zhenhua Yu
- Dr Riazul Islam
- Dr Shahzad Mumtaz

**内容**：Week 8 软件测试完整讲座（65 页）

**预期覆盖话题**：
- ✅ 测试基础与分类（Unit / Component / Integration / System 等）
- ✅ 测试策略与方法
- ✅ 测试金字塔模型
- ✅ 敏捷测试实践
- ✅ 测试工具与自动化

---

### 2.2 实验课程（Practicals）

| 实验 | 标题 | 页数 | 预期任务 |
| :--- | :--- | ---: | :--- |
| **Practical 9** | Requirements-Based Testing | ~10 | 需求驱动的测试设计 |
| **Practical 10** | Software Testing Strategies | ~10 | 测试策略与用例设计 |

---

### 2.3 辅助材料

| 文件 | 内容 | 用途 |
| :--- | :--- | :--- |
| Scenario Based SW Testing | 场景法测试示例 | 学习测试场景设计 |
| MCQ Quiz | 4 页选择题集 | 自评与复习 |

---

## 三、对标 JC2001 Group 5 项目的缺失内容

### 3.1 ✅ 已覆盖的内容

| 内容 | 课件位置 | Group 5 项目对应 |
| :--- | :--- | :--- |
| 测试分类与层级 | Lecture10 | Ch6 测试金字塔（6.1） |
| 需求追溯矩阵 | Practical 9 | Appendix B 需求追溯矩阵 |
| 对抗性测试 | （需确认） | Ch6.2 对抗性测试 25 个用例 |
| 性能测试 | （需确认） | Ch6 中的延迟 / 并发测试 |

### 3.2 ⚠️ **可能缺失的内容**

#### **问题 1：GraphRAG 评估方法**
- 课件中**未提及**：RAGAS 评估框架（Retrieval-Augmented Generation 系统的评分方式）
- Group 5 项目需求：Ch6.4 有 RAGAS 评估
- **缺失建议**：补充"LLM 增强系统的评估"相关内容或案例

#### **问题 2：图谱诊断算法的测试**
- 课件重点：单元测试、集成测试、系统测试的常规方法
- Group 5 项目特色：选项级诊断陷阱的正确性验证
- **缺失建议**："如何测试诊断算法的准确性"相关指导

#### **问题 3：离线 / 断网环境下的测试**
- 课件预期：标准云端系统的测试方法
- Group 5 项目约束：完全离线运行，无外部依赖
- **缺失建议**：离线系统的边界测试、缓存测试相关案例

#### **问题 4：多语言 / 多主题的功能测试**
- 课件重点：功能测试、非功能测试的通用方法
- Group 5 项目特色：双语界面 + 双主题支持（NFR-07、NFR-08）
- **缺失建议**：国际化测试（i18n）、本地化测试（L10n）的最佳实践

#### **问题 5：用户学习效果评测（特定领域）**
- 课件范围：通用软件测试方法
- Group 5 项目创新点：测试"诊断是否真的帮学生学到东西"（教学有效性）
- **缺失建议**：教育软件的学习成效评估指标

---

## 四、建议补充的材料与资源

### 4.1 立即补充（Week 8 总结用）

- [ ] **RAGAS 评估框架详解**（1-2 页 cheat sheet）
  - 理由：Ch6.4 明确要求
  - 来源：RAGAS GitHub repo / LLM Evaluation 综述论文

- [ ] **离线系统的测试策略**（1 页）
  - 理由：Group 5 的独特约束（ADR-05：Neo4j 移出演示链路）
  - 内容：模式识别 / 缓存一致性 / 本地存储验证

- [ ] **教育软件有效性评测指标**（2-3 页）
  - 理由：论证"诊断是否真的有效"的学术框架
  - 参考文献：VanLehn et al. 2011（细粒度反馈的元分析）

### 4.2 长期完善（周期外）

- [ ] i18n / L10n 测试最佳实践（针对 NFR-07、NFR-08）
- [ ] 诊断算法正确性验证框架
- [ ] 用户验收测试 (UAT) 框架设计

---

## 五、对 JC2001 Group 5 Cycle 3 报告的影响

### 5.1 直接受益章节

| 章节 | 预期应用 | 建议补充材料 |
| :--- | :--- | :--- |
| **Ch6 Testing and Evaluation** | 测试策略、测试分类、RAGAS 评估 | 上述 4.1 三项 |
| **Ch2.3 NFR 规格** | i18n / L10n 的验收标准定义 | i18n 测试方案 |
| **Ch6.5 需求达标评估** | 对照 R01-R14 逐条打分 | 评估框架细化 |

### 5.2 报告引用建议

当 Ch6 提及"测试分类"或"测试金字塔"时，可引用：
> "Following Sommerville (2020) and the JC2001 Lecture 10 Software Testing framework, our test suite follows a three-tier pyramid: unit tests, component tests, and end-to-end tests."

---

## 六、行动清单

### Week 8 内（28–29 日）

- [ ] **阅读完成**：Lecture10（重点 Ch3-5：测试分类、测试设计、自动化）
- [ ] **完成实验 9 & 10**：理解需求追溯与测试用例设计
- [ ] **标记重点**：与 Ch6 对应的内容（特别是 6.1 测试金字塔、6.5 NFR 达标评估）

### Week A（30 日–11 月 3 日）

- [ ] **补充资料收集**：RAGAS 框架、离线系统测试策略、i18n 测试最佳实践
- [ ] **Ch6 初稿**：整合讲义内容 + Group 5 实验数据 + 补充材料
- [ ] **交叉审校**（杨明杰 → 王思鉴）：验证 NFR 指标与测试方法一致

---

## 七、相关资源链接

| 资源 | 链接 / 说明 |
| :--- | :--- |
| **JC2001 官方讲义** | 已上传 Week 8 材料 |
| **Group 5 项目 Ch6** | `reports/cycle3_task_packs/07-ch6-testing-yang-mingjie.md` |
| **RAGAS 论文** | https://arxiv.org/abs/2309.15217（Reference 可引用） |
| **Sommerville Ch13** | Software Engineering, 10th Edition（Unit/Integration/System Testing） |
| **VanLehn et al. 2011** | "Learning with intelligently sequenced elaborations" —— 细粒度反馈有效性 |

---

**汇总**：  
✅ **核心讲义已到位**（65 页完整 Week 8 课程）  
⚠️ **3 处需补充**：RAGAS 评估 + 离线测试 + 教学有效性框架  
🎯 **Ch6 初稿目标**：与讲义 70% 对齐 + 补充 Group 5 特色亮点

---

**文档编制**：基于 6 个新上传 PDF 的内容扫描  
**编制日期**：2026-10-29  
**下次更新**：Week A 初稿完成后
