# 前端交互与 API 契约规约：视觉与体验重构 (Interaction & API Contracts)

**功能编号**：`002-frontend-visual-overhaul`  
**所属项目**：JC2001 Group 5 — 智学罗盘 (SmartStudy Assistant System)  
**日期**：2026-10-10  
**状态**：APPROVED  

---

## 1. 客户端交互控制器契约 (Client-Side JS Contracts)

### 1.1 全局 HUD 指令控制器 (`CommandPaletteController`)
提供极客级 `Cmd+K` 全局搜索与快捷操作通道：

```javascript
/**
 * 打开全局 HUD 指令悬浮窗
 * @param {string} [initialQuery=""] - 初始填充的搜索关键词
 */
function openCommandPalette(initialQuery = ""): void;

/**
 * 关闭全局 HUD 指令悬浮窗并释放焦点
 */
function closeCommandPalette(): void;

/**
 * 注册或扩充快捷指令
 * @param {Array<CommandPaletteItem>} items - 指令列表
 */
function registerCommands(items): void;
```

### 1.2 交互对比演播台控制器 (`SandboxComparatorController`)
用于在门户与演示场景下实时切换传统刷题与智学罗盘对比：

```javascript
/**
 * 切换沙盒显示模式
 * @param {'smartstudy' | 'traditional'} mode - 目标模式
 */
function setSandboxMode(mode): void;

/**
 * 触发沙盒干扰项错因联动
 * @param {string} optionKey - 选项键值 ('A' | 'B' | 'C' | 'D')
 */
function inspectSandboxOption(optionKey): void;
```

### 1.3 深度思维链动态渲染器 (`ReasoningRenderer`)
用于生成 DeepSeek-R1 风格的思维折叠面板：

```javascript
/**
 * 渲染或折叠 AI 思考推演路径
 * @param {HTMLElement} mountTarget - 挂载容器
 * @param {Array<ReasoningStep>} steps - 推理步骤列表
 * @param {boolean} [defaultOpen=false] - 是否默认展开
 */
function renderReasoningAccordion(mountTarget, steps, defaultOpen = false): HTMLElement;
```

### 1.4 卡片聚光灯跟随特效 (`SpotlightGlowEffect`)
在鼠标移动时动态注入坐标驱动微光流向：

```javascript
/**
 * 为容器元素绑定鼠标流光跟随监听
 * @param {HTMLElement} containerElement - 包含 .spotlight-card 的父级容器
 */
function initSpotlightCards(containerElement): void;
```

---

## 2. 后端 API 兼容性保证契约 (Backend API Compatibility)

本功能为纯前端视觉重构，**100% 保持与已有 FastAPI 接口的向后兼容**，不得破坏以下既有契约：

| 接口端点 | 方法 | 响应数据模型 | 兼容性保证要求 |
| :--- | :--- | :--- | :--- |
| `/api/health` | `GET` | `{ status: "ok", version: "1.0.0" }` | 保持健康探针原样 |
| `/api/quiz` | `GET` | `Array<QuestionEntity>` | 保持题干、选项、陷阱 ID 与拓扑数据模型不变 |
| `/api/diagnose` | `POST` | `DiagnosticResult` | 保持错因归因、先修短板与雷达扣减字段不变 |
| `/api/tutor` | `POST` | `SocraticResponse` | 保持启发式反问文本与引导级别不变 |
| `/api/graph` | `GET` | `{ nodes: [], edges: [] }` | 保持节点坐标、分类与关系边拓扑结构不变 |
