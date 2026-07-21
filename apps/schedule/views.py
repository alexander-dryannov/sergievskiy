from django.utils import timezone

from django.db.models import Prefetch
from django.shortcuts import render

from . import models


def week_schedule(request):
    today = timezone.now().date()

    events_qs = models.Event.objects.filter(is_visible=True).order_by('time')

    days_qs = models.Day.objects.filter(
        is_visible=True,
        date__gte=today
    ).prefetch_related(
        Prefetch('events', queryset=events_qs)
    )

    recent_week_ids = models.Week.objects.filter(is_visible=True).order_by('-pk')[:2].values_list('id', flat=True)

    weeks = models.Week.objects.filter(id__in=recent_week_ids) \
        .prefetch_related(Prefetch('days', queryset=days_qs)) \
        .order_by('-pk')

    weeks_list = list(weeks)[::-1]

    return render(request, template_name='week/list.html', context={'data': weeks_list})
