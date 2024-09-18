from django.urls import path

from . import views


app_name = 'gallery'

urlpatterns = [
    # Albums
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail')
]
