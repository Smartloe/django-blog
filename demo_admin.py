#!/usr/bin/env python
"""
Django管理后台美化演示脚本
"""
import subprocess
import sys
import time


def run_command(cmd, description):
    """运行命令并显示结果"""
    print(f"\n{'='*60}")
    print(f"🔧 {description}")
    print("=" * 60)

    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            print(f"✅ 成功: {description}")
        else:
            print(f"❌ 失败: {description}")
            if result.stderr:
                print(f"错误信息: {result.stderr}")
    except subprocess.TimeoutExpired:
        print(f"⏰ 超时: {description}")
    except Exception as e:
        print(f"💥 异常: {description} - {e}")


def main():
    """主函数"""
    print("🎨 Django博客管理后台美化演示")
    print("=" * 60)

    urls = [
        ("http://127.0.0.1:8000/", "前台首页"),
        ("http://127.0.0.1:8000/login/", "用户登录"),
        ("http://127.0.0.1:8000/register/", "用户注册"),
        ("http://127.0.0.1:8000/admin/", "默认管理后台"),
        ("http://127.0.0.1:8000/admin-custom/", "美化管理后台"),
        ("http://127.0.0.1:8000/admin-login/", "管理员登录导向"),
    ]

    print("\n📋 测试所有页面...")
    for url, description in urls:
        run_command(f"curl -I {url}", f"测试 {description}")
        time.sleep(1)

    print(f"\n{'='*60}")
    print("🎯 访问链接")
    print("=" * 60)

    print("\n🌐 前台页面:")
    print("  • 首页: http://127.0.0.1:8000/")
    print("  • 用户登录: http://127.0.0.1:8000/login/")
    print("  • 用户注册: http://127.0.0.1:8000/register/")

    print("\n⚙️ 管理后台:")
    print("  • 默认管理后台: http://127.0.0.1:8000/admin/")
    print("  • 美化管理后台: http://127.0.0.1:8000/admin-custom/")
    print("  • 管理员登录导向: http://127.0.0.1:8000/admin-login/")

    print("\n👤 登录信息:")
    print("  • 用户名: admin")
    print("  • 密码: admin123")

    print("\n✨ 美化特性:")
    print("  • 现代化渐变色设计")
    print("  • 响应式布局")
    print("  • 动画和过渡效果")
    print("  • 统计仪表盘")
    print("  • FontAwesome图标")
    print("  • 自定义导航")

    print("\n🔧 管理功能对比:")
    print("  • 默认后台: Django原生管理界面")
    print("  • 美化后台: 自定义样式 + 仪表盘")

    print(f"\n{'='*60}")
    print("🚀 现在可以在浏览器中访问这些链接体验美化效果！")
    print("=" * 60)


if __name__ == "__main__":
    main()
