from django.urls import path

from . import views


app_name = 'schedule'

urlpatterns = [
    path('weeks/', views.week_schedule, name='week_schedule_list'),
]
