from django.contrib import admin
from blogs.models import Blog, Post, Category

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Post)

