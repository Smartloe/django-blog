from django.contrib.auth import authenticate
from django.contrib.auth.models import User

admin_user = User.objects.get(username="admin")
print(f"用户: {admin_user.username}")
print(f"超级用户: {admin_user.is_superuser}")
print(f"激活: {admin_user.is_active}")

auth_user = authenticate(username="admin", password="admin123")
if auth_user:
    print("✅ 密码验证成功")
else:
    print("❌ 密码验证失败")
    print("正在重置密码...")
    admin_user.set_password("admin123")
    admin_user.save()
    print("✅ 密码已重置")
