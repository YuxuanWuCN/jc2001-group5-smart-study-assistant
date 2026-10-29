# JC2001 Week 6 User Interaction Modeling Lab: University Library System

> **课程代码**: JC2001 Introduction to Software Engineering (2026-27)  
> **实验题目**: User Interaction Modeling Lab / Class Exercise — University Library System  
> **绘制工程文件**: [`reports/diagrams/JC2001_Week6_UML_Lab_Practices.drawio`](file:///d:/jc2001/reports/diagrams/JC2001_Week6_UML_Lab_Practices.drawio)  
> **快捷启动入口**: [`reports/diagrams/open_in_drawio.html`](file:///d:/jc2001/reports/diagrams/open_in_drawio.html)

---

## 1. 实验交付物清单 (Submission Requirements)

按 `User-Case-Diagram-Lab.pdf` 要求，提交内容包含以下三部分：
1. **识别的参与者（Actors）与用例（Use Cases）清单**；
2. **`<<include>>` 与 `<<extend>>` 关系的理论与业务逻辑解释**；
3. **完整的 UML 用例图（可在 draw.io 中直接导出 PNG/PDF）**。

---

## 2. 参与者与用例识别 (Tasks 1 & 2)

### 2.1 参与者 (Actors) 识别（满分 20 分）
* **`Student`（学生 - 主要人类用户）**：
  * 系统的一般使用者，发起查书、借书、还书等核心图书流转行为。
* **`Librarian`（图书管理员 - 管理类用户）**：
  * 负责系统的后台维护与运营，包括编目维护图书记录、查验学生的逾期罚款情况。
* **`Timer / Reminder Service`（系统后台定时服务 / 系统角色）**：
  * 课件问题描述中明确提及：*“The system automatically sends reminders for overdue books.”*（系统自动发送逾期催还提醒）。在 UML 规范中，此类无人值守、周期性自动触发的后台调度服务通常建模为系统参与者（`<<system>>` Actor），以凸显其事件驱动的自主性。

---

### 2.2 核心用例 (Use Cases) 识别（满分 20 分，要求 $\ge 5$ 个）
系统边界框内识别了以下 7 个核心业务用例（远超要求的 5 个）：
1. **`Search Books`（检索图书）**：支持学生按书名、ISBN、作者、类别等条件查询馆藏与在架状态。
2. **`Borrow Book`（借阅图书）**：学生办理借书手续，扣减可借额度并记录借阅日期与应还日期。
3. **`Return Book`（归还图书）**：学生归还图书，更新馆藏库存状态。
4. **`Verify User & Borrowing Eligibility`（验证用户身份与借书资格）**：*（被包含用例）* 验证借阅证有效性、未缴罚款上限及剩余借书配额。
5. **`Pay Overdue Fine`（缴纳逾期罚款）**：*（扩展用例）* 还书时如果发现逾期，条件触发计算罚金并进行在线或前台支付。
6. **`Manage Book Records`（管理图书记录）**：图书管理员对图书数据进行录入、更新、报损、下架等日常管理。
7. **`Check Overdue Fines`（检查逾期罚款记录）**：图书管理员审查特定学生或全馆的罚金未缴清单与催缴记录。
8. **`Send Overdue Reminders`（发送逾期催还提醒）**：定时服务自动扫描逾期记录，向相关借阅人推送邮件或系统消息。

---

## 3. 核心用例关系解释 (Task 4: Explain Relationships)

### 3.1 `<<include>>` 关系解释（满分 20 分）
* **关系定义**：基础用例（Base Use Case）在执行过程中，**必须、无条件且完整地调用**被包含用例（Inclusion Use Case）的功能。它用于提取和复用公共行为，基础用例自身若不包含被包含用例则是不完整的。
* **箭头方向**：从基础用例指向被包含用例（虚线开箭头）：  
  $$\text{Borrow Book} \xrightarrow{\quad \ll\text{include}\gg \quad} \text{Verify User \& Borrowing Eligibility}$$
* **业务理由（Rationale）**：
  在图书借阅流程中，系统不能直接办理出借，必须在交易确认前强制执行借阅人身份鉴权、账号状态排查（是否被挂失/冻结）、以及借书额度核验。将该逻辑抽象为独立的 `Verify User & Eligibility` 用例，不仅保证了借书流程的安全性，还能在未来被其它需要鉴权的高权限用例（如预约紧俏图书）复用。

---

### 3.2 `<<extend>>` 关系解释（满分 20 分）
* **关系定义**：扩展用例（Extension Use Case）在**满足特定前提条件（Extension Point / Condition）**时，为基础用例（Base Use Case）提供可选的增量或异常行为。基础用例本身具有完整的业务语义，不依赖扩展用例即可独立完成。
* **箭头方向**：**必须从扩展用例指向基础用例**（虚线开箭头，注意 UML 标准规范是子/增量指向父/基础）：  
  $$\text{Pay Overdue Fine} \xrightarrow{\quad \ll\text{extend}\gg \quad} \text{Return Book}$$
  * *扩展触发点 (Extension Point)*: `Condition: if the book is overdue`（当图书逾期时触发）。
* **业务理由（Rationale）**：
  普通的“还书（`Return Book`）”用例本身是一个独立的完整操作（还书成功即入库）。只有在图书被系统检测为“超过应还日期”的特殊分支情形下，系统才会引导进入“缴纳逾期罚款（`Pay Overdue Fine`）”流程。如果按期归还，则该扩展行为根本不会被执行。因此将其建模为 `<<extend>>` 严格符合 UML 规范。

---

## 4. draw.io 工程说明与导出指南

工程文件已经保存在：
`d:\jc2001\reports\diagrams\JC2001_Week6_UML_Lab_Practices.drawio`

### 4.1 四个标签页对应内容：
1. **`1. Library Use Case Lab`**：大学图书馆系统用例图（本次评分大作业，包含配色、系统边界、规范虚线箭头、角色及设计注解）。
2. **`2. Practice - Exam Use Case`**：`UML Draw Practices.pdf` 练习 1（考试系统用例图：Student, Administration, Registration, Test, Report）。
3. **`3. Practice - Activity Diagram`**：`UML Draw Practices.pdf` 练习 2（用户登录验证活动图：输入密码 $\to$ 提交 $\to$ 数据库校验 $\to$ 分支判断通过/拒绝/重试）。
4. **`4. Practice - Class Diagram`**：`UML Draw Practices.pdf` 练习 3（`Document` 基类与 `Book`、`Email` 派生子类继承图，规范空心三角箭头）。

### 4.2 导出交作业方法：
1. 在 Edge 浏览器中打开的 draw.io 页面中；
2. 点击顶部菜单：**文件（File） $\to$ 导出为（Export as） $\to$ PNG（或 PDF）**；
3. 选择“仅当前页面”或“所有页面”导出即可获得高清无水印实验作业图。
