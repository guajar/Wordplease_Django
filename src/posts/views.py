from django.shortcuts import render

from posts.models import Post


def posts_list(request):
    """
    Recupera todas los posts de la BBDD y las pinta
    :param request: objeto HttpRequest
    :return
    """

    # Recuperar todas los posts de la BBDD
    posts = Post.objects.all()

    # Comprobamos si se debe filtrar por posts creados por el user autenticado


    # Comprobamos si se debe filtrar por posts creadas por el user autenticado


    # Devolver la respuesta
    context = {
        'post_objects': posts
    }
    return render(request, 'posts/list.html', context)
