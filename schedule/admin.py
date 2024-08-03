from django.contrib import admin

from . import models


class ScheduleInline(admin.TabularInline):
    model = models.Schedule
    fieldsets = (
        (
            'Основное',
            {
                'fields': (
                    'event',
                    'type_service',
                )
            },
        ),
        ('Описание', {'fields': ('to_whom',)}),
    )


@admin.register(models.Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    inlines = [ScheduleInline]


@admin.register(models.ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
