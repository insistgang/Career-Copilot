#!/usr/bin/env python3
import json
from pathlib import Path

json_file = Path("docs/wechat_group_recruitment_raw.json")
with open(json_file, "r", encoding="utf-8") as f:
    posts = json.load(f)

print(f"Total posts: {len(posts)}")
for i, p in enumerate(posts[:55], 1):
    time_str = p.get("time", "")
    p_type = p.get("type", "")
    if p_type == "link":
        title = p.get("title", "")
        source = p.get("source", "")
        url = p.get("url", "")
        print(f"[{i:02d}] {time_str} | 🔗 LINK: {title} ({source})")
        print(f"     URL: {url}")
    else:
        content = p.get("content", "").replace("\n", " ").strip()
        print(f"[{i:02d}] {time_str} | 📝 TEXT: {content}")

