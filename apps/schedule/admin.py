from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, reverse

from . import models
from .choices import ServiceTypeEnum


class DayInline(admin.StackedInline):
    model = models.Day
    extra = 0


class EventInline(admin.StackedInline):
    model = models.Event
    extra = 0


@admin.register(models.Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    inlines = [DayInline]


@admin.register(models.ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ordering']
    list_display_links = ['id', 'name']
    change_list_template = 'admin/schedule/servicetype/change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'autofill_view/',
                self.autofill_view,
                name='autofill_view',
            ),
        ]
        return my_urls + urls

    def autofill_view(self, request):
        service_type = [st[-1] for st in ServiceTypeEnum.choices]

        for st in service_type:
            models.ServiceType.objects.get_or_create(name=st)

        return HttpResponseRedirect(reverse('admin:schedule_servicetype_changelist'))


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['id', 'date']
    list_display_links = ['id', 'date']
    inlines = [EventInline]


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_day', 'time', 'get_services']
    list_display_links = ['id', 'time']

    @admin.display(description='Дата службы', ordering='day__date')
    def get_day(self, obj):
        return obj.day.date

    @admin.display(description='Тип службы')
    def get_services(self, obj):
        return ', '.join([ts.name for ts in obj.type_service.all()])
