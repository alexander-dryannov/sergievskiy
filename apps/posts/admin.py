from django.contrib import admin

from apps.posts.models import Post, FixedPost


@admin.action(description='Закрепить')
def set_fixed_post(modeladmin, request, queryset):
    for obj in queryset:
        FixedPost.objects.create(target=obj)


@admin.register(FixedPost)
class FixedPostAdmin(admin.ModelAdmin):
    fields = ('target',)
    list_display = (
        'id',
        'target',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [
        set_fixed_post,
    ]
    fields = ('title', 'author', 'text', 'created_at', 'updated_at')
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('created_at', 'author')
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at')
