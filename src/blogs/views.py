from django.utils.datetime_safe import datetime
from django.views.generic import ListView
from blogs.models import Post, Blog


class BlogMixin(object):
    def get_author(self):
        # How to get author?
        if self.kwargs:
            author = Blog.objects.filter(owner__username=self.kwargs['username'])
            return author


class PostList(ListView):

    template_name = 'posts/post_list.html'

    def get_queryset(self):

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

    """

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['post'] = Post.objects.select_related("blog").all()
        return context
    """
    """
    def posts_list(request):
       # Recupera todas los posts de la BBDD y las pinta
        #:param request: objeto HttpRequest
        #:return

        # Recuperar todas los posts de la BBDD
        posts = Post.objects.select_related("blog").all()

        # Comprobamos si se debe filtrar por posts creados por el user autenticado


        # Comprobamos si se debe filtrar por posts creadas por el user autenticado


        # Devolver la respuesta
        context = {
            'post_objects': posts
        }
        return render(request, 'posts/post_list.html', context)

    def posts_detail(request, post_pk):
        Recupera un post de la BBDD y la pinta con una plantilla
        :param request: HttpRequest
        :param post_pk: Primary key de la tarea a recuperar
        :return: HttpResponse
        # Recuperar el post
        # Opción 1
        try:
            post = Post.objects.select_related().get(pk=post_pk)
        except Post.DoesNotExist:
            return render(request, '404.html', status=404)
        except Post.MultipleObjectsReturned:
            return HttpResponse("Existen varias tareas con ese identificador", status=300)

        # Preparar el contexto
        context = {
            'post': post
        }

        # Renderizar la plantilla
        return render(request, 'posts/post_detail.html', context)
    """