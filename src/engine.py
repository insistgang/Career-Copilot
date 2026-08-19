"""
Career-Copilot: Core Engine for Master Profile Ingestion, Tailoring, and Compilation.
"""

import os
import sys
import yaml
import json
import glob
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "master_profile"
TEMPLATES_DIR = PROJECT_ROOT / "templates"
OUTPUT_DIR = PROJECT_ROOT / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class ProfileLoader:
    """Loads and manages the Master Profile Vault (YAML + Markdown Project Cards)."""

    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = data_dir
        self.profile_path = data_dir / "profile.yaml"
        self.projects_dir = data_dir / "projects"
        self.profile_data = self._load_profile()
        self.project_cards = self._load_projects()

    def _load_profile(self) -> Dict[str, Any]:
        if not self.profile_path.exists():
            raise FileNotFoundError(f"profile.yaml not found at {self.profile_path}")
        with open(self.profile_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _load_projects(self) -> List[Dict[str, Any]]:
        projects = []
        for md_file in sorted(self.projects_dir.glob("*.md")):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Simple metadata parse
            lines = content.splitlines()
            title = lines[0].replace("#", "").strip() if lines else md_file.stem
            projects.append({
                "id": md_file.stem,
                "file_path": str(md_file),
                "title": title,
                "raw_content": content
            })
        return projects


class ResumeCompiler:
    """Compiles tailored resume data into single-page PDF using Typst."""

    def __init__(self, output_dir: Path = OUTPUT_DIR):
        self.output_dir = output_dir
        self.template_path = TEMPLATES_DIR / "resume.typ"

    def render_typst(self, tailored_data: Dict[str, Any], output_pdf_name: str = "CV_刘钢.pdf") -> Path:
        """Generates a dynamic .typ file and compiles it to PDF."""
        output_typ_path = self.output_dir / "current_resume.typ"
        output_pdf_path = self.output_dir / output_pdf_name

        typst_content = self._build_typst_document(tailored_data)
        with open(output_typ_path, "w", encoding="utf-8") as f:
            f.write(typst_content)

        # Check if typst is available
        try:
            cmd = ["typst", "compile", "--root", str(PROJECT_ROOT), str(output_typ_path), str(output_pdf_path)]
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ PDF 简历成功生成: {output_pdf_path}")
            return output_pdf_path
        except FileNotFoundError:
            print("⚠️ 未找到 typst 命令，请确保 typst 已安装在系统环境中。")
            return output_typ_path
        except subprocess.CalledProcessError as e:
            print(f"❌ Typst 编译失败:\n{e.stderr}")
            return output_typ_path

    def _build_typst_document(self, data: Dict[str, Any]) -> str:
        b = data["basic_info"]
        doc = f"""#import "../templates/resume.typ": resume

#show: resume.with(
  name: "{b.get('name', '刘钢')}",
  english_name: "{b.get('english_name', '')}",
  title: "{data.get('target_title', b.get('title', 'AI 算法工程师'))}",
  phone: "{b.get('phone', '')}",
  email: "{b.get('email', '')}",
  github: "{b.get('github', '')}",
  blog: "{b.get('blog', '')}",
  location: "{b.get('location', '上海')}",
  education: (
"""
        for edu in data.get("education", []):
            honors_str = ", ".join([f'"{h}"' for h in edu.get("honors", [])])
            doc += f"""    (
      school: "{edu['school']}",
      degree: "{edu['degree']}",
      period: "{edu['period']}",
      gpa: "{edu.get('gpa', '')}",
      advisor: "{edu.get('advisor', '')}",
      thesis: "{edu.get('thesis', '')}",
      honors: ({honors_str})
    ),\n"""
        doc += "  ),\n  skills: (\n"

        for sk_key, sk in data.get("skills", {}).items():
            doc += f"""    (
      title: "{sk['title']}",
      description: "{sk['description']}"
    ),\n"""
        doc += "  ),\n  projects: (\n"

        for p in data.get("selected_projects", []):
            points_str = "\n".join([f'      "{pt}",' for pt in p.get("points", [])])
            tags_str = ", ".join([f'"{t}"' for t in p.get("tags", [])])
            doc += f"""    (
      name: "{p['name']}",
      role: "{p.get('role', '')}",
      period: "{p.get('period', '')}",
      tag: "{p.get('tag', '')}",
      tags: ({tags_str}),
      points: (
{points_str}
      )
    ),\n"""
        doc += "  ),\n  awards: (\n"
        for aw in data.get("awards_summary", []):
            doc += f'    "{aw}",\n'
        doc += "  ),\n  papers: (\n"
        for pp in data.get("papers_summary", []):
            doc += f'    "{pp}",\n'
        doc += "  )\n)\n"
        return doc


class Dispatcher:
    """Invokes agently-mail CLI to dispatch tailored emails."""

    @staticmethod
    def send_email(to: str, subject: str, body: str, attachment_path: Optional[str] = None) -> bool:
        cmd = [
            "agently-cli", "message", "+send",
            "--to", to,
            "--subject", subject,
            "--body", body,
            "--confirmed"
        ]
        if attachment_path and os.path.exists(attachment_path):
            rel_path = os.path.relpath(attachment_path, os.getcwd())
            cmd.extend(["--attachment", rel_path])
        
        try:
            print(f"🚀 正在通过 agently-mail 发送至 {to}...")
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ 发送成功！输出: {res.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ 邮件发送失败: {e.stderr.strip()}")
            return False


class TimingAdvisor:
    """Evaluates the optimal delivery timing for email and job applications based on HR workflows."""

    @staticmethod
    def evaluate_current_timing() -> Dict[str, Any]:
        from datetime import datetime
        now = datetime.now()
        weekday = now.weekday()  # 0: Mon, 1: Tue, ..., 6: Sun
        hour = now.hour
        minute = now.minute
        time_str = now.strftime("%Y-%m-%d %H:%M:%S (星期%w)" if "%w" != "" else "%Y-%m-%d %H:%M:%S")
        weekday_names = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        current_day_name = weekday_names[weekday]

        # S-Grade Golden Windows:
        # Tue-Thu 09:00-10:30, 14:00-15:30
        is_tue_thu = weekday in [1, 2, 3]
        is_morning_s = (hour == 9) or (hour == 10 and minute <= 30)
        is_afternoon_s = (hour == 14) or (hour == 15 and minute <= 30)
        
        # A-Grade Good Windows:
        # Mon 14:00-17:30
        # Tue-Thu 10:30-12:00, 15:30-18:00, 19:30-21:00
        # Fri 09:00-11:30
        is_mon_afternoon = (weekday == 0 and 14 <= hour < 18)
        is_fri_morning = (weekday == 4 and (9 <= hour < 11 or (hour == 11 and minute <= 30)))
        is_midweek_normal = (is_tue_thu and (10 < hour < 12 or 15 < hour < 18 or (19 <= hour <= 20) or (hour == 21 and minute == 0)))

        # D-Grade Bad Windows:
        # Late Night 22:30 - 08:30, Weekends
        is_weekend = weekday in [5, 6]
        is_late_night = (hour >= 22 or hour < 8)

        if (is_tue_thu and (is_morning_s or is_afternoon_s)):
            level = "S级 (🌟 黄金爆发时段)"
            recommendation = "【极力推荐立即投递】当前正处于 HR 打开邮箱置顶处理与集中初筛的高峰期，曝光率最高！"
            is_optimal = True
        elif is_mon_afternoon or is_fri_morning or is_midweek_normal:
            level = "A级 (🟢 良好活跃时段)"
            recommendation = "【推荐投递】当前处于正常工作或晚间直聘活跃期，HR 会在常规工作流中查看。"
            is_optimal = True
        elif is_weekend or is_late_night:
            level = "D级 (🔴 沉底风险时段)"
            recommendation = "【建议稍后或定时发送】当前为周末或深夜，邮件容易被夜间系统消息覆盖。建议在明天上午 09:00 或下午 14:00 发送！"
            is_optimal = False
        else:
            level = "B级 (🟡 普通时段)"
            recommendation = "【可以投递】建议确保邮件标题格式规范以突出重点。"
            is_optimal = True

        return {
            "current_time": f"{now.strftime('%Y-%m-%d %H:%M')} ({current_day_name})",
            "level": level,
            "is_optimal": is_optimal,
            "recommendation": recommendation
        }

