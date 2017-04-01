"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blogs.views import PostList, BlogList
from users.views import logout, LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout, name='logout'),
    url(r'^$', PostList.as_view(), name="posts_list"),
    url(r'^blogs/$', BlogList.as_view(), name="blog_list"),
    url(r'^blogs/(?P<username>[\w.@+-]+)/$', PostList.as_view(), name="posts_list"),
    #url(r'^posts/(?P<post_pk>[0-9]+)$', posts_detail, name="posts_detail"),
]
