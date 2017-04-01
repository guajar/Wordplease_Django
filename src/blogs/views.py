from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView

from blogs.forms import PostForm
from blogs.models import Post, Blog


class BlogMixin(object):
    def get_author(self):
        # How to get author?
        if self.kwargs:
            author = Blog.objects.filter(owner__username=self.kwargs['username'])
            return author


class PostList(ListView):

    model = Post
    # paginate_by = 10
    template_name = 'posts/post_list.html'

    def get_queryset(self):

        auth_user = User.objects.get(username=self.request.user.username)
        # user_post = Post.objects.filter(blog__owner__username=self.kwargs['username'])
        # Si en la ruta se especifica el usuario
        if self.kwargs:
            context = Post.objects.filter(blog__owner__username=self.kwargs['username'])
            return context
        # Si no se especifica usuario, genera una lista de todos los post ordenados por + actuales a - actuales
        else:
            context = Post.objects.filter(publish_date__lte=datetime.now())
            return context


class BlogList(ListView):

    model = Blog
    template_name = 'blogs/blog_list.html'


class NewPostView(CreateView):

    model = Post
    form_class = PostForm
    template_name = 'posts/new_post.html'

