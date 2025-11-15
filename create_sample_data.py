import os
import django
from django.contrib.auth.models import User
from blog.models import Category, Post

# 设置Django环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_project.settings")
django.setup()


def create_sample_data():
    """创建示例数据"""
    print("正在创建示例数据...")

    # 创建分类
    categories_data = [
        {
            "name": "技术分享",
            "slug": "tech",
            "description": "分享编程技术、开发经验和最佳实践",
        },
        {
            "name": "生活感悟",
            "slug": "life",
            "description": "记录生活点滴、人生感悟和思考",
        },
        {
            "name": "学习笔记",
            "slug": "notes",
            "description": "学习过程中的知识记录和总结",
        },
    ]

    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={"slug": cat_data["slug"], "description": cat_data["description"]},
        )
        if created:
            print(f"创建分类: {category.name}")

    # 创建示例文章
    posts_data = [
        {
            "title": "Django博客系统开发指南",
            "slug": "django-blog-development-guide",
            "content": """# Django博客系统开发指南

Django是一个功能强大的Python Web框架，非常适合快速开发博客系统。

## 主要特性

1. **MVC架构**: Django采用了模型-视图-控制器的架构模式
2. **ORM系统**: 强大的对象关系映射，让数据库操作变得简单
3. **自动管理后台**: Django自带强大的管理界面
4. **安全性**: 内置了多种安全防护措施

## 开发步骤

1. 创建Django项目
2. 设计数据模型
3. 实现视图和URL路由
4. 创建模板
5. 配置静态文件

## 总结

Django框架让博客系统开发变得高效且有趣。通过合理的设计和实现，可以快速构建一个功能完善的博客平台。""",
            "excerpt": "详细介绍如何使用Django框架开发一个功能完善的博客系统，包括项目搭建、模型设计、视图实现等关键步骤。",
            "category": Category.objects.get(slug="tech"),
        },
        {
            "title": "Python编程最佳实践",
            "slug": "python-best-practices",
            "content": """# Python编程最佳实践

Python是一门优雅而强大的编程语言，遵循最佳实践可以让代码更加清晰和高效。

## 代码风格

遵循PEP 8规范，包括：
- 使用4个空格进行缩进
- 行长度不超过79个字符
- 使用有意义的变量名

## 性能优化

1. 合理使用列表推导式
2. 避免不必要的循环
3. 使用生成器处理大数据集

## 错误处理

```python
try:
    result = dangerous_operation()
except SpecificError as e:
    logger.error(f"操作失败: {e}")
    handle_error(e)
finally:
    cleanup()
```

## 总结

良好的编程习惯是成为优秀开发者的基础。""",
            "excerpt": "分享Python编程中的最佳实践，包括代码风格、性能优化、错误处理等方面的经验总结。",
            "category": Category.objects.get(slug="tech"),
        },
        {
            "title": "如何保持学习动力",
            "slug": "how-to-stay-motivated",
            "content": """# 如何保持学习动力

学习是一个持续的过程，保持动力至关重要。

## 设定明确目标

- 制定短期和长期目标
- 将大目标分解为小任务
- 定期回顾和调整目标

## 建立学习习惯

- 固定的学习时间
- 创造良好的学习环境
- 找到适合自己的学习方法

## 保持好奇心

- 探索新的知识领域
- 与他人交流学习心得
- 不断挑战自己的舒适区

## 总结

保持学习动力需要持续的实践和调整，找到适合自己的节奏和方法。""",
            "excerpt": "探讨如何在漫长的学习过程中保持动力和热情，分享实用的方法和策略。",
            "category": Category.objects.get(slug="life"),
        },
        {
            "title": "Django模型设计要点",
            "slug": "django-model-design-tips",
            "content": """# Django模型设计要点

良好的模型设计是Django应用的基础。

## 设计原则

1. **单一职责**: 每个模型应该专注于一个实体
2. **适当的关系**: 正确使用ForeignKey、ManyToManyField等
3. **字段选择**: 选择合适的数据类型和约束

## 实践技巧

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "文章"
        verbose_name_plural = "文章"
```

## 性能考虑

- 合理使用索引
- 避免N+1查询问题
- 使用select_related和prefetch_related

## 总结

好的模型设计会让后续开发事半功倍。""",
            "excerpt": "深入探讨Django模型设计的核心原则和实践技巧，帮助开发者构建高效的数据模型。",
            "category": Category.objects.get(slug="notes"),
        },
    ]

    # 确保admin用户存在
    admin_user = User.objects.filter(username="admin").first()
    if not admin_user:
        admin_user = User.objects.create_superuser(
            "admin", "admin@example.com", "admin123"
        )
        print("创建了admin用户")

    for post_data in posts_data:
        post, created = Post.objects.get_or_create(
            slug=post_data["slug"],
            defaults={
                "title": post_data["title"],
                "content": post_data["content"],
                "excerpt": post_data["excerpt"],
                "author": admin_user,
                "category": post_data["category"],
                "status": "published",
            },
        )
        if created:
            print(f"创建文章: {post.title}")

    print("示例数据创建完成！")
    print("管理员账号: admin")
    print("管理员密码: admin123")


if __name__ == "__main__":
    create_sample_data()
