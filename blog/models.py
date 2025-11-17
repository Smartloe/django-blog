from django.db import models
from django.contrib.auth.models import User
<<<<<<< Updated upstream
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
=======
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


class Category(models.Model):
    """文章分类模型"""
    name = models.CharField(max_length=100, verbose_name='分类名称')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL标识')
    description = models.TextField(blank=True, verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']
>>>>>>> Stashed changes

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
<<<<<<< Updated upstream
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
=======
    """文章模型"""
    STATUS_CHOICES = [
        ('draft', '草稿'),
        ('published', '已发布'),
    ]

    title = models.CharField(max_length=200, verbose_name='标题')
    slug = models.SlugField(max_length=200, unique_for_date='publish_date', verbose_name='URL标识')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='作者')
    content = models.TextField(verbose_name='内容')
    excerpt = models.TextField(max_length=300, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name='分类')
    tags = models.CharField(max_length=200, blank=True, verbose_name='标签（逗号分隔）')
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name='封面图片')
    publish_date = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='状态')
    view_count = models.PositiveIntegerField(default=0, verbose_name='阅读数')
    is_featured = models.BooleanField(default=False, verbose_name='是否推荐')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-publish_date']
>>>>>>> Stashed changes

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

<<<<<<< Updated upstream

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
=======
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={
            'slug': self.slug
        })

    @property
    def tag_list(self):
        """返回标签列表"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []


class Comment(models.Model):
    """评论模型"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='文章')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='评论者')
    content = models.TextField(verbose_name='评论内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_approved = models.BooleanField(default=False, verbose_name='是否审核通过')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-created_at']

    def __str__(self):
        return f'评论 by {self.author.username} on {self.post.title}'


class UserProfile(models.Model):
    """用户资料模型"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='用户')
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='头像')
    location = models.CharField(max_length=100, blank=True, verbose_name='所在地')
    website = models.URLField(blank=True, verbose_name='个人网站')
    birth_date = models.DateField(null=True, blank=True, verbose_name='出生日期')

    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'

    def __str__(self):
        return f'{self.user.username}的资料'
>>>>>>> Stashed changes
