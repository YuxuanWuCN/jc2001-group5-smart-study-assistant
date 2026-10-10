# JC2001 Group 5 智学罗盘项目章程 (Constitution)

**项目名称**：基于认知图谱与出题陷阱拓扑的大学生理工科智能助学系统 (SmartStudy Assistant)  
**所属课程**：阿伯丁大学 JC2001 软件工程 (2026–27) · Group 5 (BSc BMIS)  
**版本**：2.0.0 | **最后修订**：2026-10-10  

---

## 核心开发与设计原则

### 原则 I: 顶刊级学术与前沿 AI 视觉审美 (Top-Tier Academic & AI Aesthetics)
- 界面视觉严禁低质粗糙，必须达到现代高水准技术产品（Linear / Vercel / Raycast / DeepSeek）的精致质感。
- 引入深度微光流光 (Ambient Glow)、网格矩阵底纹 (Technical Grid Texture)、分层玻璃拟态 (Backdrop-filter Glassmorphism) 与精准的排版层级对比。
- 保证信息呈现既有阿伯丁大学 Honours Project 的严谨学术规范，又具备震撼评委与用户的现代科技交互冲击力。

### 原则 II: 原生极速加载与零打包负担 (Vanilla ES6+ & Zero Build Friction)
- 坚持原生 HTML5 / CSS3 / ES6+ 架构，零 Webpack/Vite 复杂构建黑盒，保证本地浏览器即开即用（首次绘制时间 FCP < 100ms）。
- 组件设计模块化、高内聚，CSS 采用 CSS Variables 语义化设计 Token，JS 采用事件总线与清晰的状态机控制。

### 原则 III: 零破坏性兼容与测试门禁 (Zero Regression & Test Preservation)
- 现有 114 个 pytest 后端自动化测试、FastAPI 端点（`/api/health`, `/api/quiz`, `/api/diagnose`, `/api/graph`, `/api/tutor`）必须 100% 保持通过与协议兼容。
- 原有的功能逻辑、学号登录状态、本地缓存 (`localStorage`) 与错因拓扑核心推理链路严禁破坏。

### 原则 IV: 双模自适应与多端响应式 (Fluid Dual-Theme & Responsive Ergonomics)
- 全面原生支持“深空极光 (Dark Mode)”与“学术科技白 (Light Mode)”，色阶对比度严格达到 WCAG AA 级别。
- 响应式适配移动端、平板与 4K 超宽桌面，平滑过渡动效维持 60 FPS 硬件加速。
- 完整维持中英双语 (ZH / EN) 国际化无缝切换。

### 原则 V: 文件系统与空间纪律 (Zero Root Pollution & Space Hygiene)
- 严禁在项目根目录下创建任何临时脚本、中间测试文件或碎屑。
- 所有的规划文档、数据模型、API 契约均归拢于 `specs/002-frontend-visual-overhaul/` 对应结构中。

---

## 质量门禁与治理规则

1. **视觉与交互门禁**：任何新 UI 必须经过色彩对比度、视口自适应、微动效平滑度、双语匹配测试。
2. **回归门禁**：任何代码提交前后必须运行测试套件，保证 `pytest tests/` 保持 100% 通过。
3. **架构正当化**：不得为了炫技引入沉重臃肿的三方重型库，严守本科生软件工程可解释性与学术答辩防御性。