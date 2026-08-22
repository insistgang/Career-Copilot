#!/usr/bin/env python3
"""
Career-Copilot: Generate specialized resumes for WeChat group companies:
1. 上海芯圣电子 (AI 系统开发 / VibeCoding 实习生)
2. 南凌科技 (SASE / SD-WAN 测试开发实习生)
3. 上海航天八院 (武器装备现场调试 / 嵌入式软件)
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
# 1. 上海芯圣电子 - AI 系统开发 / VibeCoding 实习生
# ==========================================
data_holychip = {
    "basic_info": basic_info,
    "target_title": "AI 系统开发工程师 / VibeCoding & 大模型全栈",
    "education": common_education,
    "skills": {
        "vibecoding": {
            "title": "AI-Native 与 VibeCoding 工具链",
            "description": "深度精通 Claude Code、Codex、Google Antigravity (agy)、Grok、MiniMax、GLM、Kimi 等现代 AI 原生工具链与 MCP 协议，具备极强的代码自迭代与端到端系统秒级原型交付能力。"
        },
        "llm_agent": {
            "title": "大模型量化微调与 Multi-Agent 架构",
            "description": "主攻 Qwen2-7B 的 INT4 权重量化部署（显存 14G 压至 5.8G，单卡 42 tokens/s）与 QLoRA 微调；精通 4 层 Multi-Agent 状态路由与 RAG 向量知识库检索增强。"
        },
        "fullstack": {
            "title": "全栈工程交付与高并发后端",
            "description": "精通 Python、FastAPI 异步高并发后端、Celery 异步调度、SQLite/PostgreSQL 与 React 18 / Vite / Ant Design 前端看板构建，具备独立架构生产级 AI SaaS 平台实力。"
        },
        "embedded_cv": {
            "title": "工业视觉与嵌入式端侧部署",
            "description": "掌握 YOLO 系列模型改进与工业落地，具备央企中国电科 50 所生产交付经验及 NVIDIA Jetson Orin Nano / TensorRT 边缘端优化能力（45+ FPS 实时推理）。"
        }
    },
    "selected_projects": [
        {
            "name": "多智能体协同网络安全威胁智能分析系统",
            "tag": "“华为杯”全国研究生网安大赛 · 国家三等奖 (队长)",
            "role": "队长 / 大模型与 Multi-Agent 架构",
            "period": "2025.07 - 2025.10",
            "tags": ["Multi-Agent", "LangChain", "ChromaDB", "Qwen2-7B", "INT4量化", "RAG"],
            "points": [
                "设计 4 层 Multi-Agent（解析/检索/因果推理/报告生成）协同研判架构，基于 ChromaDB 检索 8 万+ 威胁情报，研判准确率提升 12%。",
                "主导 Qwen2-7B 的 INT4 极限量化部署，显存由 14GB 压缩至 5.8GB (降低 58.5%)，单张消费级 GPU 实现 42 tokens/s 离线推理。"
            ]
        },
        {
            "name": "K12 个性化自适应学习与智能辅导系统",
            "tag": "“华为杯”中国研究生 AI 创新大赛 · 国家三等奖 (队长)",
            "role": "队长 / 架构与大模型研发",
            "period": "2025.07 - 2025.09",
            "tags": ["React 18", "Vite", "FastAPI", "知识图谱", "自适应推荐", "智能批改"],
            "points": [
                "主导研发基于大语言模型的自适应 K12 智能辅导平台，构建细粒度知识图谱，实现对话式答疑、错题归因与作文智能批改。",
                "设计基于学情画像与艾宾浩斯曲线的自适应出题引擎；基于 React 18 + Ant Design 构建看板，端到端延迟 < 800ms，获全国三等奖。"
            ]
        },
        {
            "name": "understand_mov_v2 多模态视频内容智能检索平台",
            "tag": "多模态 AI 全栈平台 · 独立研发",
            "role": "独立全栈架构与开发",
            "period": "2025.08 - 2025.10",
            "tags": ["FastAPI", "React", "CLIP多模态", "SQLite FTS5", "向量检索", "RESTful API"],
            "points": [
                "基于 FastAPI + React 独立架构高并发视频智能检索系统，集成 CLIP 视觉特征提取与文本跨模态匹配，实现毫秒级以文搜图/视频定位。",
                "构建 SQLite FTS5 高性能全文索引与结构化元数据缓存机制，打造兼顾轻量化部署与极速响应的企业级 AI SaaS 原型平台。"
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
        }
    ],
    "awards_summary": common_awards,
    "papers_summary": common_papers
}

# ==========================================
# 2. 南凌科技 - SASE / SD-WAN 测试开发实习生
# ==========================================
data_nova = {
    "basic_info": basic_info,
    "target_title": "测试开发工程师 / 网络安全与自动化开发",
    "education": common_education,
    "skills": {
        "python_automation": {
            "title": "Python 自动化开发与系统测试",
            "description": "精通 Python 脚本开发、自动化测试框架构建与接口测试；精通 Linux 操作系统网络配置、Shell 脚本编写及 CI/CD 自动化流水线搭建。"
        },
        "network_security": {
            "title": "网络安全协议与 Multi-Agent 研判",
            "description": "精通 TCP/IP 协议族与网络安全攻防，曾作为队长带队获“华为杯”网安大赛全国三等奖；精通 4 层 Multi-Agent 网络威胁自动化研判与日志分析系统架构。"
        },
        "backend_arch": {
            "title": "高并发后端与数据存储",
            "description": "精通 FastAPI 异步高性能后端开发、Celery 分布式任务调度；熟悉 ChromaDB 向量数据库、PostgreSQL 与 SQLite 数据管理与性能调优。"
        },
        "ai_tooling": {
            "title": "AI 赋能测试与敏捷交付",
            "description": "熟练运用 Claude Code、Codex、agy 等现代 AI 编程与测试工具，具备在复杂网络与安全业务场景下快速编写自动化用例、定位故障与排障的能力。"
        }
    },
    "selected_projects": [
        {
            "name": "多智能体协同网络安全威胁智能分析系统",
            "tag": "“华为杯”全国研究生网安大赛 · 国家三等奖 (队长)",
            "role": "队长 / 架构与后端开发",
            "period": "2025.07 - 2025.10",
            "tags": ["Multi-Agent", "网络安全协议", "ChromaDB", "Python自动化", "Qwen2-7B"],
            "points": [
                "设计 4 层 Multi-Agent（解析/检索/因果推理/报告生成）协同研判架构，基于 ChromaDB 检索 8 万+ MITRE ATT&CK 威胁情报，研判准确率提升 12%。",
                "主导 Qwen2-7B 的 INT4 极限量化部署，单张消费级 GPU 实现 42 tokens/s 离线推理，将安全事件研判耗时从小时级缩减至秒级。"
            ]
        },
        {
            "name": "understand_mov_v2 多模态视频内容智能检索平台",
            "tag": "高并发全栈系统 · 独立架构",
            "role": "独立全栈架构与开发",
            "period": "2025.08 - 2025.10",
            "tags": ["FastAPI", "自动化测试", "SQLite FTS5", "RESTful API", "React"],
            "points": [
                "基于 FastAPI + React 独立架构高并发智能检索平台，设计完整的 RESTful API 规范与自动化单元测试，保障系统高吞吐与高可用。",
                "构建 SQLite FTS5 全文索引与元数据多级缓存，经过压力测试在高并发读写下仍保持毫秒级极速响应。"
            ]
        },
        {
            "name": "中国电子科技集团第五十研究所 · 道路智能检测系统",
            "tag": "央企算法研发实习 · 生产落地",
            "role": "算法研发实习生",
            "period": "2025.10 - 2026.01",
            "tags": ["Python", "YOLOv8", "时域平滑滤波", "工业级交付"],
            "points": [
                "针对细长目标设计长宽比敏感约束检测骨干，自建数据集上路灯及部件检测 mAP50 达到 92%+；",
                "引入卡尔曼时域平滑滤波与 ReID 轨迹防重机制，编写自动化验证脚本，算法已在实际生产环境上线稳定运行。"
            ]
        },
        {
            "name": "企业双碳创新平台与 ESG 评价智能决策系统",
            "tag": "双碳创新赛 · 能源碳金融算法",
            "role": "算法与全栈负责人",
            "period": "2025.03 - 2025.06",
            "tags": ["Python数据分析", "时序预测", "FastAPI", "ESG量化"],
            "points": [
                "基于碳排放因子数据库构建多维度企业碳足迹计算模型，实现范围一二三排放自动化测算与动态追踪。",
                "开发多层指标加权的 ESG 智能量化评价算法与绿色金融产品推荐模型，输出综合能耗诊断报告。"
            ]
        }
    ],
    "awards_summary": common_awards,
    "papers_summary": common_papers
}

# ==========================================
# 3. 上海航天八院 - 武器装备现场调试 / 嵌入式软件
# ==========================================
data_hangtian = {
    "basic_info": basic_info,
    "target_title": "现场调试工程师 / 嵌入式软件与智能算法研发",
    "education": common_education,
    "skills": {
        "field_engineering": {
            "title": "现场工程调试与严苛环境交付",
            "description": "具备央企研究所（中国电科 50 所）实地工业环境算法交付经验，熟悉现场装备安装调试、故障排查与技术文档编写；能吃苦抗压，适应出差攻坚。"
        },
        "embedded_cpp": {
            "title": "嵌入式系统与 C/C++ 软件开发",
            "description": "精通 C/C++ 与 Python 编程，熟练掌握常用总线通信协议（CAN、UART、SPI、Modbus、Profinet）；精通 NVIDIA Jetson Orin Nano 嵌入式端侧部署与 TensorRT 加速。"
        },
        "cv_control": {
            "title": "智能检测与控制算法",
            "description": "深入掌握 YOLO 系列视觉检测改进、单目几何标定测距与时域平滑滤波算法；曾获西门子杯中国智能制造挑战赛省级一等奖及二等奖。"
        },
        "leadership": {
            "title": "党员先锋与多项国奖带队能力",
            "description": "中共党员、研究生团支书、校“党员之星”；作为队长带队斩获全国数学建模国二、网安国三、AI创新大赛国三等 4 项国家级及 6 项省部级奖项，纪律性与组织协调能力极强。"
        }
    },
    "selected_projects": [
        {
            "name": "中国电子科技集团第五十研究所 · 道路智能检测与单目测距系统",
            "tag": "央企算法研发实习 · 工业生产落地",
            "role": "算法研发实习生",
            "period": "2025.10 - 2026.01",
            "tags": ["YOLOv8", "单目几何测距", "ReID防重", "时域平滑", "工业级交付"],
            "points": [
                "针对细长杆状目标设计长宽比敏感约束检测骨干，在自建道路巡检数据集上实现路灯及部件检测 mAP50 达到 92%+。",
                "提出结合相机几何标定与边界框底边的单目测距算法，5~50 米范围内相对误差控制在 5% 以内；引入时域平滑消除车辆行进抖动，已在实际生产环境上线运行。"
            ]
        },
        {
            "name": "多智能体协同网络安全威胁智能分析系统",
            "tag": "“华为杯”全国研究生网安大赛 · 国家三等奖 (队长)",
            "role": "队长 / 架构与大模型研发",
            "period": "2025.07 - 2025.10",
            "tags": ["Qwen2-7B", "INT4量化", "Multi-Agent", "RAG", "ChromaDB"],
            "points": [
                "主导 Qwen2-7B 的 INT4 权重量化部署，显存由 14GB 压缩至 5.8GB (降低 58.5%)，单张消费级 GPU 实现 42 tokens/s 离线推理，解决内网敏感数据不出域刚需。",
                "设计 4 层多智能体协同研判架构，基于 ChromaDB 检索 8 万+ 威胁情报，威胁研判准确率提升 12%。"
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
            "name": "Jetson Orin Nano 边缘端智能推理与轻量化部署",
            "tag": "边缘计算与端侧推理 · 核心研发",
            "role": "算法部署负责人",
            "period": "2025.04 - 2025.07",
            "tags": ["Jetson Orin Nano", "TensorRT INT8", "CUDA", "边缘计算", "实时推理"],
            "points": [
                "基于 NVIDIA Jetson Orin Nano 搭建边缘端低功耗推理环境，通过 TensorRT INT8 对视觉骨干网络进行权重量化与算子融合。",
                "利用统一内存零拷贝与 CUDA Stream 异步流水线调优，端侧推理帧率由 18 FPS 提升至 45+ FPS，满足高实时严苛工业要求。"
            ]
        }
    ],
    "awards_summary": common_awards,
    "papers_summary": common_papers
}

compiler = ResumeCompiler()

print("🚀 正在编译【上海芯圣电子 - AI 系统开发】定制简历...")
pdf_holychip = compiler.render_typst(data_holychip, output_pdf_name="电子信息_刘钢_上海芯圣电子_AI系统开发.pdf")

print("🚀 正在编译【南凌科技 - 测试开发工程师】定制简历...")
pdf_nova = compiler.render_typst(data_nova, output_pdf_name="电子信息_刘钢_南凌科技_测试开发.pdf")

print("🚀 正在编译【上海航天八院 - 现场调试与嵌入式】定制简历...")
pdf_hangtian = compiler.render_typst(data_hangtian, output_pdf_name="电子信息_刘钢_航天八院_现场调试与软件.pdf")

print("✅ 全部 3 份群内推定制简历编译完成！")
