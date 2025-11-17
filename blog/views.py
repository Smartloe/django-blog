<<<<<<< Updated upstream
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Q, F
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import CommentForm, UserLoginForm, UserRegistrationForm
from .models import Category, Comment, Post


def get_category_context():
    """获取分类及分类统计"""
    categories_qs = Category.objects.all().order_by("name")
    categories_with_count = [
        {"category": category, "count": category.published_count}
        for category in categories_qs.annotate(
            published_count=Count("post", filter=Q(post__status="published"))
        )
    ]
    return categories_qs, categories_with_count


def home(request):
    categories, categories_with_count = get_category_context()
    latest_posts = (
        Post.objects.filter(status="published")
        .select_related("author", "category")
        .order_by("-published_at")[:5]
    )
    context = {
        "latest_posts": latest_posts,
        "categories_with_count": categories_with_count,
        "categories": categories,
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    """文章列表"""

    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5

    def get_queryset(self):
        return (
            Post.objects.filter(status="published")
            .select_related("author", "category")
            .order_by("-published_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories, categories_with_count = get_category_context()
        context.update(
            {
                "categories": categories,
                "categories_with_count": categories_with_count,
                "category_slug": None,
            }
        )
        return context


class PostDetailView(DetailView):
    """文章详情"""

    model = Post
    template_name = "blog/post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return (
            Post.objects.filter(status="published")
            .select_related("author", "category")
            .prefetch_related("comments__author")
        )

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        Post.objects.filter(pk=self.object.pk).update(views=F("views") + 1)
        self.object.refresh_from_db(fields=["views"])
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories, categories_with_count = get_category_context()
        comments = (
            self.object.comments.filter(is_approved=True)
            .select_related("author")
            .order_by("created_at")
        )
        context.update(
            {
                "categories": categories,
                "categories_with_count": categories_with_count,
                "comments": comments,
                "comment_form": CommentForm(),
            }
        )
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponseForbidden
from django.db.models import Q, Count
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post, Category, Comment, UserProfile
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, CommentForm, UserProfileForm
import json


def home(request):
    """首页视图"""
    # 获取推荐文章
    featured_posts = Post.objects.filter(
        status='published',
        is_featured=True
    ).select_related('author', 'category')[:6]
    
    # 获取最新文章
    latest_posts = Post.objects.filter(
        status='published'
    ).select_related('author', 'category')[:10]
    
    # 获取热门文章（按阅读数）
    popular_posts = Post.objects.filter(
        status='published'
    ).order_by('-view_count')[:5]
    
    # 获取所有分类
    categories = Category.objects.annotate(
        post_count=Count('posts')
    )
    
    context = {
        'featured_posts': featured_posts,
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
        'categories': categories,
    }
    
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """文章列表视图"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Post.objects.filter(status='published').select_related('author', 'category')
        return queryset


class PostDetailView(DetailView):
    """文章详情视图"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # 增加阅读数
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # 获取相关文章（同一分类）
        related_posts = Post.objects.filter(
            category=post.category,
            status='published'
        ).exclude(id=post.id)[:3]
        
        # 获取评论
        comments = post.comments.filter(is_approved=True).select_related('author')
        
        context['related_posts'] = related_posts
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        
>>>>>>> Stashed changes
        return context


def category_posts(request, category_slug):
<<<<<<< Updated upstream
    """分类下的文章列表"""

    category = get_object_or_404(Category, slug=category_slug)
    posts = (
        Post.objects.filter(status="published", category=category)
        .select_related("author", "category")
        .order_by("-published_at")
    )
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get("page"))
    categories, categories_with_count = get_category_context()
    context = {
        "page_obj": page_obj,
        "categories": categories,
        "categories_with_count": categories_with_count,
        "category_slug": category.slug,
    }
    return render(request, "blog/post_list.html", context)


def search_posts(request):
    """文章搜索"""

    query = request.GET.get("q", "").strip()
    page_obj = None
    if query:
        posts = (
            Post.objects.filter(status="published")
            .select_related("author", "category")
            .filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(excerpt__icontains=query)
            )
            .order_by("-published_at")
        )
        paginator = Paginator(posts, 5)
        page_obj = paginator.get_page(request.GET.get("page"))

    categories, categories_with_count = get_category_context()
    context = {
        "query": query,
        "page_obj": page_obj,
        "categories": categories,
        "categories_with_count": categories_with_count,
    }
    return render(request, "blog/search_results.html", context)


