from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


from articleapp.models import Article

# Create your models here.
from likeapp.models import Author, Post


class Bookmark(models.Model):
    class Meta:
        db_table = "user_bookmark"
        constraints = [
            models.UniqueConstraint(fields=["user", "article"], name="unique_bookmark"),
        ]

    user = models.ForeignKey(Author, on_delete=models.CASCADE, db_column="user")
    article = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="article")
    created_at = models.DateTimeField(auto_now_add=True)
