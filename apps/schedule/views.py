from datetime import date

from django.shortcuts import render

from . import models


def week_schedule(request):
    weeks = []
    context = {}
    week_qs = models.Week.objects.filter(is_visible=True).order_by('-pk')[:2]
    week_qs = reversed(week_qs)

    if week_qs:
        for week in week_qs:
            days = models.Day.objects.filter(is_visible=True, date__gte=date.today())

            if days:
                days_filter = days.filter(week=week)
                data = {'week': week, 'days_and_events': []}

                for day in days_filter:
                    data['days_and_events'].append(
                        {'day': day, 'events': models.Event.objects.filter(day=day, is_visible=True)}
                    )
                weeks.append(data)
        context['weeks'] = weeks
    return render(request, template_name='week/list.html', context=context)
