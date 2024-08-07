from django.forms import forms

from schedule.models import Schedule


class ScheduleForm(forms):
    # time =
    # date =
    class Meta:
        model = Schedule
        fields = ('week', 'to_whom', 'type_service')
