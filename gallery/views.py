import os
import uuid

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, FormView, ListView, UpdateView

from . import choices, models
from .forms import AlbumContentForm, AlbumForm


def create(files, album, is_deleted=False, is_visible=True):
    file_type = choices.FileType.IMAGE.value

    with transaction.atomic():
        for file in files:
            _, file_ext = os.path.splitext(file.name)
            file.name = f'{uuid.uuid4().hex}.{file_ext}'

            if file_ext in choices.VIDEO_EXTENSIONS:
                file_type = choices.FileType.VIDEO.value

            models.AlbumContent.objects.create(
                album=album,
                file=file,
                is_deleted=is_deleted,
                is_visible=is_visible,
                file_type=file_type,
            )
    return True


class AlbumListView(ListView):
    model = models.Album
    queryset = models.Album.objects.filter(is_visible=True, is_deleted=False)
    context_object_name = 'albums'
    template_name = 'album/list.html'


class AlbumCreateView(LoginRequiredMixin, FormView):
    form_class = AlbumForm
    template_name = 'album/create.html'
    success_url = reverse_lazy('gallery:album_list')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data['files']
        name = form.cleaned_data['title']
        is_visible = form.cleaned_data['is_visible']
        is_deleted = form.cleaned_data['is_deleted']
        cover = form.cleaned_data['cover']
        album_obj = models.Album.objects.create(
            title=name, is_visible=is_visible, is_deleted=is_deleted, cover=cover
        )

        with transaction.atomic():
            create(
                files=files,
                album=album_obj,
                is_visible=is_visible,
                is_deleted=is_deleted,
            )

        return super().form_valid(form)


class AlbumDetailView(DetailView):
    model = models.Album
    template_name = 'album/detail.html'

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


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Album
    template_name = 'album/update.html'
    fields = ('title', 'cover', 'is_visible', 'is_deleted')
    raise_exception = True


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Album
    template_name = 'album/delete.html'
    success_url = reverse_lazy('album_list')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        contents = models.AlbumContent.objects.filter()


def album_delete_to_cart(request, *args, **kwargs):
    album = models.Album.objects.filter(pk=kwargs['pk'])
    album_content = models.AlbumContent.objects.filter(album=album.first())
    with transaction.atomic():
        album_content.update(is_deleted=True, is_visible=False)
        album.update(is_deleted=True, is_visible=False)
    return redirect('gallery:album_detail', pk=kwargs['pk'])


def content_delete_to_cart(request, *args, **kwargs):
    album_content = models.AlbumContent.objects.filter(
        album__id=kwargs['album__pk'], slug=kwargs['slug']
    )
    album_content.update(is_deleted=True, is_visible=False)
    return redirect('gallery:image_detail', album__pk=kwargs['album__pk'], slug=kwargs['slug'])


class AlbumContentCreateView(LoginRequiredMixin, FormView):
    form_class = AlbumContentForm
    template_name = 'content/create.html'
    raise_exception = True

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('gallery:album_detail', args=[self.kwargs['album__pk']])

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data['files']
        is_visible = form.cleaned_data['is_visible']
        is_deleted = form.cleaned_data['is_deleted']

        album_obj = models.Album.objects.get(pk=self.kwargs['album__pk'])

        create(
            files=files,
            album=album_obj,
            is_visible=is_visible,
            is_deleted=is_deleted,
        )
        return super().form_valid(form)


class AlbumContentDetailView(DetailView):
    model = models.AlbumContent
    template_name = 'content/detail.html'


class AlbumContentUpdateView(LoginRequiredMixin, UpdateView):
    model = models.AlbumContent
    template_name = 'content/update.html'
    fields = ['file', 'album', 'is_visible', 'is_deleted']
    raise_exception = True


class AlbumContentDeleteView(LoginRequiredMixin, DeleteView):
    model = models.AlbumContent
    template_name = 'content/delete.html'
    success_url = reverse_lazy('gallery:album_detail')
    raise_exception = True


class AlbumContentDeleteToCartView(LoginRequiredMixin, UpdateView):
    model = models.Album
    template_name = 'content/delete_to_cart.html'
    success_url = reverse_lazy('gallery:album_detail')
    raise_exception = True
