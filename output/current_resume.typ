#import "../templates/resume.typ": resume

#show: resume.with(
  name: "刘钢",
  title: "大模型推理优化 / 边缘 AI 算法工程师",
  phone: "+86 159-9519-7640",
  email: "insistgang@163.com",
  github: "https://github.com/insistgang",
  blog: "https://insistgang.top",
  location: "上海",
  education: (
    (
      school: "上海工程技术大学",
      degree: "硕士 (电子信息 - 人工智能方向)",
      period: "2024.09 - 2027.06",
      gpa: "3.36 / 4.0",
      advisor: "刘翔 教授",
      honors: ("硕士研究生学业一等奖学金", "优秀共产党员 / 党员之星", "三好学生 / 优秀共青团员 / 优秀团干部", "团干部示范典型 / 活力团支部班长/团支书")
    ),
    (
      school: "宿迁学院",
      degree: "学士 (信息与计算科学)",
      period: "2017.09 - 2021.06",
      gpa: "3.23 / 4.0",
      advisor: "",
      honors: ("校级优秀毕业设计", "中共党员 (2021)")
    ),
  ),
  skills: (
    (
      title: "推理优化与端侧部署",
      description: "主攻 LLM INT4 权重量化（Qwen2-7B 显存 14GB 压缩至 5.8GB，单卡 42 tokens/s）、QLoRA 微调、vLLM/TensorRT FP16/INT8 编译导出与 NVIDIA Jetson Orin Nano 边缘端部署调优。"
    ),
    (
      title: "大模型与多模态 (LLM/VLM/Agent)",
      description: "精通 Qwen2 / Qwen2.5-VL 多模态微调、RAG 检索增强架构 (ChromaDB 8万+条目向量检索)、Prompt 工程及 4 层多智能体 (Multi-Agent) 协同架构设计。"
    ),
    (
      title: "计算机视觉与深度学习",
      description: "熟练掌握 YOLO 系列（P2 高分辨率特征金字塔、自适应特征融合 AMSFF、解耦检测头 DCH、YOLO-seg 实例分割）、ReID 消除重复计数、单目测距与 OpenCV 视觉处理。"
    ),
    (
      title: "工程开发与全栈工具链",
      description: "精通 Python 与现代 C/C++；熟练掌握 Linux/Shell 生产开发、FastAPI 高并发异步后端、React 前端开发、SQLite FTS5 全文检索及 Typst 自动化文档编译。"
    ),
  ),
  projects: (
    (
      name: "多智能体协同网络安全威胁智能分析系统",
      role: "大模型研发与全栈架构",
      period: "2025.07 - 2025.10",
      tag: "华为杯网安专项赛 · 国家三等奖 (队长)",
      tags: ("Qwen2-7B", "INT4量化", "QLoRA", "Multi-Agent", "RAG", "ChromaDB"),
      points: (
      "主导开源大模型 Qwen2-7B 的 INT4 权重量化部署，将运行显存由 14GB 压缩至 5.8GB (降低 58.5%)，实现消费级单卡 42 tokens/s 离线推理。",
      "设计 4 层多智能体 (Multi-Agent) 协同研判架构，基于 ChromaDB 毫秒级检索 8 万+ 威胁情报条目，分析准确率提升 12%。",
      )
    ),
    (
      name: "电路系统框图多模态智能识别与逻辑解析系统",
      role: "多模态大模型研发",
      period: "2025.09 - 2025.11",
      tag: "集成电路 EDA 精英赛 · 国家三等奖",
      tags: ("YOLOv8", "Qwen2.5-VL", "LoRA微调", "拓扑理解", "图元识别"),
      points: (
      "提出“YOLOv8 空间几何定位 + Qwen2.5-VL 拓扑语义理解”级联架构，元件定位准确率达 95%+，逻辑推断 F1 达 0.87。",
      "微调专用 LoRA 适配器，实现原理图从图像输入到标准网表 (Netlist) 逆向生成的全流程自动化。",
      )
    ),
    (
      name: "智慧城市井盖状态细粒度检测与遥感违建边缘部署",
      role: "第一作者 / 核心算法设计",
      period: "2024.10 - 至今",
      tag: "硕士核心课题 / 中文核心在投",
      tags: ("YOLOv11", "特征金字塔 P2", "AMSFF", "Jetson Orin Nano", "TensorRT"),
      points: (
      "在 YOLOv11 骨干网络中引入 P2 层高分辨率特征金字塔与自适应多尺度特征融合 (AMSFF)，细粒度状态识别 mAP50 达到 93.2%。",
      "完成 TensorRT FP16/INT8 量化与算子融合，部署至 NVIDIA Jetson Orin Nano 边缘设备，端侧推理吞吐量达 45+ FPS。",
      )
    ),
  ),
  awards: (
    "全国大学生数学建模竞赛【国家二等奖】 (队长)",
    "“华为杯”全国研究生网络安全专项赛【国家三等奖】 (队长)",
    "全国大学生集成电路 EDA 精英创新赛【国家三等奖】",
    "西门子杯智能制造挑战赛【省一等奖】、研电赛【省二/三等奖】、上海市智慧城市大赛【省三等奖】",
  ),
  papers: (
    "《基于 YOLOv11 深度学习的智慧城市井盖细粒度状态检测系统》（中文核心在投，第一作者）",
    "软著《研发费用智能核算与报表自动化 RPA 软件 V1.0》（独立研发）",
  )
)
