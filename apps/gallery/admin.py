from django.contrib import admin, messages

from snippets.minio.delete import delete_object
from . import models
from .handlers import create


@admin.action(description='Удалить окончательно')
def delete_from_minio(modeladmin, request, queryset):
    for obj in queryset:
        if modeladmin.model.__name__ == models.Album.__name__:
            contents = models.AlbumContent.objects.filter(album=obj)
            minio_delete_objects = [content.file.name for content in contents]

            if contents:
                delete_object(minio_delete_objects)
                contents.delete()

            delete_object(obj=obj.cover.name)
        else:
            delete_object(obj=obj.file.name)

    queryset.delete()
    messages.success(request, 'Выбранные объекты удалены')


@admin.action(description='Переместить в корзину')
def delete_to_cart(modeladmin, request, queryset):
    queryset.update(is_deleted=True, is_visible=False)
    messages.success(request, 'Выбранные объекты перемещены в корзину')


@admin.register(models.AlbumContent)
class AlbumContentAdmin(admin.ModelAdmin):
    list_display = ['album', 'file_type', 'is_deleted', 'is_visible']
    exclude = ['slug']
    actions = [delete_to_cart, delete_from_minio]


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_deleted', 'is_visible']
    exclude = ['slug']
    change_form_template = 'admin/gallery/album/change_form.html'
    actions = [delete_to_cart, delete_from_minio]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        files = request.FILES.pop('upload_files')
        obj.save()

        if files:
            create(album=obj, files=files)
