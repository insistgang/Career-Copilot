"""
Career-Copilot: NetEase 163 Mailbox IMAP Reader & Notification Extractor.
Allows the agent to securely read incoming emails from insistgang@163.com.
"""

import os
import email
import imaplib
from email.header import decode_header
from pathlib import Path
from typing import List, Dict, Any, Optional

IMAP_SERVER = "imap.163.com"
IMAP_PORT = 993
DEFAULT_EMAIL = "insistgang@163.com"
CONFIG_FILE = Path.home() / ".config" / "career_copilot" / "mail163.env"


def _decode_str(s) -> str:
    """Decodes email headers handling multiple encodings (utf-8, gbk, gb2312, etc.)."""
    if not s:
        return ""
    decoded_parts = decode_header(s)
    result = []
    for content, encoding in decoded_parts:
        if isinstance(content, bytes):
            try:
                result.append(content.decode(encoding or "utf-8", errors="ignore"))
            except (LookupError, UnicodeDecodeError):
                result.append(content.decode("gbk", errors="ignore"))
        else:
            result.append(str(content))
    return "".join(result)


def _get_auth_code() -> Optional[str]:
    """Retrieves the 163 authorization code from environment or config file."""
    if "NETEASE_163_AUTH_CODE" in os.environ:
        return os.environ["NETEASE_163_AUTH_CODE"].strip()
    
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("NETEASE_163_AUTH_CODE="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


class NetEase163Reader:
    """Connects to NetEase 163 IMAP server to fetch and parse incoming emails."""

    def __init__(self, email_address: str = DEFAULT_EMAIL, auth_code: Optional[str] = None):
        self.email_address = email_address
        self.auth_code = auth_code or _get_auth_code()

    def is_configured(self) -> bool:
        return bool(self.auth_code)

    def fetch_recent_emails(self, limit: int = 10, unread_only: bool = False, keyword: Optional[str] = None) -> List[Dict[str, Any]]:
        """Fetches and parses the most recent emails from the 163 inbox."""
        if not self.auth_code:
            raise ValueError(
                f"未配置 163 邮箱客户端授权码！请在 {CONFIG_FILE} 中配置 NETEASE_163_AUTH_CODE=<你的16位授权码>"
            )

        # Connect to IMAP with SSL
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        try:
            mail.login(self.email_address, self.auth_code)
        except Exception as e:
            raise RuntimeError(f"163 邮箱登录失败 (请检查授权码是否正确): {e}")

        mail.select("INBOX")

        search_criteria = "UNSEEN" if unread_only else "ALL"
        status, messages = mail.search(None, search_criteria)
        if status != "OK" or not messages[0]:
            mail.logout()
            return []

        msg_ids = messages[0].split()
        # Get newest first
        target_ids = msg_ids[-limit:][::-1]
        
        parsed_emails = []
        for msg_id in target_ids:
            res, data = mail.fetch(msg_id, "(RFC822)")
            if res != "OK":
                continue
            
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            subject = _decode_str(msg.get("Subject", "无主题"))
            sender = _decode_str(msg.get("From", "未知发件人"))
            date_str = msg.get("Date", "")
            
            # Extract plain text or html body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        payload = part.get_payload(decode=True)
                        if payload:
                            charset = part.get_content_charset() or "utf-8"
                            body = payload.decode(charset, errors="ignore")
                            break
            else:
                payload = msg.get_payload(decode=True)
                if payload:
                    charset = msg.get_content_charset() or "utf-8"
                    body = payload.decode(charset, errors="ignore")

            # Keyword filter if provided
            if keyword and (keyword.lower() not in subject.lower() and keyword.lower() not in body.lower()):
                continue

            # Identify if this is a recruitment / interview / exam email
            is_job_related = any(k in subject.lower() or k in body.lower() for k in [
                "面试", "测评", "笔试", "录用", "offer", "招聘", "校招", "简历", "初试", "复试"
            ])

            parsed_emails.append({
                "id": msg_id.decode(),
                "subject": subject,
                "sender": sender,
                "date": date_str,
                "body_snippet": body.strip()[:300].replace("\n", " "),
                "full_body": body.strip(),
                "is_job_related": is_job_related
            })

        mail.logout()
        return parsed_emails
