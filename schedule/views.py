from datetime import datetime

from django import forms
from django.urls import reverse_lazy
from django.views import generic

from . import models


class WeekScheduleListView(generic.ListView):
    model = models.Week
    queryset = models.Week.objects.filter(is_visible=True)
    context_object_name = 'weeks'
    template_name = 'week/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = [
            {
                'week': {'id': week.id, 'name': week.name},
                'schedule': list(models.Schedule.objects.filter(is_visible=True, week_id=week.id)),
            }
            for week in self.model.objects.filter(is_visible=True)
        ]
        return context
