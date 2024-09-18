from django.contrib import admin

from . import models
from .handlers import create


@admin.register(models.AlbumContent)
class AlbumContentAdmin(admin.ModelAdmin):
    list_display = ['album', 'file_type']
    exclude = ['slug']


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    exclude = ['slug']
    change_form_template = 'admin/gallery/album/change_form.html'

    def save_model(self, request, obj, form, change):
        files = request.FILES.pop('upload_files')
        obj.save()

        if files:
            create(album=obj, files=files)
