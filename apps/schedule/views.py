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
            days = models.Day.objects.filter(
                is_visible=True, date__gte=date.today(), week=week
            ).order_by('date')

            if days:
                data = {'week': week, 'days_and_events': []}

                if not days:
                    continue

                for day in days:
                    data['days_and_events'].append(
                        {
                            'day': day,
                            'events': models.Event.objects.filter(
                                day=day, is_visible=True
                            ).order_by('time'),
                        }
                    )
                weeks.append(data)
        context['weeks'] = weeks
    return render(request, template_name='week/list.html', context=context)
    # days = models.Day.objects.filter(is_visible=True, date__gt=date.today()).order_by('date')
    # context = {}
    # for day in days:
    #     if not context.get(day.week):
    #         context['week'] = day.week
    # return render(request, template_name='week/list2.html', context={'days': days})

    # events = (
    #     models.Event.objects.filter(is_visible=True)
    #     .order_by('time')
    #     .select_related('day')
    #     .filter(day__date__gt=date.today())
    #     .order_by('day__date')
    # )
    #
    # data = {}
    #
    # for event in events:
    #     data[event.day.week] = []
    #
    #     if not data[event.day.week]:
    #         data[event.day.week].append(event.day) {event.day: [event]}
    #     else:
    #         data[event.day.week][event.day].append(event)
    #     x = 1
    #
    # return render(request, template_name='week/list.html', context={})


# All Events
# models.Event.objects.filter(is_visible=True).select_related('day').filter(day__date__gt=date.today()).order_by('time')
