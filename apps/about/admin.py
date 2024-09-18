from django.contrib import admin, messages
from solo.admin import SingletonModelAdmin

from apps.about import models
from snippets.minio.delete import delete_object

admin.site.register(models.Contact, SingletonModelAdmin)


@admin.action(description='Удалить окончательно')
def delete_from_minio(modeladmin, request, queryset):
    for obj in queryset:
        if modeladmin.model.__name__ == models.Clergy.__name__:
            delete_object(obj=obj.photo.name)
        elif modeladmin.model.__name__ == models.Requisites.__name__:
            delete_object(obj=obj.qr_code.name)
    queryset.delete()
    messages.success(request, 'Выбранные объекты удалены')


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
    actions = [delete_from_minio]

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
    actions = [delete_from_minio]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
