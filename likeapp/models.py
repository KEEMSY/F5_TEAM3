from typing import Any, List


from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from articleapp.models import Article


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    like_count = models.IntegerField(default=0)

    my_likes: List[Any]


class Author(models.Model):
    name = models.CharField(max_length=50)


class Datcle(models.Model):
    comment = models.CharField(max_length=200)
    like_count = models.IntegerField(default=0)

    my_likes: List[Any]



class ArticleLikes(models.Model):
    class Meta:
        db_table = "article_likes"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "article"], name="unique_user_article"
            ),
        ]

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    user = models.ForeignKey(Author, on_delete=models.CASCADE, db_column="user")
    article = models.ForeignKey(Post, on_delete=models.CASCADE, db_column="article")


class CommentLikes(models.Model):
    class Meta:
        db_table = "comment_likes"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "comment"], name="unique_user_comment"
            ),
        ]

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user')
    user = models.ForeignKey(Author, on_delete=models.CASCADE, db_column="user")
    comment = models.ForeignKey(Datcle, on_delete=models.CASCADE, db_column="comment")