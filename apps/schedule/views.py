from django.views import generic

from . import models


class WeekScheduleListView(generic.ListView):
    model = models.Week
    queryset = models.Week.objects.filter(is_visible=True)
    context_object_name = 'weeks'
    template_name = 'week/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weeks = []
        days = models.Day.objects.all().filter(is_visible=True)

        for week in self.queryset:
            days_filter = days.filter(week=week)
            data = {'week': week, 'days_and_events': []}
            for day in days_filter:
                data['days_and_events'].append(
                    {'day': day, 'events': models.Event.objects.filter(day=day, is_visible=True)}
                )
            weeks.append(data)
        context['weeks'] = weeks
        return context
