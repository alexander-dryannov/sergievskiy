from django.conf import settings
from django.contrib import admin, messages
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

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(models.Clergy)
class ClergyAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'dignity')
    list_display_links = ('last_name', 'first_name', 'dignity')
    search_fields = ('last_name', 'first_name', 'dignity')



    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
