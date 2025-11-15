#!/usr/bin/env python
"""Django博客系统状态检查"""

import subprocess
import sys


def run_command(cmd):
    """运行命令并返回输出"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.returncode


def check_server_status():
    """检查服务器状态"""
    print("=== Django博客系统状态检查 ===\n")

    # 检查首页
    print("1. 检查首页访问...")
    stdout, returncode = run_command("curl -I http://127.0.0.1:8000/")
    if returncode == 0 and "200 OK" in stdout:
        print("✅ 首页访问正常")
    else:
        print("❌ 首页访问失败")

    # 检查管理后台
    print("\n2. 检查管理后台...")
    stdout, returncode = run_command("curl -I http://127.0.0.1:8000/admin/")
    if returncode == 0 and ("302 Found" in stdout or "200 OK" in stdout):
        print("✅ 管理后台访问正常")
    else:
        print("❌ 管理后台访问失败")

    # 检查登录页面
    print("\n3. 检查登录页面...")
    stdout, returncode = run_command("curl -I http://127.0.0.1:8000/admin/login/")
    if returncode == 0 and "200 OK" in stdout:
        print("✅ 登录页面正常")
    else:
        print("❌ 登录页面访问失败")

    print("\n=== 登录信息 ===")
    print("🌐 网站首页: http://127.0.0.1:8000/")
    print("⚙️  管理后台: http://127.0.0.1:8000/admin/")
    print("👤 用户名: admin")
    print("🔑 密码: admin123")

    print("\n=== 使用说明 ===")
    print("1. 在浏览器中打开 http://127.0.0.1:8000/")
    print("2. 点击 '管理后台' 或直接访问 http://127.0.0.1:8000/admin/")
    print("3. 使用用户名 'admin' 和密码 'admin123' 登录")
    print("4. 在管理后台中可以管理文章、分类和评论")


if __name__ == "__main__":
    check_server_status()
