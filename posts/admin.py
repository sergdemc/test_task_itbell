from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title', 'text', 'created_at')
    search_fields = ('title',)
    list_filter = ('author', 'created_at')
    list_per_page = 10
