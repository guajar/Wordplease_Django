from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):  # como toString() en Java
        return self.name


class Blog(models.Model):
    owner = models.OneToOneField(User, related_name="blog")
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # como toString() en Java
        return self.name


class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name="posts")
    title = models.CharField(max_length=80)
    summary = models.TextField(max_length=300)
    article = models.TextField()
    url_media = models.URLField(blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category, related_name="posts")

    # Metadata
    class Meta:
        ordering = ["-publish_date"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Post.
        """
        return reverse('post_list', args=[str(self.id)])

    def __str__(self):  # como toString() en Java
        return self.title


