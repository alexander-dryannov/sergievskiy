from django.urls import path

from . import views


app_name = 'schedule'

urlpatterns = [
    path('weeks/', views.WeekScheduleListView.as_view(), name='week_schedule_list'),
]
