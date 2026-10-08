# 💻 JC2001 Group 5 开工任务包（三）：PoC 核心开发与算法组

**责任人**：江昊 (50106065，后端主导)、董思钦 (50106060，逻辑与算法主导)  
**对接组长**：吴宇轩 (50106070) | **审核人**：王思鉴 (50106045)  
**关键交付节点**：**2026 年 10 月 10 日（周六）晚 22:00（完成首个本地可跑后端脚手架）**  
**预计投入时间**：每人约 4–5 小时

---

## 🎯 本周核心目标
拒绝过度设计！按照本科生高分标准，搭建一个**轻量、清晰、本地 `uvicorn` 一键可启动的 FastAPI 后端服务脚手架**，锁定关键数据契约（Pydantic Schemas），并跑通 `/api/quiz` 与 `/api/diagnose` 两个基础接口的 Mock/联调。

---

## 📌 你们需要完成的交付物清单

### 1. 绝对不能破坏的数据契约（Pydantic Schemas）
为了防止前后端联调翻车，**所有人必须严格遵循以下数据格式**（江昊在路由中直接使用，董思钦在 Prompt 输出解析中直接组装）：

```python
from pydantic import BaseModel, Field
from typing import Dict, List, Optional

# --- 1. 题目数据模型 ---
class QuizItem(BaseModel):
    question_id: str = Field(..., example="Q_ECON_01")
    subject: str = Field(..., example="economics")
    stem: str = Field(..., example="当需求价格弹性大于 1 时，降价会使总收益如何变化？")
    options: Dict[str, str] = Field(..., example={"A": "增加", "B": "减少", "C": "不变", "D": "不确定"})
    answer: str = Field(..., example="A")
    trap_hint: Optional[str] = Field(None, description="预设的干扰项陷阱标签")

# --- 2. 诊断请求与响应模型 ---
class DiagnoseRequest(BaseModel):
    question_id: str = Field(..., example="Q_ECON_01")
    selected_option: str = Field(..., example="B")

class DiagnoseResponse(BaseModel):
    is_correct: bool = Field(..., example=False)
    trap_name: str = Field(..., example="反向弹性误判陷阱")
    concept_name: str = Field(..., example="需求价格弹性与总收益关系")
    socratic_guidance: str = Field(..., example="想一想降价引起的需求量增加比例，是否大于价格下降的比例？")
    fallback_mode: bool = Field(False, description="是否启用了离线兜底模式")
```

---

### 2. 极简后端目录结构规划（推荐置于 `backend/`）
```text
backend/
├── main.py              # FastAPI 实例、CORS 中间件、挂载路由
├── config.py            # 读取 .env (QWEN_API_KEY, NEO4J_URI 等)
├── models/
│   └── schemas.py       # 上述 Pydantic 数据模型定义
├── api/
│   └── routes.py        # /api/quiz 与 /api/diagnose 接口定义
└── services/
    ├── qwen_service.py   # 董思钦主责：Qwen Prompt 组装与调用封装
    └── graph_service.py  # 江昊主责：Neo4j Cypher 查询（可先提供 Mock 数据）
```

---

### 3. 分工细节与示范代码桩

#### 👨‍💻 江昊（后端骨架与接口路由）：
1. 负责在 `backend/main.py` 配置 **CORS（跨域中间件）**，允许所有本地端口访问（`allow_origins=["*"]`），以便 `frontend/index.html` 无阻碍联调；
2. 在 `backend/api/routes.py` 实现两组接口：
   - `GET /api/quiz?subject={subject}`：从本地 CSV 或静态题库返回 3–5 道题目数据（格式对齐 `List[QuizItem]`）；
   - `POST /api/diagnose`：接收 `DiagnoseRequest`，调用董思钦的 `qwen_service` 返回 `DiagnoseResponse`。

#### 👨‍💻 董思钦（Prompt 封装与离线兜底服务）：
编写 `backend/services/qwen_service.py`，实现结构化排雷提示词解析。**核心原则：即使网络断网或没配 API Key，也绝不能抛出 500 异常崩溃**：
```python
def generate_socratic_diagnosis(stem: str, user_choice: str, correct_choice: str) -> dict:
    """
    调用 Qwen-Turbo 获取诊断，具备自动 try-except 本地离线兜底保护
    """
    try:
        # TODO: 从环境变量获取 QWEN_API_KEY 并发起调用
        # prompt = f"学生题目：{stem}，正确答案是 {correct_choice}，学生误选了 {user_choice}。请用两句话指出考点盲区并启发提问。"
        # res = dashscope.Generation.call(...)
        pass
    except Exception as e:
        # 兜底降级逻辑，保证系统稳定可靠
        return {
            "is_correct": False,
            "trap_name": "核心概念混淆 (离线分析)",
            "concept_name": "基础考点定义",
            "socratic_guidance": "请回顾该定理的适用前提条件，特别注意自变量与因变量的正负相关性。",
            "fallback_mode": True
        }
```

---

## 🛠️ 组员实操与提交指引
1. **安装与启动命令**（极简，不引入冗余包）：
   ```bash
   pip install fastapi uvicorn pydantic python-dotenv
   # 启动后端（在 backend 目录下）：
   uvicorn main:app --reload --port 8000
   ```
2. **Git 提交**：
   - 江昊分支：`feature/jianghao-fastapi-scaffold`
   - 董思钦分支：`feature/dongsiqin-qwen-service`
   - 提交命令：`git commit -m "jianghao: scaffold fastapi with quiz and diagnose endpoints"`
3. **完成时间**：**10 月 10 日（周六）晚 22:00 前**，在本地浏览器访问 `http://127.0.0.1:8000/docs` 能看到自动生成的 Swagger 文档并成功点击 Execute 测试！
