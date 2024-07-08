from django.urls import path

from . import views


app_name = 'gallery'

urlpatterns = [
    # Albums
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    path('album/<int:pk>/trash/', views.album_delete_to_cart, name='album_delete_to_cart'),
    # Content
    path(
        '<int:album__pk>/content/create/',
        views.AlbumContentCreateView.as_view(),
        name='content_create',
    ),
    path(
        'album/<int:album__pk>/<slug:slug>/',
        views.AlbumContentDetailView.as_view(),
        name='content_detail',
    ),
    path(
        'album/<int:album__pk>/<slug:slug>/update/',
        views.AlbumContentUpdateView.as_view(),
        name='content_update',
    ),
    path(
        'album/<int:album__pk>/<slug:slug>/delete/',
        views.AlbumContentDeleteView.as_view(),
        name='content_delete',
    ),
    path(
        'album/<int:album__pk>/<slug:slug>/trash/',
        views.content_delete_to_cart,
        name='content_delete_to_cart',
    ),
]
