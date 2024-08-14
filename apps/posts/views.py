from django.views.generic import ListView, DetailView

from apps.posts.models import Post, FixedPost


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_visible=True).order_by('-pk')
    template_name = 'post/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['fixed_posts'] = [fp.target for fp in FixedPost.objects.all().order_by('-pk')]
        ctx['posts'] = self.queryset.exclude(id__in=[fp.id for fp in ctx['fixed_posts']])
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
