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
