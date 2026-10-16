# JC2001 Group 5 项目与第三周规划假设登记表 (Assumptions Log)

**项目名称**：基于知识图谱与智能排雷的大学生理工科智能助学系统（Smart Study Assistant System）  
**课程编号**：JC2001 Introduction to Software Engineering (2026–27)  
**文档路径**：`reports/assumptions.md`  
**最后更新**：2026年10月17日  
**基准依据**：`JC2001-GroupProjectDescription-and-Requirements-2026-27(1).pdf` 与现有 PoC 基线

---

## 1. 事实与假设边界总则

依据软件工程规范与评审纪律，本团队严格区分“已验证事实”与“推演/阶段性假设”，杜绝将未验证推测作为完成依据：

- **已验证事实 (Facts)**：有实际运行代码、已执行通过的自动化测试（如 114 个 pytest 测试用例）、官方课程规范文字、已归档图件或已提交提案。
- **阶段性假设 (Assumptions)**：在当前阶段（第三周 / M2.2 准备期）为推进设计与分工而设定的前置条件与预期，后续需经导师确认、用户实测或联调验证予以转正或修正。

---

## 2. 关键假设清单及其对结论的影响

| 编号 | 核心假设 (Assumption) | 事实依据 (Grounding Fact) | 对结论/架构/交付的影响 | 验证/转正方式 | 当前状态 |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **ASM-01** | **Reports 模块“完成一半”指核心业务主流程闭环（50% 核心链路）而非全功能堆砌** | 导师反馈要求“太像 AI 做，下周期把 reports 做到起码 half 进度” | 团队集中攻克“时间/范围筛选 -> 核心学情指标 -> 趋势与分布 -> 数据来源/时间戳”一条垂直切片，不分散精力做无效静态页面。 | 本周初向导师汇报此定义并获得认可。 | 待确认 (Pending) |
| **ASM-02** | **第三周 PoC 阶段学情数据可使用标注清晰的 Session / Mock 数据服务** | 当前处于 Phase 2 架构设计阶段，真实云端 Neo4j 完整图谱与持久化学生答题日志按 Proposal 规划在 Phase 3 (M3.2) 上线 | 避免在第三周强行引入重型数据库造成过度设计；接口明确返回 `source: "mock"` 或 `source: "session"`，诚实展示技术演进阶段。 | 导师确认允许原型阶段标注 mock，期末联调前替换为真实数据源。 | 活跃有效 (Active) |
| **ASM-03** | **Reports 优先服务学生自我学情诊断（Student Persona）而非教师大屏** | Proposal 中核心目标是帮助本科生解决复习超载与错因定位，PoC 当前为学生端控制台 | 第三周暂缓开发教师端班级宏观热力图（Cohort Heatmap），防止需求膨胀导致两头未落定。 | 纳入第三周提问清单第 2 题向导师核对。 | 活跃有效 (Active) |
| **ASM-04** | **40–60 页技术报告在第三周只需完成骨架锁死与核心章节初稿（约 15–20 页）** | 官方评分标准要求 Technical Report 在期末提交，正文 40–60 页，不计代码 | 避免组员在需求与架构未最终冻结时盲目水字数；第三周以结构、追踪矩阵（RTM）和核心图件为主。 | 对齐课程第 6 周节奏与期末进度要求。 | 活跃有效 (Active) |
| **ASM-05** | **本地一键运行（FastAPI + Vanilla JS SPA）符合 PoC 考核中关于“Runnable Software”的要求** | 官方 PoC 规范（Page 7）要求“Complete source code required to run and evaluate... does not need to be production-ready” | 团队无需额外维护 Docker/K8s 集群，降低组员运行门槛，保持本科生级别高质量代码简洁性。 | 在 User Manual 中给出本地一键启动测试验证步骤。 | 活跃有效 (Active) |
| **ASM-06** | **苏格拉底式反问（不直接泄露答案）是系统区别于常规 AI 助手的核心学术护城河** | 官方评分侧重“Consistency with Technical Report”及项目创新与教育价值 | 诊断接口在任何降级模式下都必须坚持反问式启发，不得因为图谱未命中直接打印标准答案。 | 纳入自动化测试契约（如 `test_diagnose.py` 断言）。 | 活跃有效 (Active) |

---

## 3. 假设失效应急预案 (Contingency Plans)

1. **若导师坚持 Reports 必须具备真实数据库存储**：
   - 立即启用 SQLite 作为单机轻量过渡数据库，记录学生本地答题日志，耗时预计增加 3–4 小时，不影响全局架构。
2. **若导师要求 Reports 必须包含教师视角**：
   - 在前端预留“角色切换（Student / Instructor Preview）”模拟视角，并在报告中诚实声明教师聚合数据为算法仿真样本。
