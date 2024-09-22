from django.shortcuts import render
from django.views import generic

from . import models


def week_schedule(request):
    weeks = []
    context = {}
    week_qs = models.Week.objects.filter(is_visible=True)
    days = models.Day.objects.filter(is_visible=True)

    for week in week_qs:
        days_filter = days.filter(week=week)
        data = {'week': week, 'days_and_events': []}
        for day in days_filter:
            data['days_and_events'].append(
                {'day': day, 'events': models.Event.objects.filter(day=day, is_visible=True)}
            )
        weeks.append(data)
    context['weeks'] = weeks
    return render(request, template_name='week/list.html', context=context)
