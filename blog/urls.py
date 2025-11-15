from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # 首页
    path("", views.home, name="home"),
    # 用户认证
    path("login/", views.user_login, name="user_login"),
    path("admin-login/", views.admin_login_guide, name="admin_login_guide"),
    path("register/", views.UserRegistrationView.as_view(), name="user_register"),
    path("logout/", views.user_logout, name="user_logout"),
    path("profile/", views.user_profile, name="user_profile"),
    # 文章列表和详情
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    # 分类
    path("category/<slug:category_slug>/", views.category_posts, name="category_posts"),
    # 搜索
    path("search/", views.search_posts, name="search"),
    # 评论
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"),
]
