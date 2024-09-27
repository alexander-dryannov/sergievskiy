from datetime import date

from django.shortcuts import render

from . import models


def week_schedule(request):
    context = {}
    week = models.Week.objects.filter(is_visible=True).last()

    if not week:
        return render(request, template_name='week/list.html', context=context)

    days = models.Day.objects.filter(is_visible=True, date__gte=date.today())

    if not days:
        return render(request, template_name='week/list.html', context=context)

    days_filter = days.filter(week=week)
    data = {'week': week, 'days_and_events': []}
    for day in days_filter:
        data['days_and_events'].append(
            {'day': day, 'events': models.Event.objects.filter(day=day, is_visible=True)}
        )
    context['week'] = data
    return render(request, template_name='week/list.html', context=context)
