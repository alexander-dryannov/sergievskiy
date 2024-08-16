from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.about import models

admin.site.register(models.Contact, SingletonModelAdmin)


@admin.register(models.Requisites)
class RequisitesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'current_account',
        'bank',
    )
    list_display_links = (
        'id',
        'current_account',
        'bank',
    )
    list_filter = ('bank',)
    search_fields = (
        'id',
        'current_account',
        'bank',
    )
