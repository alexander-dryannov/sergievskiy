from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models


class MultiMediaListView(ListView):
    model = models.MultiMedia
    queryset = model.objects.filter(is_visible=True)
    context_object_name = 'urls'
    template_name = 'multimedia/list.html'


class MultiMediaCreateView(LoginRequiredMixin, CreateView):
    model = models.MultiMedia
    template_name = 'multimedia/detail.html'


class MultiMediaDetailView(DetailView):
    model = models.MultiMedia
    template_name = 'multimedia/detail.html'


class MultiMediaUpdateView(LoginRequiredMixin, UpdateView):
    model = models.MultiMedia
    template_name = 'multimedia/update.html'
    fields = ['title', 'url', 'is_visible']
    raise_exception = True


class MultiMediaDeleteView(LoginRequiredMixin, DeleteView):
    model = models.MultiMedia
    template_name = 'multimedia/delete.html'
    success_url = reverse_lazy('mmedia:list')
    raise_exception = True
