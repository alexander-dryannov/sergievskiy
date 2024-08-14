from django.views.generic import ListView, DetailView

from apps.posts.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_visible=True).order_by('-is_fixed', '-pk')
    template_name = 'post/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
