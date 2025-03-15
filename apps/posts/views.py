from django.conf import settings
from django.views.generic import ListView, DetailView

from apps.posts import models


# @method_decorator(cache_page(settings.REDIS_CACHE_TIMEOUT), name='get')
class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.filter(is_visible=True).order_by('-pk')
    template_name = 'post/list.html'
    paginate_by = settings.POSTS_PAGE_SIZE

    def get_context_data(self, **kwargs):
        qs = self.get_queryset()
        ctx = super().get_context_data(**kwargs)
        ctx['fixed_posts'] = qs.filter(fixed=True)
        ctx['posts'] = qs.filter(fixed=False)
        return ctx


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post/detail.html'
