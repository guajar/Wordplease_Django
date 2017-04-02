from django.conf.urls import url
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, request, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.datetime_safe import datetime
from django.views.decorators import http
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin

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

        # Si en la ruta se especifica el usuario
        if self.kwargs:
            context = Post.objects.filter(blog__owner__username=self.request.user)
            return context
        # Si no se especifica usuario, genera una lista de todos los post ordenados por + actuales a - actuales
        else:
            context = Post.objects.filter(publish_date__lte=datetime.now())
            return context


class BlogList(ListView):

    model = Blog
    template_name = 'blogs/blog_list.html'


class PostDetail(DetailView):

    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # return custom template
            return render(request, '404.html', status=404)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    """
    def dispatch(self, request, *args, **kwargs):
        if self.request.user not in self.object.registered_users.all():
            return HttpResponseForbidden()
        else:
            return super(PostDetail, self).dispatch(request, *args, **kwargs)
    """

class NewPostView(CreateView):

    form_class = PostForm
    template_name = 'posts/new_post.html'
    success_url = 'post_detail'

    def form_valid(self, form):
        form.instance.blog = self.request.user.blog
        return super(NewPostView, self).form_valid(form)

    def get_success_url(self):
        """
        If everything is OK, we redirect the user to the new Post URL
        """
        post = self.object
        return reverse('post_detail', args=[post.blog.owner.username, post.pk])

    def form_invalid(self, form):
        return http.HttpResponse("form is invalid.. this is just an HttpResponse object")

