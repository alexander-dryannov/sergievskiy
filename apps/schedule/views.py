import locale

from django.views import generic

from . import models


class WeekScheduleListView(generic.ListView):
    model = models.Week
    queryset = models.Week.objects.filter(is_visible=True)
    context_object_name = 'weeks'
    template_name = 'week/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule = []

        for week in self.model.objects.filter(is_visible=True):
            data = {'week': week}

            for sch in models.Schedule.objects.filter(is_visible=True, week_id=week.id):
                sch_date = sch.event.date()

                if not data.get('schedule'):
                    data['schedule'] = {sch_date: []}
                try:
                    data['schedule'][sch_date].append(sch)
                except KeyError:
                    data['schedule'][sch_date] = []
                    data['schedule'][sch_date].append(sch)
            schedule.append(data)

        context['data'] = schedule

        return context
