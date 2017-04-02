from django import forms
from django.forms import ModelForm
from blogs.models import Post


class PostForm(ModelForm):

    class Meta:

        model = Post
        exclude = ('blog',)
