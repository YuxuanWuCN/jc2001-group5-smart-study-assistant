# 编辑说明（中文，不属于报告正文）

> 本文件是给你自己看的操作手册。**`draft.md` 是纯英文**，可以直接粘进报告，不含任何中文。

## 1. 本目录文件

| 文件 | 用途 | 状态 |
| :--- | :--- | :--- |
| `outline.md` | G1 骨架（已提交并开 PR #16） | 已交付 |
| `draft.md` | 英文正文初稿，含 Table 5.4/5.5/5.6、Figure 5.2 引用、伪代码、References | **已交付，通过全部自动检查** |
| `sources.md` | 素材清单（每个数字的出处） | 已交付 |
| `group_messages.md` | 三段可直接粘贴的群消息 | 已交付 |
| `EDITOR_NOTES.md` | 本文件 | — |

## 2. draft.md 的自动检查结果

| 检查项 | 要求 | 实测 |
| :--- | :--- | :--- |
| 正文总词数 | 1,800–2,400 | **1,881** ✅ |
| 5.3 词数 | 900–1,200 | **1,181** ✅ |
| 5.4 词数 | 700–900 | **700** ✅ |
| 禁用词（leverage / cutting-edge / state-of-the-art / seamlessly / revolutionise） | 0 | **0** ✅ |
| 正文源码（`def` / `import` / ```python） | 无 | **无** ✅ |
| 中文混入正文 | 0 | **0** ✅ |
| 超过 30 词的单句 | 0 | **0** ✅ |
| emoji | 0 | **0** ✅ |
| 无出处的百分比 | 0 | **0** ✅ |
| Harvard 引用 | ≥4 | **4 条（均经 Crossref 核对）** ✅ |
| 图表编号 | 仅 5.4 / 5.5 / 5.6 / Figure 5.2 | ✅ 未新增任何未分配编号 |

## 3. 需要你本人确认的 3 件事（我无法替你保证）

1. **5.3.3 里的 "checked within the team"** —— 如果你能确认 36 个陷阱确实由第二个人逐条复核过，保留；若没有，改成 "reviewed by the authors against the syllabus"。
2. **Corbett and Anderson 的年份** —— Crossref 记录为 **1995**，学界多引作 1994。本稿按任务包用 1994；提交前请按出版社页面统一，正文与 References 两处必须一致。
3. **Table 5.4 的 Knowledge point 列** —— 我从中文 tag 转写成了英文（因为正文必须英文）。如果你想保留中文原文，请全表统一处理。

## 4. Figure 5.2 怎么插进报告

- 源文件：`reports/figures/fig_trap_causal_chain.mmd`
- 矢量图（**优先用这个**）：`reports/figures/fig_trap_causal_chain.svg` —— 直接拖进 Word，缩放不糊
- 需要 PNG 时：把 `.mmd` 粘到 <https://mermaid.live> 导出 PNG
- 图注已按规范写在正文里（图下方、含 `(Source: …)`）

## 5. 与任务包 06 的 8 处差异（建议同步给吴宇轩）

| # | 任务包 | 实测 |
| :-: | :--- | :--- |
| 1 | `seed_questions.py` 932 行 | **657 行** |
| 2 | `law_1` 的 `radar_hit` = `boundary` | **`trapDefense`** |
| 3 | 5.3.3 举例"子网划分 2^n−2" | 题库无此题型 → 换成 `cs_2 / trap_cs_2_2` |
| 4 | 5.3.3 举例"供需弹性因果倒置" | econ 全是计量经济学 → 换成 `econ_3 / trap_econ_3_1` |
| 5 | 5.3.3 举例"单元测试 vs 集成测试" | 无此题 → 换成 `se_3 / trap_se_3_3` |
| 6 | 5.4.3 读 `report_service.py` / `/api/reports/trend` | 均不存在 → 已按组长裁定改读 `frontend/app.js` |
| 7 | 伪代码 404 / 422 | 实现为 **200 + 优雅兜底**（422 只在 schema 校验失败） |
| 8 | 端点 8 个 | **4 个** |

## 6. 提交方式

```powershell
cd "C:\Users\Dongsiqintony\Documents\deepseek-harness\default-workspace\.piptmp\report-worktree"
git push -u fork report/ch05-dong-siqin
```

推到**同一个分支**后，PR #16 会自动更新，不需要开新 PR。

## 7. 还可以继续做的

- 扩写 5.3.2 的文献论证（如果你想把学术味再加重）
- 把 5.4.2 做成正式的三线表（现在已是标准 markdown 表，Word 里转三线表即可）
- 按你习惯的语气逐段润色（现在偏"工程报告"风格，若要更"学术论文"风格，我可以再调一轮）
