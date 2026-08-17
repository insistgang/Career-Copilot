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
            "--body", body
        ]
        if attachment_path and os.path.exists(attachment_path):
            cmd.extend(["--attach", str(attachment_path)])
        
        try:
            print(f"🚀 正在通过 agently-mail 发送至 {to}...")
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"✅ 发送成功！输出: {res.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ 邮件发送失败: {e.stderr.strip()}")
            return False
