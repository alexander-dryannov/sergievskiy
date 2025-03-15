from datetime import date

from django.shortcuts import render

from . import models


# @cache_page(settings.REDIS_CACHE_TIMEOUT)
def week_schedule(request):
    week_qs = models.Week.objects.filter(is_visible=True).order_by('-pk')[:2]
    week_qs = reversed(week_qs)
    days_qs = models.Day.objects.filter(is_visible=True, date__gte=date.today()).order_by('date')
    events_qs = models.Event.objects.filter(is_visible=True).order_by('time')

    weeks_data_list = []

    for week in week_qs:
        d = {'week': week, 'days_and_events': []}

        for day in days_qs.filter(is_visible=True, week=week).order_by('date'):
            events = events_qs.filter(day=day)
            d['days_and_events'].append({'day': day, 'events': events})

        weeks_data_list.append(d)

    return render(request, template_name='week/list.html', context={'data': weeks_data_list})
