# 实现计划：前端视觉巅峰重构与现代 AI 交互体验升级 (Frontend Visual Overhaul & Modern AI UX)

**分支**：`002-frontend-visual-overhaul` | **日期**：2026-10-10 | **规格**：[spec.md](spec.md)  
**输入**：来自 `specs/002-frontend-visual-overhaul/spec.md` 的功能规格与用户反馈“你的前端不够看啊”

---

## 概要

针对用户反馈“前端界面不够看、缺乏顶级现代 AI 产品的视觉质感与交互震撼度”的问题，本计划制定并落地**前端视觉巅峰重构与现代 AI 交互升级体系**。
全面借鉴 Linear / Vercel / Raycast / DeepSeek 国际顶尖设计美学，在保持纯原生极速秒开（零重型构建黑盒）的前提下，落地以下五大关键突破：
1. **流光极光视差门户 (Aurora Hero & Matrix Grid)**：打造具备工程点阵网格、微妙流光渐变、动态指标卡片与鼠标聚光灯跟随高光的顶级学术门户；
2. **交互式双核对比沙盒 (Interactive Comparison Sandbox)**：在首页与控制台内置“传统刷题（冷硬判断、只给答案）” vs “智学罗盘（陷阱雷达预警、先修溯源、启发反问）”的一键拨动对比演播台；
3. **沉浸式控制台微交互升级 (Workspace Micro-interactions)**：引入 DeepSeek-R1 风格的**思维链折叠面板 (Reasoning Accordion)**、错题脉冲震颤、磨砂玻璃浮层与考点拓扑高亮光环；
4. **全局极客 HUD 快捷指令控制台 (Command Palette `Cmd+K` / `Ctrl+K`)**：支持全键盘模糊搜题、跨学科一键直达与主题切换；
5. **学情雷达战力勋章系统 (Radar Defense Badge)**：将学情报告升级为带动态扫描光效与 S/A/B/C 级防守勋章的高能看板。

---

## 技术背景

- **语言/版本**：原生 ES6+ JavaScript, HTML5 语义化标签, 现代 CSS3 (CSS Variables, Grid, Backdrop-Filter)
- **主要依赖项**：Apache ECharts 5.5.1 CDN（无任何新增外部重型构建依赖）
- **存储**：浏览器本地持久化缓存（`localStorage`：`smartstudy_auth_session`, `smartstudy_theme`, `smartstudy_radar`）
- **测试**：后端 `pytest tests/`（114 个用例 100% 自动化测试），前端基于 Chrome/Edge 浏览器全视口与控制台交互走查
- **目标平台**：现代 Chromium 浏览器 / Edge / Firefox / Safari，响应式自适应移动端与超宽屏桌面
- **项目类型**：FastAPI 单体静态挂载原生单页面应用 (Vanilla SPA)
- **性能目标**：首次内容渲染 (FCP) < 80ms，交互转场 60 FPS 硬件加速，HUD 弹窗唤起 < 50ms
- **约束条件**：
  1. 严格遵守阿伯丁大学 JC2001 本科生软件工程规范，学术表达严谨；
  2. 保持对已有 114 个自动化后端测试与已部署的 FastAPI 端点 100% 零破坏兼容；
  3. 严格执行零根目录污染、外科手术式精准修改与空间整洁原则。
- **规模/范围**：涵盖 Landing 门户、对比沙盒、刷题排雷工作台、学伴推理流、考点图谱漫游、学情雷达、HUD 指令弹窗共 7 大核心模块。

---

## 宪章检查 (Constitution Checks)

| 宪章原则 | 检查状态 | 评估与正当化理由 |
| :--- | :---: | :--- |
| **原则 I: 顶级学术与 AI 视觉审美** | ✅ 通过 | 摆脱粗糙后台风格，采用 Cyber Obsidian / Technical Chalk 材质系统，视觉质感直接比肩行业标杆。 |
| **原则 II: 原生轻量与零打包负担** | ✅ 通过 | 纯原生 CSS3 + ES6 实现，零 Webpack/Vite 依赖，彻底消除环境配置门槛与网络加载白屏。 |
| **原则 III: 零破坏性兼容与回归** | ✅ 通过 | 纯增量式 UI 与微交互升级，不修改后端数据契约，现有 114 个 pytest 测试百分之百通过。 |
| **原则 IV: 双模自适应与多端响应式** | ✅ 通过 | 完整支持深浅双主题无缝切换，色彩对比度达 WCAG AA 标准，移动端完美适配手势交互。 |
| **原则 V: 零根目录污染与空间纪律** | ✅ 通过 | 所有规格文档归集于 `specs/002-frontend-visual-overhaul/`，修改精准限制在 `frontend/` 目录。 |

