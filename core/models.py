import os
from django.conf import settings
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.FilePathField(path="static/img")

    def __str__(self):
        return f"{self.id}. {self.title}"

