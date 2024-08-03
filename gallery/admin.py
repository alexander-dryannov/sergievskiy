from django.contrib import admin

from . import models


class ContentInline(admin.StackedInline):
    model = models.AlbumContent
    exclude = ['slug']


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    exclude = ['slug']
    inlines = [
        ContentInline,
    ]