---

## 项目结构

### 规范工件 (此功能)

```text
specs/002-frontend-visual-overhaul/
├── spec.md              # 需求工程与用户故事规格书
├── plan.md              # 本实施计划文件
├── research.md          # 第 0 阶段：架构抉择与材质方案
├── data-model.md        # 第 1 阶段：实体模型与状态机定义
├── contracts/           # 第 1 阶段：UI 交互契约与后端兼容保障
│   └── ui-interaction-contracts.md
└── quickstart.md        # 第 1 阶段：快速启动与验收核对单
```

### 源代码变动区域 (Repository Layout)

```text
frontend/
├── index.html           # 升级 Hero 极光结构、注入对比沙盒、HUD 指令模态层与思维链容器
├── style.css            # 升级现代化设计系统变量、极光微光、网格纹理、毛玻璃与微动效
└── app.js               # 升级 CommandPalette 控制器、对比沙盒交互、聚光灯跟随与思维链渲染
```

---

## 复杂度跟踪

*无需填报（未触发任何架构门禁违规，无过度设计与非必要依赖引入）。*

---

## 实施阶段任务分解 (Work Breakdown)

### 阶段 0: 架构与技术调研 (已完成)
- [x] 产出 `research.md`：解决 Cyber Obsidian 材质体系、对比沙盒状态流转、DeepSeek 思考链折叠与聚光灯微动效方案。

### 阶段 1: 模型与契约设计 (已完成)
- [x] 产出 `spec.md`：明确极光视差门户、对比沙盒、工作台沉浸交互、HUD 指令台四大核心用户故事。
- [x] 产出 `data-model.md`：标准化 `CommandPaletteItem`、`ComparisonCase`、`ReasoningStep` 及 `RadarBadgeTier` 模型。
- [x] 产出 `contracts/ui-interaction-contracts.md`：明确 UI 控制器交互契约与向后 API 兼容保障。
- [x] 产出 `quickstart.md`：制定 8 项全维度验收核验单。

### 阶段 2: 精准实施编码 (Ready to Execute)
1. **CSS 现代设计系统与质感升级** (`frontend/style.css`)：
   - 注入顶级极光微光渐变、点阵网格纹理背景、毛玻璃亚克力面板类；
   - 增加卡片聚光灯跟随高光 (Spotlight Border) 与发光按钮微交互；
   - 实现 DeepSeek-R1 风格的 `<details>` 深度思考折叠动效与五维战力勋章样式；
   - 实现全局 Command Palette HUD 模态层与快捷键提示徽章样式。
2. **HTML 骨架与交互容器注入** (`frontend/index.html`)：
   - 在 Hero 区域注入流光排版、动态学术遥测指标卡片；
   - 注入“传统刷题 vs 智学罗盘”分屏交互对比演播台 (Interactive Sandbox)；
   - 在工作台与学伴视图中注入思考链容器；
   - 注入全局 Command Palette HUD 模态节点结构。
3. **JS 交互控制器与状态机联动** (`frontend/app.js`)：
   - 编写 `initCommandPalette()` 支持 `Cmd+K` / `Ctrl+K` 全局快捷指令；
   - 编写 `initComparisonSandbox()` 支持即时点击对比与错因联动；
   - 编写 `renderReasoningTrace()` 为学伴与排雷注入呼吸感思考过程；
   - 编写 `initSpotlightCards()` 注入鼠标流光跟随动效；
   - 联动中英双语与明暗主题自适应重绘。
4. **验证与回归**：
   - 运行 `pytest tests/` 验证 100% 测试通过；
   - 启动本地服务进行多视口交互走查与验收。