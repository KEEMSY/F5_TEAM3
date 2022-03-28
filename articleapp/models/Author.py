from django.db import models


class Author(models.Model):
    name = models.TextField()