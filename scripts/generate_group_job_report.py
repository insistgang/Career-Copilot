#!/usr/bin/env python3
import json
import re
from pathlib import Path

json_file = Path("docs/wechat_group_recruitment_raw.json")
with open(json_file, "r", encoding="utf-8") as f:
    posts = json.load(f)

print(f"Total posts: {len(posts)}")

parsed_jobs = []

for i, p in enumerate(posts, 1):
    time_str = p.get("time", "")
    p_type = p.get("type", "")
    if p_type == "link":
        title = p.get("title", "")
        source = p.get("source", "")
        url = p.get("url", "")
        desc = p.get("desc", "")
        parsed_jobs.append({
            "id": i,
            "time": time_str,
            "type": "推文链接",
            "company_or_title": title,
            "source": source,
            "url": url,
            "detail": desc,
            "raw": f"{title} | {desc}"
        })
    else:
        content = p.get("content", "").strip()
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        first_line = lines[0] if lines else ""
        
        # Extract email if present
        emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', content)
        phones = re.findall(r'1\d{10}', content)
        
        parsed_jobs.append({
            "id": i,
            "time": time_str,
            "type": "群通知文本",
            "company_or_title": first_line[:40],
            "source": "辅导员通知",
            "url": "",
            "emails": emails,
            "phones": phones,
            "detail": content,
            "raw": content
        })

# Save parsed analysis
output_md = Path("docs/就业信息群_全量岗位汇总与匹配分析.md")
with open(output_md, "w", encoding="utf-8") as f:
    f.write("# 📋 辅导员微信就业信息群 · 全量招聘岗位智能归纳与精准匹配库\n\n")
    f.write("> **数据来源**：上海工程技术大学电子信息专业 2027届微信就业群（辅导员 刘慧老师发布）\n")
    f.write(f"> **采集记录总数**：共 {len(parsed_jobs)} 条招聘通知 / 推文\n\n")
    f.write("---\n\n")
    
    for job in parsed_jobs:
        f.write(f"### [{job['id']:02d}] {job['time']} ｜ {job['company_or_title']}\n")
        f.write(f"- **类型**：{job['type']} ({job['source']})\n")
        if job.get('url'):
            f.write(f"- **网申/推文链接**：[{job['company_or_title']}]({job['url']})\n")
        if job.get('emails'):
            f.write(f"- **投递邮箱**：`{', '.join(job['emails'])}`\n")
        if job.get('phones'):
            f.write(f"- **联系电话**：`{', '.join(job['phones'])}`\n")
        f.write(f"- **详细内容**：\n```text\n{job['detail']}\n```\n\n---\n\n")

print(f"✅ 已全量解析并生成 Markdown 报告: {output_md}")
