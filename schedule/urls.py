from django.urls import path

from . import views


app_name = 'schedule'

urlpatterns = [
    path('weeks/', views.WeekScheduleListView.as_view(), name='week_schedule_list'),
    # path('week/create/', views.WeekScheduleCreateView.as_view(), name='week_schedule_create'),
    # path(
    #     'week/<int:pk>/detail/',
    #     views.WeekScheduleDetailView.as_view(),
    #     name='week_schedule_detail',
    # ),
    # path(
    #     'week/<int:pk>/update/',
    #     views.WeekScheduleUpdateView.as_view(),
    #     name='week_schedule_update',
    # ),
    # path(
    #     'week/<int:pk>/delete/',
    #     views.WeekScheduleDeleteView.as_view(),
    #     name='week_schedule_delete',
    # ),
    # path('create/', views.ScheduleCreateView.as_view(), name='schedule_create'),
    # path('<int:pk>/detail/', views.ScheduleDetailView.as_view(), name='schedule_detail'),
    # path('<int:pk>/update/', views.ScheduleUpdateView.as_view(), name='schedule_update'),
    # path('<int:pk>/delete/', views.ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('service-types/', views.ServiceTypeListView.as_view(), name='service_type_list'),
    path(
        'service-type/create/', views.ServiceTypeCreateView.as_view(), name='service_type_create'
    ),
    path(
        'service-type/<int:pk>/detail/',
        views.ServiceTypeDetailView.as_view(),
        name='service_type_detail',
    ),
    path(
        'service-type/<int:pk>/update/',
        views.ServiceTypeUpdateView.as_view(),
        name='service_type_update',
    ),
    path(
        'service-type/<int:pk>/delete/',
        views.ServiceTypeDeleteView.as_view(),
        name='service_type_delete',
    ),
]
