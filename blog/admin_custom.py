"""自定义管理后台样式和功能"""

from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Category, Post, Comment


class CustomAdminSite(admin.AdminSite):
    """自定义管理站点"""

    site_header = format_html(
        '<span style="font-size: 24px; color: #007bff;">'
        '<i class="fas fa-blog"></i> Django 博客管理'
        "</span>"
    )
    site_title = "博客管理后台"
    index_title = "欢迎使用博客管理系统"

    def get_urls(self):
        from django.urls import include

        urls = super().get_urls()
        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    @staff_member_required
    def dashboard_view(self, request):
        """自定义仪表盘视图"""
        # 统计数据
        stats = {
            "total_posts": Post.objects.count(),
            "published_posts": Post.objects.filter(status="published").count(),
            "draft_posts": Post.objects.filter(status="draft").count(),
            "total_categories": Category.objects.count(),
            "total_comments": Comment.objects.count(),
            "pending_comments": Comment.objects.filter(is_approved=False).count(),
        }

        # 最新文章和评论
        latest_posts = Post.objects.order_by("-created_at")[:5]
        latest_comments = Comment.objects.order_by("-created_at")[:5]

        context = {
            **self.each_context(request),
            "stats": stats,
            "latest_posts": latest_posts,
            "latest_comments": latest_comments,
            "title": "仪表盘",
        }

        return TemplateResponse(request, "admin/dashboard.html", context)


# 创建自定义管理站点实例
custom_admin_site = CustomAdminSite(name="custom_admin")

# 注册模型到自定义管理站点
from .models import Category, Post, Comment

# 注册模型
custom_admin_site.register(Category)
custom_admin_site.register(Post)
custom_admin_site.register(Comment)
