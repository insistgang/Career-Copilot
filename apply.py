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
    
    # 针对性组装高密度、全铺满、强量化单页数据
    tailored_data = {
        "basic_info": loader.profile_data["basic_info"],
        "target_title": "AI 算法工程师 / 边缘智能与大模型推理优化" if args.mode == "industry" else "博士研究生申请人 (计算机视觉与端侧大模型方向)",
        "education": [
            {
                "school": "上海工程技术大学",
                "degree": "电子信息 (人工智能方向 · 硕士)",
                "period": "2024.09 - 2027.06",
                "gpa": "3.36 / 4.0",
                "advisor": "刘翔 教授",
                "thesis": "《面向违法建筑识别的多尺度图像检测方法研究》",
                "honors": ["学业一等奖学金", "优秀共产党员 (党员之星)", "三好学生", "电子信息3班团支书 (活力团支部)"]
            },
            {
                "school": "宿迁学院",
                "degree": "信息与计算科学 (理学学士)",
                "period": "2017.09 - 2021.06",
                "gpa": "3.23 / 4.0",
                "honors": ["校级优秀毕业设计", "中共党员 (2021年入党)"]
            }
        ],
        "skills": {
            "ai_native": {
                "title": "AI-Native 研发与 Agent 生态",
                "description": "深度实践 AI-Native 研发范式，精通 Claude Code、Codex、Google Antigravity (agy)、Grok、MiniMax、GLM 及 Kimi 等前沿 AI Agent 工具链与 MCP 协议；具备极强的多智能体编排与系统级落地能力，独立/主导完成视频多模态检索 (understand_mov_v2)、网络安全研判、行动工作台等多个复杂系统的端到端敏捷交付。"
            },
            "inference": {
                "title": "推理优化与端侧部署",
                "description": "主攻 LLM INT4 权重量化（Qwen2-7B 显存 14GB 压缩至 5.8GB，单卡 42 tokens/s）、QLoRA 微调、vLLM/TensorRT FP16/INT8 算子融合与 NVIDIA Jetson Orin Nano 边缘端部署调优，具备工业级单卡离线推理实战经验。"
            },
            "llm_agent": {
                "title": "大模型与多模态 (LLM/VLM)",
                "description": "精通 Qwen2 / Qwen2.5-VL 多模态微调、RAG 检索增强架构 (ChromaDB 8万+条目向量检索与重排)、Prompt 工程及 4 层多智能体 (Multi-Agent) 协同架构设计。"
            },
            "cv_dl": {
                "title": "计算机视觉与深度学习",
                "description": "精通 PyTorch、YOLOv8/v11（引入 P2 高分辨率金字塔、AMSFF 自适应多尺度融合、DCH 解耦头、YOLO-seg 实例分割）、ReID 目标追踪、单目几何测距与 OpenCV 视觉处理。"
            }
        },
        "selected_projects": [
            {
                "name": "中国电子科技集团第五十研究所 · 道路智能检测与单目测距系统",
                "tag": "央企算法研发实习 · 生产落地",
                "role": "算法研发实习生",
                "period": "2025.10 - 2026.01",
                "tags": ["YOLOv8", "单目几何测距", "ReID防重", "时域平滑", "工业级部署"],
                "points": [
                    "针对细长杆状目标设计长宽比敏感约束与轻量化检测骨干，在自建道路巡检数据集上实现路灯及关键部件检测 mAP50 达到 92%+。",
                    "提出结合相机几何标定与边界框底边的单目测距算法，5~50 米范围内相对误差控制在 5% 以内；引入时域平滑消除车辆行进抖动，已在实际生产环境上线运行。"
                ]
            },
            {
                "name": "多智能体协同网络安全威胁智能分析系统",
                "tag": "“华为杯”全国研究生网安大赛 · 国家三等奖 (队长)",
                "role": "队长 / 大模型研发与架构",
                "period": "2025.07 - 2025.10",
                "tags": ["Qwen2-7B", "INT4量化", "QLoRA", "Multi-Agent", "RAG", "ChromaDB"],
                "points": [
                    "主导 Qwen2-7B 的 INT4 权重量化部署，显存由 14GB 压缩至 5.8GB (降低 58.5%)，单张消费级 GPU 实现 42 tokens/s 离线推理，解决内网安全敏感数据不出域刚需。",
                    "设计 4 层多智能体协同研判架构，基于 ChromaDB 检索 8 万+ MITRE ATT&CK 威胁情报，威胁研判准确率提升 12%，分析耗时从小时级缩减至秒级。"
                ]
            },
            {
                "name": "电路系统框图多模态智能识别与逻辑解析系统",
                "tag": "全国集成电路 EDA 精英创新赛 · 国家三等奖",
                "role": "核心成员 / 多模态模型研发",
                "period": "2025.09 - 2025.11",
                "tags": ["YOLOv8", "Qwen2.5-VL", "LoRA微调", "拓扑理解", "图元识别"],
                "points": [
                    "提出“YOLOv8 空间几何定位 + Qwen2.5-VL 拓扑语义理解”级联架构，元件定位准确率达 95%+，电路逻辑拓扑推断 F1 达到 0.87。",
                    "针对电路图元构建专用图文微调集并训练 LoRA 适配器，实现原理图从图像输入到标准网表 (Netlist) 逆向生成的端到端全流程自动化。"
                ]
            },
            {
                "name": "智慧城市井盖细粒度检测系统与遥感违建边缘部署",
                "tag": "硕士核心课题 / 中文核心在投 (第一作者)",
                "role": "第一作者 / 核心算法设计",
                "period": "2024.10 - 至今",
                "tags": ["YOLOv11", "特征金字塔 P2", "AMSFF", "Jetson Orin Nano", "TensorRT"],
                "points": [
                    "在 YOLOv11 骨干中引入 P2 层高分辨率特征金字塔与自适应多尺度特征融合 (AMSFF)，消除梯度冲突，自建 7 类细粒度井盖识别 mAP50 达到 93.2% (Recall +4.3%)。",
                    "构建 1752 张 RSIB-1K 无人机遥感违建数据集，经 TensorRT INT8 量化部署至 NVIDIA Jetson Orin Nano，端侧推理吞吐量稳定维持在 45+ FPS。"
                ]
            }
        ],
        "awards_summary": [
            "【国家级竞赛】全国大学生数学建模竞赛【国家二等奖】(队长)、“华为杯”中国研究生网络安全创新大赛【国家三等奖】(队长)、“华为杯”中国研究生 AI 创新大赛【国家三等奖】(队长)、集成电路 EDA 精英挑战赛【国家三等奖】",
            "【省部级竞赛】2026 第二十届研电赛【省级二等奖】(LinkAble)、2026 西门子杯智能制造挑战赛【省级二等奖】(答辩82分)、2025 西门子杯【省级一等奖】、第十九届研电赛【省级三等奖】、上海市研究生智慧城市大赛【省级三等奖】、上海市大学生行业分析大赛【银奖/省二】"
        ],
        "papers_summary": [
            "【学术论文与软著】《基于 YOLOv11 深度学习的智慧城市井盖细粒度状态检测系统》（中文核心在投，第一作者）、软著《研发费用智能核算与报表自动化 RPA 软件 V1.0》（登记完成，独立开发）"
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
