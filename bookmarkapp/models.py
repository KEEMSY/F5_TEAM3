from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from articleapp.models import Article


class Bookmark(models.Model):
    class Meta:
        db_table = "user_bookmark"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, db_column='article')
    created_at = models.DateTimeField(auto_now_add=True)