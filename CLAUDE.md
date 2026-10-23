# 智学罗盘 SmartStudy Assistant 开发指南（JC2001 Group 5）

自动生成自所有功能计划。最后更新：2026-10-18

## 活动技术

- **后端**：Python 3.13.14 + FastAPI + Pydantic v2（`CamelModel` 双命名同步）
- **前端**：原生 HTML5 / CSS3 / ES6+，零构建工具（宪法原则 II）
- **图谱**：Neo4j + GraphRAG 自建管线（`graphrag（终）/`）
- **评测**：pandas 3.x / numpy 2.x / matplotlib 3.x（离线脚本，无新增依赖）
- **测试**：pytest（`tests/` 9 个文件 / 145 用例）
- **规范工具链**：spec-kit（`.specify/`），PowerShell 脚本

## 项目结构

```text
D:\jc2001\
├── backend\app\           FastAPI 应用（models/, data/, routers/）
├── frontend\              index.html + app.js + styles.css（零构建）
├── graphrag（终）\         GraphRAG 管线 + MMLU 测试集 CSV（12 学科，n=4,445）
├── reports\               Cycle 3 报告正文与任务包（cycle3_master_plan.md 为总纲）
├── specs\                 001–004 规范包（spec/plan/research/data-model/contracts/quickstart）
├── scripts\               离线审计与评测脚本
├── tests\                 pytest 回归基线（145 用例，计数为报告既定口径）
├── .specify\              spec-kit 脚手架（memory/constitution.md 章程 v2.0.0）
└── CLAUDE.md / GEMINI.md  代理上下文文件
```

## 命令

```powershell
# 测试（必须 100% 通过，宪章质量门禁）
python -m pytest tests/ -q

# 启动后端
python backend/app/main.py

# 审计（功能 004）
python scripts/audit_hallucination_l1_l3.py
python scripts/audit_persona_claims.py
python scripts/audit_online_baseline.py     # 无 QWEN_API_KEY 时以退出码 0 跳过

# spec-kit
./.specify/scripts/powershell/setup-plan.ps1 -Json
./.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude
```

## 代码风格

- Python：PEP 8，类型注解齐全，Pydantic 模型统一继承 `CamelModel`（`backend/app/models/common.py`）以自动同步 snake_case / camelCase；禁止 `as any` 式绕过。
- 前端：ES6+ 原生语法，无打包器；CSS 变量驱动双主题。
- 文档：中文正文，禁用词清单见 `reports/cycle3_master_plan.md`（赋能/闭环/生态/全方位/深度融合/显著提升/综上所述、leverage/cutting-edge/seamlessly/revolutionise）。
- **根目录零污染**（章程原则 V）：临时脚本一律放仓库外（如 `C:\Users\45607\AppData\Local\Temp`）。

## 最近变更

- **004-persona-hallucination-audit**（2026-10-18）：新增画像证据等级 E0–E3、四级幻觉 L1–L4、结论等级 V0–V3；四份契约（`audit-result.schema.json`、`online-experiment.schema.md`、`report-claim-contract.md`、`quickstart.md`）。审计脚本落 `scripts/`、产物落 `reports/audit/`，不改动 `tests/` 计数。
- **003-cycle3-startup-report**：Cycle 3 报告七章 + 附录结构，21 表 / 17 图编号分配。
- **002-frontend-visual-overhaul**：Cyber Obsidian 视觉体系、对比沙盒、Reasoning Accordion、Command Palette。

<!-- 手动添加开始 -->
<!-- 手动添加结束 -->
