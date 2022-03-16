from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from articleapp.models import Article
# Create your models here.
class ArticleLikes(models.Model):
    class Meta:
        db_table = "article_likes"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='article')

class CommentLikes(models.Model):
    class Meta:
        db_table = "comment_likes"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    comment = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='comment')
