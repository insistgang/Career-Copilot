#!/usr/bin/env python3
"""
Career-Copilot: Generate specialized resumes for 为恒智能, 振石控股, and 施耐德电气 (Schneider Electric).
"""

import os
import subprocess
from pathlib import Path
from src.engine import ProfileLoader, ResumeCompiler

PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

loader = ProfileLoader()
basic_info = loader.profile_data["basic_info"]

common_education = [
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
        "school": "扬州大学广陵学院",
        "degree": "信息与计算科学 (理学学士)",
        "period": "2017.09 - 2021.06",
        "gpa": "3.23 / 4.0",
        "honors": ["校级优秀毕业设计", "中共党员 (2021年入党)"]
    }
]

common_awards = [
    "【国家级竞赛】全国大学生数学建模竞赛【国家二等奖】(队长)、“华为杯”中国研究生网络安全创新大赛【国家三等奖】(队长)、“华为杯”中国研究生 AI 创新大赛【国家三等奖】(队长)、集成电路 EDA 精英挑战赛【国家三等奖】",
    "【省部级竞赛】2025 西门子杯中国智能制造挑战赛【省级一等奖】、2026 第二十届西门子杯【省级二等奖】(答辩82分)、第二十届研电赛【省级二等奖】(LinkAble)、第十九届研电赛【省级三等奖】、上海市智慧城市大赛【省级三等奖】"
]

common_papers = [
    "【硕士核心论文 (在研)】《面向无人机航拍的高分辨率违章建筑小目标检测与边缘部署研究》（第一作者，论文撰写与投稿中）",
    "【国家计算机软件著作权】《研发费用智能核算与报表自动化 RPA 软件 V1.0》（登记完成，独立开发）"
]

# ==========================================
# 1. 施耐德电气 (Schneider Electric) - AI 应用顾问 / 算法工程师 (2027 新星计划)
# ==========================================
data_schneider = {
    "basic_info": basic_info,
    "target_title": "AI 应用顾问 / 算法与前置部署工程师 (FDE) / 能源与工业智能",
    "education": common_education,
    "skills": {
        "energy_automation": {
            "title": "工业智能与能源双碳算法",
            "description": "深入理解能源数字化与绿色低碳转型业务；主导企业双碳碳足迹核算、ESG 量化评价模型及工业能耗时序预测算法研发，曾获西门子杯中国智能制造挑战赛省级一等奖与二等奖。"
        },
        "llm_agent": {
            "title": "大模型应用 (LLM) 与 Multi-Agent 架构",
            "description": "精通 4 层多智能体 (Multi-Agent) 协同架构设计、LangChain/AutoGen 范式、Qwen2-7B INT4 权重量化部署（显存 14G 压至 5.8G，单卡 42 tokens/s）与 RAG 向量检索增强。"
        },
        "industrial_cv": {
            "title": "工业视觉与嵌入式边缘端部署",
            "description": "精通 YOLO 系列算法优化与工业级落地，具备央企（中国电科 50 所）生产环境交付经验，熟练掌握 TensorRT INT8 优化与 NVIDIA Jetson Orin Nano 边缘端部署（45+ FPS 实时吞吐）。"
        },
        "fde_consulting": {
            "title": "AI-Native 敏捷交付与技术咨询 (FDE)",
            "description": "精通 Python/C++、FastAPI 异步后端与 React 看板；深度应用 Claude Code、Codex、agy 等 Agent 工具链，具备面向工业客户复杂场景从 0 到 1 敏捷落地 MVP 的技术咨询与交付能力。"
        }
    },
    "selected_projects": [
        {
            "name": "企业双碳创新平台与 ESG 评价智能决策系统",
            "tag": "能源碳金融算法 · 绿色低碳决策",
            "role": "算法与全栈负责人",
            "period": "2025.03 - 2025.06",
            "tags": ["碳足迹核算", "ESG量化评价", "能源时序预测", "工业能耗分析", "FastAPI"],
            "points": [
                "基于国内外碳排放因子数据库构建多维度企业碳足迹计算模型，实现范围一、二、三温室气体排放的自动化测算与动态追踪。",
                "开发多层指标加权的 ESG 智能量化评价算法与绿色金融产品推荐模型，输出可视化综合能耗诊断报告，为企业节能减排提供辅助决策。"
            ]
        },
        {
            "name": "中国电子科技集团第五十研究所 · 道路智能检测与单目测距系统",
            "tag": "央企算法研发实习 · 工业生产落地",
            "role": "算法研发实习生",
            "period": "2025.10 - 2026.01",
            "tags": ["YOLOv8", "单目几何测距", "ReID防重", "时域平滑", "工业级交付"],
            "points": [
                "针对细长杆状目标设计长宽比敏感约束与轻量化检测骨干，在自建道路巡检数据集上实现路灯及关键部件检测 mAP50 达到 92%+。",
                "提出结合相机几何标定与边界框底边的单目测距算法，5~50 米范围内相对误差控制在 5% 以内；引入时域平滑消除车辆行进抖动，已在实际生产环境上线运行。"
            ]
        },
        {
            "name": "多智能体协同网络安全威胁智能分析系统",
            "tag": "“华为杯”全国研究生网安大赛 · 国家三等奖 (队长)",
            "role": "队长 / 大模型与 Multi-Agent 架构",
            "period": "2025.07 - 2025.10",
            "tags": ["Multi-Agent", "LangChain范式", "ChromaDB", "RAG", "Qwen2-7B", "INT4量化"],
            "points": [
                "设计并实现 4 层 Multi-Agent（解析/检索/因果推理/报告生成）协同研判架构，基于 ChromaDB 检索 8 万+ 威胁情报，威胁研判准确率提升 12%。",
                "主导 Qwen2-7B 的 INT4 极限量化部署，显存由 14GB 压缩至 5.8GB (降低 58.5%)，单张消费级 GPU 实现 42 tokens/s 离线推理，解决安全敏感数据不出域刚需。"
            ]
        },
        {
            "name": "电路系统框图多模态智能识别与逻辑解析系统",
            "tag": "全国集成电路 EDA 精英创新赛 · 国家三等奖",
            "role": "核心成员 / 多模态模型研发",
            "period": "2025.09 - 2025.11",
            "tags": ["YOLOv8", "Qwen2.5-VL", "LoRA微调", "拓扑理解", "电气图元识别"],
            "points": [
                "提出“YOLOv8 空间几何定位 + Qwen2.5-VL 拓扑语义理解”级联架构，元件定位准确率达 95%+，电路逻辑拓扑推断 F1 达到 0.87。",
                "针对电路图元构建专用图文微调集并训练 LoRA 适配器，实现原理图从图像输入到标准网表 (Netlist) 逆向生成的端到端全流程自动化。"
            ]
        }
    ],
    "awards_summary": common_awards,
    "papers_summary": common_papers
}

