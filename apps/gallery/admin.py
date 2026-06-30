from django.conf import settings
from django.contrib import admin, messages

from . import models
from .handlers import create


@admin.action(description='Переместить в корзину')
def delete_to_cart(modeladmin, request, queryset):
    queryset.update(is_deleted=True, is_visible=False)
    messages.success(request, 'Выбранные объекты перемещены в корзину')


@admin.register(models.AlbumContent)
class AlbumContentAdmin(admin.ModelAdmin):
    list_display = ['album', 'file_type', 'is_deleted', 'is_visible']
    exclude = ['slug']
    actions = [delete_to_cart]



@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_deleted', 'is_visible']
    exclude = ['slug']
    change_form_template = 'admin/gallery/album/change_form.html'
    actions = [delete_to_cart]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        try:
            files = request.FILES.pop('upload_files')
        except KeyError:
            files = None

        obj.save()

        if files:
            create(album=obj, files=files)
