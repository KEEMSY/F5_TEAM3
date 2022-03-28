from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from articleapp.models import Article
# Create your models here.
from likeapp.models import Post
from userapp.models import User


class Bookmark(models.Model):
    class Meta:
        db_table = "user_bookmark"
        constraints = [
            models.UniqueConstraint(fields=["user", "article"], name="unique_bookmark"),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    article = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="article")
    created_at = models.DateTimeField(auto_now_add=True)
