#!/usr/bin/env python3
"""
Career-Copilot: Model Context Protocol (MCP) Server for NetEase 163 Mailbox.
Exposes tools to search and read emails from insistgang@163.com via stdio JSON-RPC.
"""

import sys
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.mail163 import NetEase163Reader

def handle_tools_list():
    return {
        "tools": [
            {
                "name": "read_163_inbox",
                "description": "Read recent incoming emails from NetEase 163 mailbox (insistgang@163.com)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "Number of emails to fetch (default: 10)",
                            "default": 10
                        },
                        "unread_only": {
                            "type": "boolean",
                            "description": "Whether to fetch only unread emails",
                            "default": False
                        },
                        "query": {
                            "type": "string",
                            "description": "Optional keyword search filter (e.g. '面试', 'HSBC', '施耐德')"
                        }
                    }
                }
            }
        ]
    }

def handle_call_tool(name: str, arguments: dict):
    if name == "read_163_inbox":
        limit = arguments.get("limit", 10)
        unread_only = arguments.get("unread_only", False)
        query = arguments.get("query")
        
        reader = NetEase163Reader()
        emails = reader.fetch_recent_emails(limit=limit, unread_only=unread_only, keyword=query)
        
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(emails, ensure_ascii=False, indent=2)
                }
            ]
        }
    raise ValueError(f"Unknown tool: {name}")

def main():
    reader = NetEase163Reader()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_call_tool("read_163_inbox", {"limit": 3}), ensure_ascii=False, indent=2))
        return

    # Basic stdio JSON-RPC loop
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            req_id = req.get("id")
            
            if method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": req_id, "result": handle_tools_list()}
            elif method == "tools/call":
                params = req.get("params", {})
                tool_name = params.get("name")
                args = params.get("arguments", {})
                result = handle_call_tool(tool_name, args)
                resp = {"jsonrpc": "2.0", "id": req_id, "result": result}
            else:
                resp = {"jsonrpc": "2.0", "id": req_id, "result": {}}
            
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {"jsonrpc": "2.0", "id": req.get("id") if "req" in locals() else None, "error": {"code": -32603, "message": str(e)}}
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
