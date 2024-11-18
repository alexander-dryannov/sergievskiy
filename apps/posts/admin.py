from django.contrib import admin

from apps.posts import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'text', 'is_visible', 'fixed', 'created_at', 'updated_at')
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('created_at', 'author')
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at')
