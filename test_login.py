#!/usr/bin/env python
"""测试管理员登录功能"""

import os
import django
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# 设置Django环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")
django.setup()


def test_admin_user():
    """测试管理员用户"""
    print("=== 测试管理员用户 ===")

    # 检查用户是否存在
    try:
        admin_user = User.objects.get(username="admin")
        print(f"✅ 找到管理员用户: {admin_user.username}")
        print(f"   - 是否超级用户: {admin_user.is_superuser}")
        print(f"   - 是否激活: {admin_user.is_active}")
        print(f"   - 邮箱: {admin_user.email}")

        # 测试密码认证
        auth_user = authenticate(username="admin", password="admin123")
        if auth_user:
            print("✅ 密码认证成功")
        else:
            print("❌ 密码认证失败")

    except User.DoesNotExist:
        print("❌ 未找到admin用户")

        # 重新创建管理员用户
        print("正在重新创建admin用户...")
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        print("✅ 重新创建admin用户成功")


def test_all_users():
    """测试所有用户"""
    print("\n=== 所有用户列表 ===")
    users = User.objects.all()
    if users:
        for user in users:
            print(
                f"- {user.username} (超级用户: {user.is_superuser}, 激活: {user.is_active})"
            )
    else:
        print("没有找到任何用户")


if __name__ == "__main__":
    test_admin_user()
    test_all_users()

    print("\n=== 登录信息 ===")
    print("管理后台地址: http://127.0.0.1:8000/admin/")
    print("用户名: admin")
    print("密码: admin123")
