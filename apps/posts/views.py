from django.views.generic import ListView, DetailView

from apps.posts.models import Post, FixedPost
from django.conf import settings


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_visible=True).order_by('-pk')
    template_name = 'post/list.html'
    paginate_by = settings.POSTS_PAGE_SIZE

    def get_queryset(self):
        fixed_post_ids = [fp.target.id for fp in FixedPost.objects.all().order_by('-pk')]
        queryset = self.queryset.exclude(id__in=fixed_post_ids)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['fixed_posts'] = [fp.target for fp in FixedPost.objects.all().order_by('-pk')]
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
