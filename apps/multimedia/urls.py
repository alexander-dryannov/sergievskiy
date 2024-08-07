from django.urls import path

from . import views


app_name = 'mmedia'

urlpatterns = [
    path('', views.MultiMediaListView.as_view(), name='list'),
    path('media/create/', views.MultiMediaCreateView.as_view(), name='create'),
    path('media/<int:pk>/', views.MultiMediaDetailView.as_view(), name='detail'),
    path('media/<int:pk>/update/', views.MultiMediaUpdateView.as_view(), name='update'),
    path('media/<int:pk>/delete/', views.MultiMediaDeleteView.as_view(), name='delete'),
]
