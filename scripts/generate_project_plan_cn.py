#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JC2001 软件工程 - Group 5 项目规划书 (Project Plan / Project Proposal) 中文正式版生成器
专供吴宇轩队长交付给 10 位组员审阅与工程对齐
"""

import os
import sys
from pathlib import Path

import docx
from docx.enum.section import WD_SECTION_START
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Mm, Pt, RGBColor

# 控制台 UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 经典深蓝商务学术配色
COLOR_NAVY = (0x1B, 0x36, 0x5D)        # #1B365D -  oxford navy
COLOR_BLUE = (0x1E, 0x3A, 0x8A)        # #1E3A8A - primary blue
COLOR_TEXT = (0x1F, 0x29, 0x37)        # #1F2937 - dark body
COLOR_MUTED = (0x4B, 0x55, 0x63)       # #4B5563 - gray
COLOR_EMERALD = (0x05, 0x96, 0x69)     # #059669 - success green
COLOR_AMBER = (0xD9, 0x77, 0x06)       # #D97706 - warning amber

HEX_NAVY = "1B365D"
HEX_ALT = "F8FAFC"
HEX_BORDER = "CBD5E1"


def set_run_font(run, name="微软雅黑", size_pt=10.0, bold=False, italic=False, color_rgb=COLOR_TEXT):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color_rgb:
        run.font.color.rgb = RGBColor(*color_rgb)
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:eastAsia"), name)
    rFonts.set(qn("w:cs"), name)


def apply_table_style(table, col_widths=None, hdr_bg=HEX_NAVY, alt_bg=HEX_ALT):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = table._tbl.tblPr

    borders = parse_xml(f"""
        <w:tblBorders {nsdecls('w')}>
            <w:top w:val="single" w:sz="8" w:space="0" w:color="{hdr_bg}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="{hdr_bg}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    """)
    tblPr.append(borders)

    cell_mar = parse_xml(f"""
        <w:tblCellMar {nsdecls('w')}>
            <w:top w:w="90" w:type="dxa"/>
            <w:bottom w:w="90" w:type="dxa"/>
            <w:left w:w="120" w:type="dxa"/>
            <w:right w:w="120" w:type="dxa"/>
        </w:tblCellMar>
    """)
    tblPr.append(cell_mar)

    hdr_row = table.rows[0]
    trPr = hdr_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

    for cell in hdr_row.cells:
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hdr_bg}"/>')
        cell._tc.get_or_add_tcPr().append(shd)
        for p in cell.paragraphs:
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            for r in p.runs:
                set_run_font(r, name="微软雅黑", size_pt=9.0, bold=True, color_rgb=(0xFF, 0xFF, 0xFF))

    for idx, row in enumerate(table.rows[1:], start=1):
        bg = alt_bg if idx % 2 == 0 else "FFFFFF"
        r_trPr = row._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if bg != "FFFFFF":
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg}"/>')
                cell._tc.get_or_add_tcPr().append(shd)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(1.5)
                p.paragraph_format.space_after = Pt(1.5)
                p.paragraph_format.line_spacing = 1.15
                for r in p.runs:
                    set_run_font(r, name="微软雅黑", size_pt=8.5, color_rgb=COLOR_TEXT)

    if col_widths:
        for row in table.rows:
            for c_idx, w in enumerate(col_widths):
                if c_idx < len(row.cells):
                    row.cells[c_idx].width = Inches(w)


def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="微软雅黑", size_pt=13.0, bold=True, color_rgb=COLOR_NAVY)


def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, name="微软雅黑", size_pt=11.0, bold=True, color_rgb=COLOR_BLUE)


def add_bullet(doc, text, bold_prefix=""):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.2)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1.5)
    p.paragraph_format.line_spacing = 1.2
    r_dot = p.add_run("• ")
    set_run_font(r_dot, name="微软雅黑", size_pt=9.0, bold=True, color_rgb=COLOR_NAVY)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        set_run_font(r_pre, name="微软雅黑", size_pt=9.0, bold=True, color_rgb=COLOR_NAVY)
    r_txt = p.add_run(text)
    set_run_font(r_txt, name="微软雅黑", size_pt=9.0)


def add_p(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.line_spacing = 1.22
    r = p.add_run(text)
    set_run_font(r, name="微软雅黑", size_pt=9.0)


def add_callout(doc, text, border_color=HEX_NAVY, bg_color="F8FAFC"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

    borders = parse_xml(f"""
        <w:tcBorders {nsdecls('w')}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    """)
    cell._tc.get_or_add_tcPr().append(borders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.18
    r = p.add_run(text)
    set_run_font(r, name="微软雅黑", size_pt=9.0, color_rgb=COLOR_NAVY)


def generate_project_plan_docx(docx_path: str):
    doc = docx.Document()

    # A4 页面与页边距
    s = doc.sections[0]
    s.page_width = Mm(210)
    s.page_height = Mm(297)
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

    # 页眉页脚
    hdr = s.header
    hp = hdr.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("JC2001 软件工程 — Group 5 (BSc BMIS) | 项目规划书 (Project Proposal)")
    set_run_font(hrun, name="微软雅黑", size_pt=8.5, italic=True, color_rgb=COLOR_MUTED)

    ftr = s.footer
    fp = ftr.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun1 = fp.add_run("第 ")
    set_run_font(frun1, name="微软雅黑", size_pt=8.5, color_rgb=COLOR_MUTED)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    fp._p.append(fld)
    frun2 = fp.add_run(" 页  |  智能大学生备考与知识诊断辅导系统 (Smart Study Assistant)")
    set_run_font(frun2, name="微软雅黑", size_pt=8.5, color_rgb=COLOR_MUTED)

    # 封面标题
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(3)
    r_sub = p_title.add_run("JC2001 软件工程导论 (2026–27 学年)\n")
    set_run_font(r_sub, name="微软雅黑", size_pt=14.0, bold=True, color_rgb=COLOR_BLUE)
    r_main = p_title.add_run("【软件工程项目规划书 (Project Proposal)】")
    set_run_font(r_main, name="微软雅黑", size_pt=18.0, bold=True, color_rgb=COLOR_NAVY)

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_proj.paragraph_format.space_before = Pt(4)
    p_proj.paragraph_format.space_after = Pt(12)
    r_proj = p_proj.add_run("项目名称：基于知识图谱与大模型的智能备考诊断辅导系统\n"
                            "Smart Study Assistant System: A GraphRAG & Knowledge Graph Diagnostic Approach")
    set_run_font(r_proj, name="微软雅黑", size_pt=10.0, italic=True, color_rgb=COLOR_MUTED)

    # 团队信息表
    team_tbl = doc.add_table(rows=11, cols=4)
    team_tbl.rows[0].cells[0].paragraphs[0].add_run("序号")
    team_tbl.rows[0].cells[1].paragraphs[0].add_run("姓名")
    team_tbl.rows[0].cells[2].paragraphs[0].add_run("学号")
    team_tbl.rows[0].cells[3].paragraphs[0].add_run("专业与项目身份")

    members = [
        ("1", "吴宇轩", "50106070", "BSc (BMIS) | 组长兼项目联系人 (Team Leader)"),
        ("2", "林泳桐", "50106038", "BSc (BMIS) | 联合课题奠基人 (Principal Concept Co-Originator)"),
        ("3", "王思鉴", "50106045", "BSc (BMIS) | 团队成员 (Team Member)"),
        ("4", "江昊", "50106065", "BSc (BMIS) | 团队成员 (Team Member)"),
        ("5", "谢炜昕", "50106034", "BSc (BMIS) | 联合课题奠基人 (Principal Concept Co-Originator)"),
        ("6", "张梓健", "50106035", "BSc (BMIS) | 团队成员 (Team Member)"),
        ("7", "习羽赛", "50105989", "BSc (BMIS) | 团队成员 (Team Member)"),
        ("8", "董思钦", "50106060", "BSc (BMIS) | 团队成员 (Team Member)"),
        ("9", "杨明杰", "50106061", "BSc (BMIS) | 团队成员 (Team Member)"),
        ("10", "梁子铉", "50106037", "BSc (BMIS) | 团队成员 (Team Member)"),
    ]
    for r_idx, row in enumerate(members, start=1):
        for c_idx, val in enumerate(row):
            team_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_style(team_tbl, col_widths=[0.6, 1.2, 1.2, 3.5])

    # 1. 项目立项背景与问题定义
    add_h1(doc, "一、 项目背景与问题定义 (Problem Statement)")
    add_p(doc, "在高校本科学习中，大学生普遍面对多门难度高、跨度大的专业课程（如计算机、经管、金融、法学等）。在期末备考与平时的知识巩固过程中，学生面临着严重的效率瓶颈与认知负担：")
    add_bullet(doc, "课件 PPT、教材章节与练习册各自独立成块，缺乏清晰的知识依赖关系图，导致学生容易陷入'盲人摸象'的混乱复习状态。", bold_prefix="1. 知识点碎片化与认知超载：")
    add_bullet(doc, "学生刷历年真题或练习题时，往往只能查看'对'或'错'，无法知道自己究竟掉进了出题老师设下的哪个逻辑陷阱，缺乏针对根源弱项的排查。", bold_prefix="2. 盲目刷题但易错点不明确：")
    add_bullet(doc, "现有商用大模型在直接问答时，倾向于直接给出最终完整答案。学生被动抄袭答案，不仅剥夺了独立思考过程，而且难以培养深层解题思维。", bold_prefix="3. 现有 AI 辅导缺乏诊断与启发式引导：")
    add_bullet(doc, "通用大模型在专业学术领域存在严重的'知识幻觉'与乱回答现象。面对大学高阶数理推导、定理前置条件和专业术语时，极易产生看似言之成理、实则虚构错误的解答。学生若轻信错误推导，不仅无法提分，反而会强化错误认知，造成严重的学业误导。", bold_prefix="4. 学术领域严重的知识幻觉与乱回答痛点：")

    # 2. 技术解决方案
    add_h1(doc, "二、 解决方案与核心技术架构 (Proposed Solution)")
    add_p(doc, "本项目提出并实现【智能大学生备考与知识诊断辅导系统 (Smart Study Assistant System)】，以现有知识图谱与检索增强生成（GraphRAG）为核心，将传统平面的被动问答升级为结构化的智能诊断导学。")
    add_bullet(doc, "在 Neo4j 中建立学科本体模型，定义四类核心节点：【核心考点】、【定理条件】、【易错漏洞】与【计算操作】。首创【易错于 (DEPENDS_ON)】关系连边，精准记录易混淆概念与易忽略边界条件。", bold_prefix="1. Neo4j 错题图谱建模：")
    add_bullet(doc, "对接阿里云通义千问大模型（DashScope Qwen-Turbo），对历年真题进行逆向考点反推与易错逻辑陷阱自动提取，实现自动化建图与考点知识沉淀。", bold_prefix="2. 自动化试卷诊断抽取：")
    add_bullet(doc, "AI 助教在答疑时严禁直接吐出完整答案，而是根据图谱中的易错节点逐步抛出启发式问题，引导学生自己发现思维漏洞（苏格拉底导学机制）。", bold_prefix="3. 启发式苏格拉底导学：")
    add_bullet(doc, "测验系统自动关联薄弱图谱节点，并在前端利用 ECharts 5.5.1 生成学生的五维能力雷达图（基础概念、边界推演、排雷防守、综合运用、计算精度），直观展现复习短板。", bold_prefix="4. 自适应测验与五维能力雷达图：")
    add_bullet(doc, "将生成式问答严格锚定 (Grounding) 于验证过的 Neo4j 知识拓扑中，并结合高置信度仲裁门禁 (>=85%)，有效过滤生成噪声与虚假连边，从机理上大幅降低了 AI 在学术专业领域的知识幻觉率。", bold_prefix="5. 图谱事实锚定与显著降低知识幻觉率：")

    add_callout(
        doc,
        "💡 【现有技术验证基础与数据佐证】\n"
        "本项目已具备坚实的技术原型（本地 graphrag 代码库已跑通 Neo4j 连通与 Qwen 诊断抽取）：\n"
        "• 在多学科真实测试集中，结合图谱排雷诊断相较于通用大模型基准：在专业法学测试中准确率提升 +2.50%，在计算机学科测试中提升 +2.00%！\n"
        "• 针对'学术界大模型乱回答与知识幻觉严重'的行业痛点，系统通过 Neo4j 权威学科本体事实锚定与高置信度仲裁门禁 (Confidence Threshold >= 85%)，有效拦截噪声，显著降低了知识幻觉率。",
        border_color="059669",
        bg_color="ECFDF5"
    )

    # 3. SMART 目标
    add_h1(doc, "三、 项目目标 (Project Objectives - SMART 原则)")
    add_p(doc, "本软件工程项目严格对照 JC2001 课程标准，制定了在 2026 年 12 月 14 日前达成的五大 SMART 目标：")
    add_bullet(doc, "在 2026 年 12 月 14 日前，设计、开发并交付一个功能完备、包含 Neo4j 云数据库、Qwen 诊断 API、苏格拉底导学与前端可视化界面的 PoC 软件运行包。", bold_prefix="目标 1 (功能交付)：")
    add_bullet(doc, "构建涵盖至少 250 个核心考点、500 道多学科真题、300 条易错依赖关系的知识图谱，双向 Cypher 图遍历查询响应延迟严格控制在 2.0 秒内。", bold_prefix="目标 2 (图谱规模与性能)：")
    add_bullet(doc, "真题考点与陷阱抽取准确率达到 85% 以上；通过图谱事实锚定与高置信度仲裁门禁 (>=85%) 过滤 85% 以上噪声连边，显著抑制学术乱回答，切实降低知识幻觉率。", bold_prefix="目标 3 (诊断精度与降低知识幻觉率)：")
    add_bullet(doc, "遵循模块化面向对象软件工程标准，核心 Cypher 查询接口单元测试覆盖率达 100%，关键业务逻辑 pytest 分支覆盖率 >= 80%，代码遵循 PEP 8 规范。", bold_prefix="目标 4 (工程质量与测试)：")
    add_bullet(doc, "在 12 月 14 日 23:59 CST 前，全量提交 40–60 页正式技术报告、8–12 页用户使用手册、15 分钟 MP4 答辩展示视频与全员签名的个人工作量表。", bold_prefix="目标 5 (文档与课程验收)：")

    # 4. 项目收益
    add_h1(doc, "四、 项目价值与预期收益 (Expected Benefits)")
    add_bullet(doc, "帮助学生建立立体的考点拓扑网络，摆脱盲目背题，预计可节省 30–40% 的复习时间；雷达图可视化让薄弱点无处遁形。", bold_prefix="对学生 (主要用户)：")
    add_bullet(doc, "通过后台聚合的学生错题图谱热力数据，任课教师与助教可直观洞察整个班级在哪些前置考点上存在群体性认知盲区，从而开展针对性答疑。", bold_prefix="对教师与助教：")
    add_bullet(doc, "沉淀一套可跨学年复用的数字课程知识资产，助力高校课程数字化与教学智能化建设。", bold_prefix="对学院与学科：")

    # 5. 时间进度规划
    add_h1(doc, "五、 项目时间规划与里程碑路线图 (Timeline & Roadmaps)")
    add_p(doc, "项目周期严格对应 2026–27 学年第一学期的 12 周全生命周期（2026年9月14日 至 2026年12月14日），划分为四个连续递进的工程阶段：")

    time_tbl = doc.add_table(rows=5, cols=4)
    time_tbl.rows[0].cells[0].paragraphs[0].add_run("工程阶段")
    time_tbl.rows[0].cells[1].paragraphs[0].add_run("核心任务内容")
    time_tbl.rows[0].cells[2].paragraphs[0].add_run("关键交付物")
    time_tbl.rows[0].cells[3].paragraphs[0].add_run("截止完成时间")

    time_data = [
        ("Phase 1: 需求捕获与开题", "团队分工组建、痛点调研、用户故事定义、与导师首期会议沟通", "开题报告 (Project Proposal PDF)", "2026年9月25日"),
        ("Phase 2: 架构设计与建模", "Neo4j Schema 确立、UML 类图/时序图/用例图建模、原型线框图", "架构设计基线与 Project Update 1", "2026年10月31日"),
        ("Phase 3: PoC 开发与验证", "图谱接口开发、Qwen API 诊断对接、刷题引擎实现、单元测试", "软件代码冻结与 Project Update 2/3", "2026年11月30日"),
        ("Phase 4: 终审交付与答辩", "技术报告撰写、8-12页用户手册、15分钟视频录制与最终总装打包", "技术报告 + 软件包 + 视频答辩", "2026年12月14日"),
    ]
    for r_idx, row in enumerate(time_data, start=1):
        for c_idx, val in enumerate(row):
            time_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_style(time_tbl, col_widths=[1.5, 2.2, 1.8, 1.0])

    add_callout(
        doc,
        "📌 【重要提交节点速记】\n"
        "• 9月25日 (第2周周五)：MyAberdeen 提交正式 Project Proposal PDF（由队长吴宇轩提交）。\n"
        "• 10月23日：提交 Project Update 1（架构设计）。\n"
        "• 11月06日：提交 Project Update 2（中间进展）。\n"
        "• 11月25日：提交 Project Update 3（原型代码与测试）。\n"
        "• 12月14日 (第12周周一)：提交最终技术报告 (50%) + 软件代码与手册 (30%) + 答辩视频 (20%)。",
        border_color="1E3A8A",
        bg_color="F1F5F9"
    )

    # 6. 项目工程模块与研发任务清单
    doc.add_page_break()
    add_h1(doc, "六、 项目工程模块与研发任务清单 (Work Breakdown Structure)")
    add_p(doc, "围绕系统实现与课程验收标准，项目整体划分为 13 项具体的工程研发与文档交付任务，全组后续按工程模块统筹推进：")

    wbs_tbl = doc.add_table(rows=14, cols=4)
    wbs_tbl.rows[0].cells[0].paragraphs[0].add_run("任务编号")
    wbs_tbl.rows[0].cells[1].paragraphs[0].add_run("具体工程任务与核心输出")
    wbs_tbl.rows[0].cells[2].paragraphs[0].add_run("所属系统模块")
    wbs_tbl.rows[0].cells[3].paragraphs[0].add_run("交付周期与状态")

    wbs_data = [
        ("WBS 1.1", "用户需求调研、备考痛点捕获与需求规格说明书整理", "需求分析模块", "Phase 1 (已完成)"),
        ("WBS 1.2", "开题报告整体统筹、格式排版校验与 MyAberdeen 提交", "开题管理模块", "Phase 1 (进行中)"),
        ("WBS 2.1", "Neo4j 图数据库知识图谱 Schema 与'易错于'关系本体设计", "数据图谱模块", "Phase 2 (进行中)"),
        ("WBS 2.2", "系统 UML 架构建模（类图、时序图、用例图、包图）", "系统架构模块", "Phase 2 (待启动)"),
        ("WBS 3.1", "Qwen-Turbo 大模型考点与错题陷阱自动抽取引擎开发", "后端算法模块", "Phase 3 (待启动)"),
        ("WBS 3.2", "GraphRAG 检索流水线与启发式苏格拉底导学助教内核开发", "导学助教模块", "Phase 3 (待启动)"),
        ("WBS 3.3", "自适应诊断刷题前端与 ECharts 5.5.1 五维能力雷达图开发", "前端交互模块", "Phase 3 (待启动)"),
        ("WBS 3.4", "Pytest 单元测试集构建、Cypher 模拟测试与异常退避处理", "测试质保模块", "Phase 3 (待启动)"),
        ("WBS 4.1", "多学科真题考卷测试与学术仲裁抗噪过滤门禁调优", "算法评测模块", "Phase 4 (待启动)"),
        ("WBS 4.2", "正式技术报告撰写 (40–60页)、UML模型集成与查重控制", "核心文档模块", "Phase 4 (待启动)"),
        ("WBS 4.3", "用户手册编撰 (8–12页) 与 PoC 可运行软件包一键部署脚本", "部署手册模块", "Phase 4 (待启动)"),
        ("WBS 4.4", "15 分钟高清答辩视频录制、剪辑与全套展示 PPT 排版制作", "答辩展示模块", "Phase 4 (待启动)"),
        ("WBS 4.5", "期末全套三联交付物质量门禁终审与 MyAberdeen 最终上传", "总装验收模块", "Phase 4 (待启动)"),
    ]
    for r_idx, row in enumerate(wbs_data, start=1):
        for c_idx, val in enumerate(row):
            wbs_tbl.rows[r_idx].cells[c_idx].paragraphs[0].add_run(val)
    apply_table_style(wbs_tbl, col_widths=[0.9, 3.2, 1.2, 1.2])

    # 7. 风险管理与应对预案
    doc.add_page_break()
    add_h1(doc, "七、 项目风险管理与应对预案 (Risk Management)")
    add_bullet(doc, "Neo4j AuraDB 免费版存在 20 万节点上限与内存限制。应对对策：实施知识节点高度规范化去重，严格设置缓存与索引，测试期本地轻量部署备份。", bold_prefix="1. 数据库配额风险：")
    add_bullet(doc, "阿里云 DashScope 存在并发限流 (HTTP 429)。应对对策：代码层实现指数退避重试算法 (Exponential Backoff with Jitter)，并在本地建立真题缓存池。", bold_prefix="2. 大模型 API 限流风险：")
    add_bullet(doc, "第 7–8 周各学科期中考可能分散精力。应对对策：将 Phase 2 架构基线提前至 10 月 20 日冻结，预留 10 天弹性冲刺缓冲期。", bold_prefix="3. 团队成员精力冲突风险：")
    add_bullet(doc, "技术报告严禁粘贴代码且须通过 Turnitin 查重。应对对策：由专人严格把控，正文只展示算法拓扑、UML 模型与架构图，文本连续引用严禁超 3 句话。", bold_prefix="4. 学术诚信与查重风险：")

    # 8. 组员核对指引
    add_h1(doc, "八、 组员审阅重点与核对清单 (Review Checklist)")
    add_p(doc, "各位组员在审阅本规划书时，请重点对照并确认以下关键内容：")
    add_bullet(doc, "请核对本规划书首页名单中的姓名与学号是否准确无误。", bold_prefix="1. 个人姓名学号核对：")
    add_bullet(doc, "充分了解我们系统的核心特色（Neo4j 错题图谱 + Qwen 考点反推 + 苏格拉底导学助教 + 五维能力雷达图）。", bold_prefix="2. 项目方案共识：")
    add_bullet(doc, "明确 JC2001 课程的五大交付板块（开题报告、阶段汇报、40–60 页技术报告、PoC 软件包+8–12 页用户手册、15 分钟答辩视频）及评分红线。", bold_prefix="3. 课程规范知晓：")
    add_bullet(doc, "全组审阅确认后，队长将在 9 月 25 日前正式上传英文版 Proposal 至 MyAberdeen；后续各研发模块由全组在组会中共同商讨自主认领推进！", bold_prefix="4. 协作推进机制：")

    add_p(doc, "\n----------------------------------------------------------------------\n"
               "JC2001 Group 5 项目团队（华南师范大学阿伯丁学院，2026年9月）全员持存。")

    doc.save(docx_path)
    print(f"[OK] 生成项目规划书 DOCX 成功: {docx_path}")


def export_pdf(docx_path: str, pdf_path: str):
    import win32com.client
    abs_docx = str(Path(docx_path).resolve())
    abs_pdf = str(Path(pdf_path).resolve())
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        wdoc = word.Documents.Open(abs_docx)
        wdoc.SaveAs(abs_pdf, FileFormat=17)
        wdoc.Close()
        print(f"[OK] 导出项目规划书 PDF 成功: {pdf_path}")
    finally:
        word.Quit()


def main():
    docx_out = "reports/JC2001_Group5_项目规划书.docx"
    pdf_out = "reports/JC2001_Group5_项目规划书.pdf"

    generate_project_plan_docx(docx_out)
    export_pdf(docx_out, pdf_out)

    import pymupdf
    doc = pymupdf.open(pdf_out)
    print(f"[VERIFY] 项目规划书 PDF 页数: {len(doc)} 页, 尺寸: {doc[0].rect}")


if __name__ == "__main__":
    main()