# ==========================================
# 2. 为恒智能 (ViHon) - AI Agent 工程师
# ==========================================
data_vihon = {
    "basic_info": basic_info,
    "target_title": "AI Agent 工程师 / 大模型应用开发与智能体架构",
    "education": common_education,
    "skills": {
        "agent_arch": {
            "title": "Multi-Agent 协同与 Agent 框架",
            "description": "熟练掌握 4 层多智能体 (Multi-Agent) 协同架构设计、LangChain/AutoGen 范式、Tool-Calling 工具调用协议、状态路由与复杂业务工作流编排，具备从 0 到 1 落地工业级 Agent 系统的实战经验。"
        },
        "llm_rag": {
            "title": "大模型应用 (LLM/VLM) 与 RAG 检索增强",
            "description": "精通 Qwen2 / Claude / GPT 等主流大模型 API 接入与 Prompt 调优；精通 RAG 检索增强架构 (ChromaDB 向量检索、混合检索与 Cross-Encoder 重排)，具备极强的大模型与业务系统集成能力。"
        },
        "energy_carbon": {
            "title": "储能双碳算法与大数据决策",
            "description": "具备企业双碳碳足迹核算、ESG 评价决策模型、绿色金融智能推荐与金融时间序列预测系统研发经验，深度理解能源数字化与虚拟电厂业务逻辑。"
        },
        "fullstack_eng": {
            "title": "全栈工程交付与 AI-Native 工具链",
            "description": "精通 Python、FastAPI 异步高并发后端、Celery 任务调度、PostgreSQL/SQLite 数据库与 React 18 前端可视化看板；深度使用 Claude Code、Codex、agy 等工具实现端到端敏捷交付。"
        }
    },
    "selected_projects": [
        {
            "name": "多智能体协同网络安全威胁智能分析系统",
            "tag": "“华为杯”全国研究生网安大赛 · 国家三等奖 (队长)",
            "role": "队长 / 大模型与 Multi-Agent 架构",
            "period": "2025.07 - 2025.10",
            "tags": ["Multi-Agent", "LangChain范式", "ChromaDB", "RAG", "Qwen2-7B", "INT4量化"],
            "points": [
                "设计并实现 4 层 Multi-Agent（解析/检索/因果推理/报告生成）协同研判架构，基于 ChromaDB 毫秒级检索 8 万+ 威胁情报，研判准确率提升 12%。",
                "主导 Qwen2-7B 的 INT4 极限量化部署，显存由 14GB 压至 5.8GB (降低 58.5%)，单张消费级 GPU 达 42 tokens/s 离线推理，实现敏感数据不出域闭环。"
            ]
        },
        {
            "name": "企业双碳创新平台与 ESG 评价智能决策系统",
            "tag": "双碳创新赛 · 能源碳金融算法",
            "role": "算法与全栈负责人",
            "period": "2025.03 - 2025.06",
            "tags": ["碳足迹模型", "ESG量化评价", "时间序列预测", "能源数据分析", "FastAPI"],
            "points": [
                "基于国内外碳排放因子数据库构建多维度企业碳足迹计算模型，实现范围一、二、三温室气体排放的自动化测算与动态追踪。",
                "开发多层指标加权的 ESG 智能量化评价算法与绿色金融产品推荐模型，输出可视化综合能耗诊断报告，为企业节能减排提供辅助决策。"
            ]
        },
        {
            "name": "K12 个性化自适应学习与智能辅导系统",
            "tag": "“华为杯”中国研究生 AI 创新大赛 · 国家三等奖 (队长)",
            "role": "队长 / 架构与大模型研发",
            "period": "2025.07 - 2025.09",
            "tags": ["React 18", "Vite", "Ant Design", "FastAPI", "知识图谱", "自适应推荐"],
            "points": [
                "主导研发基于大语言模型的自适应 K12 智能辅导平台，构建细粒度知识图谱，实现对话式答疑、错题因果归因与作文多维智能批改。",
                "设计基于学情画像与艾宾浩斯遗忘曲线的自适应出题引擎；基于 React 18 + Ant Design 构建数据看板，端到端延迟 < 800ms，荣获全国三等奖。"
            ]
        },
        {
            "name": "understand_mov_v2 多模态视频内容智能检索平台",
            "tag": "多模态 AI 全栈平台 · 独立研发",
            "role": "独立全栈架构与开发",
            "period": "2025.08 - 2025.10",
            "tags": ["FastAPI", "React", "CLIP多模态", "SQLite FTS5", "向量检索", "RESTful API"],
            "points": [
                "基于 FastAPI + React 独立架构高并发视频智能检索系统，集成 CLIP 视觉特征提取与文本多模态跨模态匹配，实现毫秒级以文搜图/视频定位。",
                "构建 SQLite FTS5 高性能全文索引与结构化元数据缓存机制，打造兼顾轻量化部署与极速响应的企业级 AI SaaS 原型平台。"
            ]
        }
    ],
    "awards_summary": common_awards,
    "papers_summary": common_papers
}

