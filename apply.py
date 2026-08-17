#!/usr/bin/env python3
"""
Career-Copilot: Unified CLI & Agent Entry Point
Usage:
  python3 apply.py --mode industry --jd "招聘岗位JD文本..." --email hr@company.com
  python3 apply.py --mode academic --advisor "导师姓名与方向..." --email prof@univ.edu.cn
"""

import sys
import argparse
from pathlib import Path
from src.engine import ProfileLoader, ResumeCompiler, Dispatcher

def main():
    parser = argparse.ArgumentParser(description="Career-Copilot: AI 职位匹配与简历智能代发系统")
    parser.add_argument("--mode", choices=["industry", "academic"], default="industry", help="投递模式：industry (企业招聘) / academic (申博套磁)")
    parser.add_argument("--jd", type=str, help="岗位 JD 文本或导师简介")
    parser.add_argument("--email", type=str, help="目标收件人邮箱")
    parser.add_argument("--send", action="store_true", help="是否直接触发代发（需人工确认）")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🎯 Career-Copilot 智能投递与对齐引擎启动")
    print(f"📌 当前运行模式: {'🏢 企业招聘模式 (Industry)' if args.mode == 'industry' else '🎓 学术申博模式 (Academic)'}")
    print("=" * 60)

    loader = ProfileLoader()
    print(f"✅ 成功加载经历主库: {loader.profile_data['basic_info']['name']} ({len(loader.project_cards)} 个核心项目)")
    
    # 示例自适应组装数据（默认全集或针对性提取）
    tailored_data = {
        "basic_info": loader.profile_data["basic_info"],
        "target_title": "大模型推理优化 / 边缘 AI 算法工程师" if args.mode == "industry" else "博士申请人 (计算机视觉与边缘智能方向)",
        "education": loader.profile_data["education"],
        "skills": loader.profile_data["skills"],
        "selected_projects": [
            {
                "name": "多智能体协同网络安全威胁智能分析系统",
                "tag": "华为杯网安专项赛 · 国家三等奖 (队长)",
                "role": "大模型研发与全栈架构",
                "period": "2025.07 - 2025.10",
                "tags": ["Qwen2-7B", "INT4量化", "QLoRA", "Multi-Agent", "RAG", "ChromaDB"],
                "points": [
                    "主导开源大模型 Qwen2-7B 的 INT4 权重量化部署，将运行显存由 14GB 压缩至 5.8GB (降低 58.5%)，实现消费级单卡 42 tokens/s 离线推理。",
                    "设计 4 层多智能体 (Multi-Agent) 协同研判架构，基于 ChromaDB 毫秒级检索 8 万+ 威胁情报条目，分析准确率提升 12%。"
                ]
            },
            {
                "name": "电路系统框图多模态智能识别与逻辑解析系统",
                "tag": "集成电路 EDA 精英赛 · 国家三等奖",
                "role": "多模态大模型研发",
                "period": "2025.09 - 2025.11",
                "tags": ["YOLOv8", "Qwen2.5-VL", "LoRA微调", "拓扑理解", "图元识别"],
                "points": [
                    "提出“YOLOv8 空间几何定位 + Qwen2.5-VL 拓扑语义理解”级联架构，元件定位准确率达 95%+，逻辑推断 F1 达 0.87。",
                    "微调专用 LoRA 适配器，实现原理图从图像输入到标准网表 (Netlist) 逆向生成的全流程自动化。"
                ]
            },
            {
                "name": "智慧城市井盖状态细粒度检测与遥感违建边缘部署",
                "tag": "硕士核心课题 / 中文核心在投",
                "role": "第一作者 / 核心算法设计",
                "period": "2024.10 - 至今",
                "tags": ["YOLOv11", "特征金字塔 P2", "AMSFF", "Jetson Orin Nano", "TensorRT"],
                "points": [
                    "在 YOLOv11 骨干网络中引入 P2 层高分辨率特征金字塔与自适应多尺度特征融合 (AMSFF)，细粒度状态识别 mAP50 达到 93.2%。",
                    "完成 TensorRT FP16/INT8 量化与算子融合，部署至 NVIDIA Jetson Orin Nano 边缘设备，端侧推理吞吐量达 45+ FPS。"
                ]
            }
        ],
        "awards_summary": [
            "全国大学生数学建模竞赛【国家二等奖】 (队长)",
            "“华为杯”全国研究生网络安全专项赛【国家三等奖】 (队长)",
            "全国大学生集成电路 EDA 精英创新赛【国家三等奖】、华为杯 AI 创新大赛【国家三等奖】",
            "2026 第二十届研电赛【省级二等奖】(LinkAble)、2026 西门子杯智能制造挑战赛【省级二等奖】",
            "2025 西门子杯【省级一等奖】、第十九届研电赛【省级三等奖】、上海市智慧城市大赛【省级三等奖】"
        ],
        "papers_summary": [
            "《基于 YOLOv11 深度学习的智慧城市井盖细粒度状态检测系统》（中文核心在投，第一作者）",
            "软著《研发费用智能核算与报表自动化 RPA 软件 V1.0》（独立研发）"
        ]
    }

    compiler = ResumeCompiler()
    pdf_path = compiler.render_typst(tailored_data, output_pdf_name="刘钢_个人简历_CareerCopilot.pdf")
    print(f"📄 渲染结果就绪: {pdf_path}")

    if args.email and args.send:
        subject = "【求职申请】刘钢 - AI 算法工程师 / 边缘智能与大模型推理优化" if args.mode == "industry" else "【博士申请】刘钢 - 申请2027年博士研究生"
        body = f"尊敬的老师/HR：\n\n您好！我是上海工程技术大学硕士研究生刘钢。附件是我针对贵团队方向量身定制的个人简历，期待与您进一步交流！\n\n刘钢\n15995197640"
        
        print("\n" + "-" * 50)
        print("📨 待发送邮件草稿预览:")
        print(f"收件人: {args.email}")
        print(f"标  题: {subject}")
        print(f"附  件: {pdf_path}")
        print("-" * 50)
        
        confirm = input("⚠️ 是否确认发送？(y/n): ").strip().lower()
        if confirm == 'y':
            Dispatcher.send_email(to=args.email, subject=subject, body=body, attachment_path=str(pdf_path))
        else:
            print("🛑 用户取消发送。")

if __name__ == "__main__":
    main()
