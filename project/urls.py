from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.posts.urls')),
    path('gallery/', include('apps.gallery.urls')),
    # path('multimedia/', include('multimedia.urls')),
    path('schedule/', include('apps.schedule.urls')),
    path('about/', include('apps.about.urls')),
]

if settings.DEBUG and not settings.MINIO_STATIC:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG and not settings.MINIO_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