# ==========================================
# 3. 振石控股集团 (Zhenshi) - 智能体研发工程师
# ==========================================
data_zhenshi = {
    "basic_info": basic_info,
    "target_title": "智能体研发工程师 / AI 应用模型开发工程师",
    "education": common_education,
    "skills": {
        "llm_inference": {
            "title": "大模型量化微调与推理加速",
            "description": "深入理解 Transformer 架构与注意力机制；主攻 Qwen2-7B 的 INT4 极限量化部署（显存 14G 压至 5.8G，单卡 42 tokens/s）、QLoRA 微调、vLLM PagedAttention 与 TensorRT 算子融合加速。"
        },
        "cv_small_model": {
            "title": "计算机视觉与轻量化小模型",
            "description": "精通 YOLOv8/v11 结构改进（P2 高分辨率金字塔、AMSFF 自适应融合、解耦头）、ReID 消除重复计数、单目几何测距与 OpenCV 图像处理，具备工业复杂背景下的视觉算法落地能力。"
        },
        "edge_deployment": {
            "title": "边缘端与嵌入式智能部署",
            "description": "精通 NVIDIA Jetson Orin Nano 边缘端部署与 TensorRT INT8 优化，利用统一内存零拷贝与 CUDA Stream 异步流水线调优，实现 45+ FPS 实时低延迟推理。"
        },
        "agent_engineering": {
            "title": "智能体编排与 AI-Native 交付",
            "description": "精通 Python 与 C++，掌握 LangChain/AutoGen 多智能体协同范式；熟练使用 Claude Code、Codex、agy 等前沿工具链，具备传统工业制造场景下快速交付生产级系统的工程实力。"
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
            "name": "K12 个性化自适应学习与智能辅导系统",
            "tag": "“华为杯”中国研究生 AI 创新大赛 · 国家三等奖 (队长)",
            "role": "队长 / 架构与大模型研发",
            "period": "2025.07 - 2025.09",
            "tags": ["React 18", "Vite", "Ant Design", "FastAPI", "知识图谱", "自适应推荐", "智能批改"],
            "points": [
                "主导研发基于大语言模型的自适应 K12 智能辅导平台，构建语文学科细粒度知识图谱，实现对话式答疑、错题因果归因与作文多维智能批改。",
                "设计基于学情画像与艾宾浩斯遗忘曲线的自适应出题引擎；基于 React 18 + Ant Design 构建数据看板，端到端延迟 < 800ms，荣获全国三等奖。"
            ]
        }
    ],
    "awards_summary": common_awards,
    "papers_summary": common_papers
}

compiler = ResumeCompiler()

print("🚀 正在编译【施耐德电气 - AI 应用顾问/算法工程师】定制简历...")
pdf_schneider = compiler.render_typst(data_schneider, output_pdf_name="刘钢_个人简历_施耐德电气_AI应用顾问.pdf")

print("🚀 正在编译【为恒智能 - AI Agent 工程师】定制简历...")
pdf_vihon = compiler.render_typst(data_vihon, output_pdf_name="刘钢_个人简历_为恒智能_AIAgent.pdf")

print("🚀 正在编译【振石控股 - 智能体研发工程师】定制简历...")
pdf_zhenshi = compiler.render_typst(data_zhenshi, output_pdf_name="刘钢_个人简历_振石控股_智能体研发.pdf")

print("✅ 全部定制单页 PDF 简历生成完毕！")