@login_required
def add_comment(request, post_id):
    """添加评论"""

    post = get_object_or_404(Post, pk=post_id, status="published")
    categories, categories_with_count = get_category_context()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                content=form.cleaned_data["content"],
            )
            messages.success(request, "评论提交成功！")
            return redirect("blog:post_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/add_comment.html",
        {
            "form": form,
            "post": post,
            "categories": categories,
            "categories_with_count": categories_with_count,
        },
    )
=======
    """分类文章列表"""
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(
        category=category,
        status='published'
    ).select_related('author', 'category')
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    
    return render(request, 'blog/category_posts.html', context)


def search_posts(request):
    """搜索文章"""
    query = request.GET.get('q', '')
    posts = []
    
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        ).filter(status='published').select_related('author', 'category')
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'query': query,
        'page_obj': page_obj,
        'count': posts.count(),
    }
    
    return render(request, 'blog/search.html', context)
>>>>>>> Stashed changes


def user_login(request):
    """用户登录"""
<<<<<<< Updated upstream

    categories, categories_with_count = get_category_context()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not form.cleaned_data.get("remember_me"):
                    request.session.set_expiry(0)
                messages.success(request, "登录成功！")
                return redirect(request.GET.get("next") or "blog:home")
            messages.error(request, "用户名或密码错误")
    else:
        form = UserLoginForm()

    return render(
        request,
        "blog/user_login.html",
        {
            "form": form,
            "title": "用户登录",
            "categories": categories,
            "categories_with_count": categories_with_count,
        },
    )


@login_required
def user_logout(request):
    """用户退出"""

    logout(request)
    messages.info(request, "已退出登录")
    return redirect("blog:home")


class UserRegistrationView(View):
    """用户注册"""

    def get(self, request):
        categories, categories_with_count = get_category_context()
        form = UserRegistrationForm()
        return render(
            request,
            "blog/user_register.html",
            {
                "form": form,
                "title": "用户注册",
                "categories": categories,
                "categories_with_count": categories_with_count,
            },
        )

    def post(self, request):
        categories, categories_with_count = get_category_context()
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "注册成功，已自动登录")
            return redirect("blog:home")
        return render(
            request,
            "blog/user_register.html",
            {
                "form": form,
                "title": "用户注册",
                "categories": categories,
                "categories_with_count": categories_with_count,
            },
        )
=======
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, '登录成功！')
            return redirect('blog:home')
        else:
            messages.error(request, '用户名或密码错误')
    
    return render(request, 'blog/login.html')


def admin_login_guide(request):
    """管理员登录引导"""
    return render(request, 'blog/admin_login_guide.html')


class UserRegistrationView(CreateView):
    """用户注册视图"""
    form_class = UserRegistrationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:user_login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '注册成功！请登录您的账户。')
        return response


def user_logout(request):
    """用户退出"""
    logout(request)
    messages.success(request, '已成功退出！')
    return redirect('blog:home')
>>>>>>> Stashed changes


@login_required
def user_profile(request):
<<<<<<< Updated upstream
    """个人资料"""

    categories, categories_with_count = get_category_context()
    return render(
        request,
        "blog/user_profile.html",
        {
            "title": "个人资料",
            "categories": categories,
            "categories_with_count": categories_with_count,
        },
    )


def admin_login_guide(request):
    """管理员登录指引"""

    categories, categories_with_count = get_category_context()
    return render(
        request,
        "blog/admin_login_guide.html",
        {
            "categories": categories,
            "categories_with_count": categories_with_count,
        },
    )
=======
    """用户资料页面"""
    user = request.user
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, '资料更新成功！')
            return redirect('blog:profile')
    else:
        form = UserProfileForm(instance=user.profile)
    
    # 获取用户的文章
    user_posts = Post.objects.filter(author=user, status='published')
    
    # 获取用户的评论
    user_comments = Comment.objects.filter(author=user, is_approved=True)
    
    context = {
        'form': form,
        'user_posts': user_posts,
        'user_comments': user_comments,
    }
    
    return render(request, 'blog/profile.html', context)


def add_comment(request, post_id):
    """添加评论"""
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        
        if not request.user.is_authenticated:
            return JsonResponse({'error': '请先登录'}, status=401)
        
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            
            return JsonResponse({
                'success': True,
                'comment': {
                    'author': comment.author.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M'),
                }
            })
        else:
            return JsonResponse({'error': '评论内容不能为空'}, status=400)
    
    return JsonResponse({'error': '无效请求'}, status=400)
>>>>>>> Stashed changes
