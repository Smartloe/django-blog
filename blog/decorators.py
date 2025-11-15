from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def admin_required(view_func):
    """
    管理员权限装饰器
    要求用户必须是员工(is_staff=True)才能访问
    """

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "请先登录管理员账号")
            return redirect("/admin/")

        if not request.user.is_staff:
            messages.error(request, "您没有管理员权限")
            return redirect("/admin/")

        return view_func(request, *args, **kwargs)

    return wrapper
