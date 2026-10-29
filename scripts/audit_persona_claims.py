#!/usr/bin/env python3
"""
Persona Claims Provenance & Requirement Mapping Audit Harness
Part of Speckit 004: Persona-Hallucination-Audit
"""

import csv
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AUDIT_DIR = REPO_ROOT / "reports" / "audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)


PERSONA_CLAIMS = [
    {
        "claim_id": "PA-01",
        "persona": "A_突击型考试生",
        "claim_text": "大二/大三，4 门考试集中在 2 周",
        "claim_kind": "身份",
        "source_type": "文献",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:78",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "依据公开文献/教学场景说明，该群体常见",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PA-02",
        "persona": "A_突击型考试生",
        "claim_text": "Quizlet 卡片、同学错题本、群里的答案汇总",
        "claim_kind": "当前工具",
        "source_type": "竞品行为",
        "source_locator": "reports/competitor_analysis.md:32",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "竞品提供该功能，暗示需求存在",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PA-03",
        "persona": "A_突击型考试生",
        "claim_text": "错了不知道为什么错，没时间深究（二元反馈陷阱）",
        "claim_kind": "痛点",
        "source_type": "文献",
        "source_locator": "VanLehn 2011; Hattie & Timperley 2007",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "依据细粒度反馈文献，该痛点在备考中广泛存在",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PA-04",
        "persona": "A_突击型考试生",
        "claim_text": "5 分钟内知道该补哪一块",
        "claim_kind": "期待",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md:37",
        "evidence_level": "E2",
        "is_core": True,
        "allowed_usage": "在组内 n=10 讨论中成员表示期待快速诊断（非代表性样本）",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PA-05",
        "persona": "A_突击型考试生",
        "claim_text": "主要目标用户",
        "claim_kind": "是否目标用户",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_master_plan.md:100",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "依据 Lean Scoping 决策确定为主目标用户",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PB-01",
        "persona": "B_系统复习者",
        "claim_text": "研究生，长期系统性复习",
        "claim_kind": "身份",
        "source_type": "文献",
        "source_locator": "Corbett & Anderson 1994 (BKT)",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "依据学术文献与研究生备考模式",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PB-02",
        "persona": "B_系统复习者",
        "claim_text": "Anki、笔记软件、论文",
        "claim_kind": "当前工具",
        "source_type": "竞品行为",
        "source_locator": "reports/competitor_analysis.md:45",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "竞品观察表明系统备考者偏好间隔记忆工具",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PB-03",
        "persona": "B_系统复习者",
        "claim_text": "知道自己弱，但看不出弱在哪个能力维度",
        "claim_kind": "痛点",
        "source_type": "文献",
        "source_locator": "Koedinger et al. 2012 (前置知识框架)",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "依据认知科学多维能力评估模型",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PB-04",
        "persona": "B_系统复习者",
        "claim_text": "看到能力维度的长期趋势",
        "claim_kind": "期待",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_task_packs/02-ch2-requirements-moscow-zhang-zijian.md:37",
        "evidence_level": "E2",
        "is_core": True,
        "allowed_usage": "组内讨论形成的学情追踪期待",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PB-05",
        "persona": "B_系统复习者",
        "claim_text": "主要目标用户",
        "claim_kind": "是否目标用户",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_master_plan.md:100",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "定位于长期备考目标用户",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PC-01",
        "persona": "C_课程教师",
        "claim_text": "本课程讲师 / 助教",
        "claim_kind": "身份",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:78",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "课程背景利益相关者",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PC-02",
        "persona": "C_课程教师",
        "claim_text": "学习平台后台、Excel",
        "claim_kind": "当前工具",
        "source_type": "竞品行为",
        "source_locator": "reports/competitor_analysis.md:60",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "常见高校教师管理工具",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PC-03",
        "persona": "C_课程教师",
        "claim_text": "无法在批改之外看到学生的具体误区分布",
        "claim_kind": "痛点",
        "source_type": "文献",
        "source_locator": "Hattie & Timperley 2007",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "文献指出的班级共性诊断盲区",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PC-04",
        "persona": "C_课程教师",
        "claim_text": "（不直接使用）",
        "claim_kind": "期待",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:81",
        "evidence_level": "E1",
        "is_core": False,
        "allowed_usage": "不直接操作系统",
        "auditor": "审计团队"
    },
    {
        "claim_id": "PC-05",
        "persona": "C_课程教师",
        "claim_text": "明确为非目标用户",
        "claim_kind": "是否目标用户",
        "source_type": "组内讨论",
        "source_locator": "reports/cycle3_task_packs/01-ch1-introduction-lin-yongtong.md:84",
        "evidence_level": "E1",
        "is_core": True,
        "allowed_usage": "明确排除出 MVP 目标用户范围（Lean Scoping）",
        "auditor": "审计团队"
    }
]


