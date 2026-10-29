# 快速开始：运行画像合理性与幻觉审计

**功能编号**：`004-persona-hallucination-audit`
**分支**：`004-persona-hallucination-audit`
**目标读者**：组内任何一位成员（无需事先理解审计设计）
**预计耗时**：离线部分 < 30 分钟（含人工复核）；在线部分约 10 分钟（需 API Key）

> 本文件是**验证指南**，不是实现指南。它描述"审计脚本写完后，如何确认它做对了"。脚本本身的实现属于 `/speckit.tasks` + `/speckit.implement` 阶段。

---

## 0. 前置条件

```powershell
# 在仓库根目录 D:\jc2001 执行
git branch --show-current          # 必须是 004-persona-hallucination-audit
python --version                   # 期望 3.13.x
python -c "import pandas; print(pandas.__version__)"   # 期望 3.x，无新增依赖
```

**硬约束**（违反即视为不通过）：
- 不得新增任何 `requirements.txt` 依赖（NFR-5）。
- 不得在仓库根目录产生临时文件（NFR-4 / 宪法原则 V）。

---

## 1. 离线审计：一条命令跑出 L1–L3

```powershell
python scripts/audit_hallucination_l1_l3.py
echo $LASTEXITCODE     # 期望 0
```

**期望产物**（全部出现在 `reports/audit/`）：

| 文件 | 断言 |
| :--- | :--- |
| `l1_content_audit.csv` | 行数 = **84**（48 选项 + 36 陷阱） |
| `l2_attribution_audit.csv` | 行数 = **36** |
| `l3_leakage_audit.csv` | 行数 = **12** |
| `verdict.json` | 通过 `contracts/audit-result.schema.json` 校验；`determinism_check.identical == true` |

**逐条验收**

1. **分母不缩水**：`l1` 行数若少于 84，说明有条目被静默跳过 —— 这是最严重的失败模式，因为分母缩小会让错误率看起来更好。脚本必须**报错退出**而不是跳过。
2. **UNDECIDABLE 留在分母**：抽查任一 `human_verdict=UNDECIDABLE` 的行，确认 `is_in_denominator=true`。
3. **离线无生成面**：`verdict.json` 的 `l4.status` 必须是 `na_no_generation_face`，`l4.rate` 必须是 `null`（**不能是 0**）。用下面命令确认：

```powershell
python -c "import json;v=json.load(open('reports/audit/verdict.json',encoding='utf-8'));print(v['l4'])"
# {'layer': 'L4_reasoning', 'denominator': 0, 'numerator': 0, 'rate': None, 'coverage': 1.0, 'status': 'na_no_generation_face'}
```

4. **可复现**：
```powershell
python scripts/audit_hallucination_l1_l3.py
python -c "import json;print(json.load(open('reports/audit/verdict.json',encoding='utf-8'))['determinism_check'])"
# identical 必须为 True，两次哈希相同
```

---

## 2. 画像溯源审计

```powershell
python scripts/audit_persona_claims.py
echo $LASTEXITCODE     # 期望 0
```

**期望产物**：`reports/audit/persona_provenance.csv`、`reports/audit/requirement_persona_map.csv`

**逐条验收**

1. **三张 Persona 全覆盖**：至少每张 Persona 有 1 条"痛点"类断言被标注，`persona` 列取值为 `A_突击型考试生` / `B_系统复习者` / `C_课程教师`。
2. **E0 必须无来源**：筛选 `evidence_level=E0` 的行，`source_locator` 应为空；筛选 `source_type=无来源` 的行，`evidence_level` 必须是 `E0`（双向一致）。
3. **循环论证检测生效**：`requirement_persona_map.csv` 中应有至少一条 R09 或 R10 需求被标 `assumption_driven=true`，且 `external_falsifiable_claim` 非空。
4. **人工回填**：`human_verdict=PENDING` 的行必须由人逐条填完 —— 审计脚本只做机器初筛，**不得**自动把 PENDING 当作 TRUE。

