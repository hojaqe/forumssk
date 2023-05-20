from django.contrib import admin
from .models import Category, Post, Rating, Comment, Like


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Like)


class RatingInline(admin.TabularInline):
    model = Rating


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'get_rating')
    inlines = [RatingInline]
    search_fields = ['title', 'body']
    ordering = ['created_at']
    list_filter = ['category__title']