REQUIREMENT_MAPPINGS = [
    {
        "requirement_id": "R01",
        "requirement_text": "按学科浏览题目列表并加载对应选项与陷阱标签",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-01, PB-01",
        "assumption_driven": False,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R02",
        "requirement_text": "提交作答并记录正误状态",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-03, PB-03",
        "assumption_driven": False,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R03",
        "requirement_text": "选项级陷阱诊断抽屉（误区命名/错因解释/前置盲区/雷达归因）",
        "moscow": "Must",
        "served_personas": "A",
        "served_pain_points": "PA-03",
        "assumption_driven": True,
        "hallucination_layers": "L1, L2, L3",
        "external_falsifiable_claim": "若学生只拿到对错二元反馈，其重复同类概念错误的概率显著高于拿到选项级归因的学生",
        "gap_reason": ""
    },
    {
        "requirement_id": "R04",
        "requirement_text": "五维雷达能力趋势展示（按答题结果实时更新能力分值）",
        "moscow": "Must",
        "served_personas": "B",
        "served_pain_points": "PB-03, PB-04",
        "assumption_driven": True,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "多维雷达图能够有效揭示单项总分掩盖的局部定理认知短板",
        "gap_reason": ""
    },
    {
        "requirement_id": "R05",
        "requirement_text": "学情卡与薄弱知识点摘要（作答次数/掌握率/核心易错前置点）",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-04, PB-04",
        "assumption_driven": False,
        "hallucination_layers": "L1",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R06",
        "requirement_text": "学号免密/密码登录与会话隔离（含预设 demo 账号快速切换）",
        "moscow": "Must",
        "served_personas": "A, B",
        "served_pain_points": "PA-01, PB-01",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R07",
        "requirement_text": "界面中英双语国际化切换",
        "moscow": "Should",
        "served_personas": "A, B",
        "served_pain_points": "PA-01",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R08",
        "requirement_text": "深色控制台与浅色学术双主题（符合 WCAG AA 对比度）",
        "moscow": "Should",
        "served_personas": "A, B",
        "served_pain_points": "PA-01",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": ""
    },
    {
        "requirement_id": "R09",
        "requirement_text": "完全离线、零外部云依赖单端口运行（StaticFiles 挂载与本地字典）",
        "moscow": "Must",
        "served_personas": "A",
        "served_pain_points": "PA-01",
        "assumption_driven": True,
        "hallucination_layers": "L4",
        "external_falsifiable_claim": "在离线确定性查表条件下，系统在消除网络波动的同时间接消除了自由生成面的推理幻觉",
        "gap_reason": ""
    },
    {
        "requirement_id": "R10",
        "requirement_text": "GraphRAG 离线准确率增强与基准验证",
        "moscow": "Should",
        "served_personas": "B",
        "served_pain_points": "PB-03",
        "assumption_driven": True,
        "hallucination_layers": "L4",
        "external_falsifiable_claim": "在概念与法条密集学科中，先验图谱能够提供结构化约束以提高检索准确度",
        "gap_reason": ""
    },
    {
        "requirement_id": "R11",
        "requirement_text": "多租户与教师端班级监控大屏",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "非核心学生闭环，超出12周零预算团队容量，已主动剪枝"
    },
    {
        "requirement_id": "R12",
        "requirement_text": "移动端原生 App 开发（iOS / Android）",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "Web 端已支持移动视口响应式，原生 App 维护成本高"
    },
    {
        "requirement_id": "R13",
        "requirement_text": "社交化错题分享与讨论社区",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "容易引入内容审核与隐私风险，背离独立沉浸复习场景"
    },
    {
        "requirement_id": "R14",
        "requirement_text": "AI 自动实时无限出题组卷",
        "moscow": "Won't",
        "served_personas": "",
        "served_pain_points": "",
        "assumption_driven": False,
        "hallucination_layers": "",
        "external_falsifiable_claim": "",
        "gap_reason": "缺乏专家审核机制时极易引发高频幻觉，威胁备考严肃性"
    }
]


def main():
    provenance_file = AUDIT_DIR / "persona_provenance.csv"
    with open(provenance_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(PERSONA_CLAIMS[0].keys()))
        writer.writeheader()
        writer.writerows(PERSONA_CLAIMS)

    req_map_file = AUDIT_DIR / "requirement_persona_map.csv"
    with open(req_map_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(REQUIREMENT_MAPPINGS[0].keys()))
        writer.writeheader()
        writer.writerows(REQUIREMENT_MAPPINGS)

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"[OK] Persona Provenance: {len(PERSONA_CLAIMS)} claims -> {provenance_file}")
    print(f"[OK] Requirement-Persona Mapping: {len(REQUIREMENT_MAPPINGS)} items -> {req_map_file}")


if __name__ == "__main__":
    main()