> 这一步是整个审计里**最耗时**的部分（预估 1–2 小时/人）。建议做法：先只看 `machine_flag=SUSPECT` 的行（预计远少于 84），其余按 30% 抽查。

---

## 3. 在线对照实验（可选）

```powershell
# 无 Key 情况下：应打印明确提示并以退出码 0 结束
python scripts/audit_online_baseline.py
echo $LASTEXITCODE     # 期望 0（不是 1）
cat reports/audit/online_baseline.skipped.json
```

```powershell
# 有 Key 情况下
$env:QWEN_API_KEY = "<your key>"
python scripts/audit_online_baseline.py
echo $LASTEXITCODE     # 期望 0
```

**逐条验收**

1. **跳过是合法状态**：无 Key 时**不得**出现网络请求、不得报错退出。
2. **三分组成对**：`online_baseline.csv` 的 `group` 列必须同时含 `A_free_generation` 与 `C_graph_constrained`。只有 A 组说明 B/C 分组未生效。
3. **每格 N ≥ 20**：
```powershell
python -c "import pandas as p;d=p.read_csv('reports/audit/online_baseline.csv');print(d.groupby('group').size())"
```
4. **区间用 Wilson**：查看 `verdict.json` 的 `l4.ci_method` 必须是 `'wilson_95'`。
5. **κ 检查**：若 `l4.status == 'skipped'` 且 note 中包含 `rater_agreement_below_threshold`，说明评分者培训不足 —— 需重新培训后重跑，**不得**改口径凑数据。

---

## 4. 回归验证（确保零破坏）

```powershell
python -m pytest tests/ -q
# 期望：145 passed（与 Table 6.1 口径一致）
```

**注意**：审计脚本**不应**被加进 `tests/`。`tests/` 的用例计数是报告（Table 6.1）里的既定事实，往里加文件会让 145 这个数字失效，进而与 `07-ch6-testing-yang-mingjie.md` 冲突。审计脚本放 `scripts/`，用退出码验收（见 `plan.md` 结构决策）。

---

## 5. 拿到结论后怎么用

打开 `reports/audit/verdict.json`，先看 `verdict_level`：

| 等级 | 你现在可以写的句子 | 你还不能写的 |
| :-: | :--- | :--- |
| **V0** | "尚未完成幻觉测量" | 任何"降低" |
| **V1** | "离线确定性路径上 L1/L2/L3 错误率为 x/y/z" | 在线自由生成的幻觉率 |
| **V2** | "相对自由生成基线，约束路径的 L4 点估计由 a 降至 b（CI …）" | 真实学生学习效果 |
| **V3** | —（本规格 Won't，不应出现） | — |

**写作前必读**：[`contracts/report-claim-contract.md`](contracts/report-claim-contract.md) 的第二节禁止互引矩阵。三个必被问到的坑：MMLU≠幻觉、离线≠0%、145 用例≠内容正确。

---

## 6. 常见失败与处理

| 症状 | 原因 | 处理 |
| :--- | :--- | :--- |
| `l1_content_audit.csv` 行数 < 84 | 某题缺 `traps` 或被静默跳过 | 修脚本使其**报错**，不允许跳过 |
| `l4.rate == 0` | 把"无生成面"写成了 0% | 改为 `rate: null, status: na_no_generation_face` |
| `determinism_check.identical == false` | 结果里混入了时间戳/随机顺序 | 哈希只覆盖数据行，不含 `timestamp_utc` |
| 两次运行 diff 出 `git_commit` 变化 | 运行间发生了提交 | 在相同 commit 下重跑 |
| `pytest` 从 145 变成 146 | 把审计脚本放进了 `tests/` | 移出到 `scripts/` |
| 报告正文禁用词命中 | 写作时用了"有效降低幻觉" | 按契约第五节替换 |
