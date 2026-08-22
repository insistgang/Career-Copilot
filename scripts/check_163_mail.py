import sys
import argparse
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.mail163 import NetEase163Reader, CONFIG_FILE

def main():
    parser = argparse.ArgumentParser(description="Check 163 mailbox for incoming emails")
    parser.add_argument("--limit", type=int, default=10, help="Number of emails to fetch")
    parser.add_argument("--unread", action="store_true", help="Fetch unread emails only")
    parser.add_argument("--query", type=str, help="Filter by keyword (e.g. 面试 / 测评)")
    parser.add_argument("--set-code", type=str, help="Save NetEase 163 Authorization Code")
    args = parser.parse_args()

    if args.set_code:
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            f.write(f"NETEASE_163_AUTH_CODE={args.set_code.strip()}\n")
        print(f"✅ 163 邮箱授权码已成功保存在: {CONFIG_FILE}")
        return

    reader = NetEase163Reader()
    if not reader.is_configured():
        print("=" * 60)
        print("⚠️ 尚未配置 163 邮箱授权码 (NETEASE_163_AUTH_CODE)！")
        print("=" * 60)
        print("📖 获取 163 授权码方法（仅需 30 秒）：")
        print("1. 浏览器登录网页版 163 邮箱：https://mail.163.com")
        print("2. 点击顶部【设置】➔【POP3/SMTP/IMAP】")
        print("3. 开启【IMAP/SMTP服务】并点击【新增授权密码】")
        print("4. 发送短信后会得到一串 16 位的客户端授权码（例如：ABCD1234EFGH5678）")
        print(f"5. 运行命令保存：python3 scripts/check_163_mail.py --set-code <你的授权码>")
        print("=" * 60)
        return

    print("🚀 正在连接 imap.163.com 拉取 insistgang@163.com 最新邮件...")
    try:
        emails = reader.fetch_recent_emails(limit=args.limit, unread_only=args.unread, keyword=args.query)
        print(f"✅ 成功拉取到 {len(emails)} 封邮件：\n")
        if not emails:
            print("📭 收件箱暂无符合条件的邮件。")
            return

        for i, m in enumerate(emails, 1):
            tag = "🎯【求职/面试相关】" if m["is_job_related"] else "📨 [普通邮件]"
            print(f"[{i:02d}] {tag} {m['subject']}")
            print(f"     发件人: {m['sender']}")
            print(f"     时间:   {m['date']}")
            print(f"     摘要:   {m['body_snippet'][:120]}...\n")
    except Exception as e:
        print(f"❌ 读取 163 邮箱失败: {e}")

if __name__ == "__main__":
    main()
