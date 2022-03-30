from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from articleapp.models import Article
from userapp.models import User
# Create your models here.


class Bookmark(models.Model):
    class Meta:
        db_table = "user_bookmark"
        constraints = [
            models.UniqueConstraint(fields=["user", "article"], name="unique_bookmark"),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, db_column="article")
    created_at = models.DateTimeField(auto_now_add=True)