from django import forms
from django.forms import ModelForm

import blogs
from blogs.models import Post


class PostForm(ModelForm):

    class Meta:

        model = Post
        exclude = (blogs,)
