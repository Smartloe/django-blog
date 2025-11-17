from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    """文章分类"""

    name = models.CharField("分类名称", max_length=100, unique=True)
    slug = models.SlugField("URL别名", max_length=100, unique=True, blank=True)
    description = models.TextField("分类描述", blank=True, null=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    """博客文章"""

    STATUS_CHOICES = [
        ("draft", "草稿"),
        ("published", "已发布"),
    ]

    title = models.CharField("标题", max_length=200)
    slug = models.SlugField("URL别名", max_length=200, unique=True)
    content = models.TextField("内容")
    excerpt = models.TextField("摘要", max_length=300, blank=True)
    status = models.CharField(
        "状态", max_length=10, choices=STATUS_CHOICES, default="draft"
    )
    featured_image = models.ImageField(
        "特色图片", upload_to="blog/images/", blank=True, null=True
    )
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    published_at = models.DateTimeField("发布时间", default=timezone.now)
    views = models.PositiveIntegerField("浏览次数", default=0)
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        verbose_name="分类",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """文章评论"""

    post = models.ForeignKey(
        Post, verbose_name="文章", related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, verbose_name="评论者", on_delete=models.CASCADE)
    content = models.TextField("评论内容")
    created_at = models.DateTimeField("评论时间", auto_now_add=True)
    is_approved = models.BooleanField("已审核", default=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return f"{self.author} - {self.post.title}"
