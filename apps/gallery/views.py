from django.views.generic import DetailView, ListView

from . import choices, models


# from snippets.minio.delete import delete_object


class AlbumListView(ListView):
    model = models.Album
    queryset = models.Album.objects.filter(is_visible=True, is_deleted=False)
    context_object_name = 'albums'
    template_name = 'album/list.html'


class AlbumDetailView(DetailView):
    model = models.Album
    template_name = 'album/detail.html'

    def get_queryset(self):
        return self.model.objects.filter(is_visible=True, is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = models.AlbumContent.objects.filter(
            album=self.object.id,
            is_visible=True,
            is_deleted=False,
            file_type=choices.FileType.IMAGE.value,
        )
        context['videos'] = models.AlbumContent.objects.filter(
            album=self.object.id,
            is_visible=True,
            is_deleted=False,
            file_type=choices.FileType.VIDEO.value,
        )
        return context

# TODO: Добавить удаление альбомов из minio
# def delete_album_minio:
#     object = self.get_object() - album
#     contents = models.AlbumContent.objects.filter(album_id=object.id)
#     minio_delete_objects = [content.file.name for content in contents]
#
#     if contents:
#         delete_object(minio_delete_objects)
#         contents.delete()
#
#     delete_object(obj=object.cover.name)


# TODO: Добавить удаление альбомов из minio
# def delete_content_minio(self, request, *args, **kwargs):
#     object = self.get_object() - content
#
#     if object:
#         delete_object(obj=object.file.name)


# TODO: Перенести удаление в админку
# def album_content_delete_to_cart(request, *args, **kwargs):
#     album_content = models.AlbumContent.objects.filter(slug=kwargs.get('slug'))
#
#     if album_content:
#         with transaction.atomic():
#             album_content.update(is_deleted=True, is_visible=False)
#
#     return redirect('gallery:album_detail', pk=kwargs.get('album__pk'))


# TODO: Перенести удаление в админку
# def album_delete_to_cart(request, *args, **kwargs):
#     album = models.Album.objects.get(pk=kwargs.get('pk'))
#
#     if album:
#         album_contents = models.AlbumContent.objects.filter(album=album.first())
#
#         with transaction.atomic():
#             album_contents.update(is_deleted=True, is_visible=False)
#             album.update(is_deleted=True, is_visible=False)
#
#     return redirect('gallery:album_list')
