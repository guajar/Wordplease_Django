from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=50)
    intro = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automáticamente añada la fecha de creación
    modified_at = models.DateTimeField(auto_now=True)  # Automáticamente actualiza la fecha al guardar
    # Category FK
    owner = models.ForeignKey(User, related_name="owner_posts")

    def __str__(self):  # como toString() en Java
        return self.title
