from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from articleapp.models import Article
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

class ArticleLikes(models.Model):
    class Meta:
        db_table = "article_likes"
        constraints = [
            models.UniqueConstraint(fields=["user", "article"], name="unique_user_article"),
        ]
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    user = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='article')


class CommentLikes(models.Model):
    class Meta:
        db_table = "comment_likes"
        constraints = [
            models.UniqueConstraint(fields=["user", "comment"], name="unique_user_comment"),
        ]
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    user = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='user')
    comment = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='comment')
