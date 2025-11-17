from django.contrib import admin

from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "author", "category", "published_at", "views")
    list_filter = ("status", "category", "created_at", "published_at")
    search_fields = ("title", "content", "excerpt")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    readonly_fields = ("views", "created_at", "updated_at")
    date_hierarchy = "published_at"
    ordering = ("-published_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at", "is_approved")
    list_filter = ("is_approved", "created_at")
    search_fields = ("content", "author__username")
