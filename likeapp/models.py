from typing import Any, List

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from articleapp.models import Article
# Create your models here.
from commentapp.models import Comment
from userapp.models import User


class ArticleLikes(models.Model):
    class Meta:
        db_table = "article_likes"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "article"], name="unique_user_article"
            ),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, db_column="article")


class CommentLikes(models.Model):
    class Meta:
        db_table = "comment_likes"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "comment"], name="unique_user_comment"
            ),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, db_column="comment")
