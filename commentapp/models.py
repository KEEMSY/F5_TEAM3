from django.db import models

# Create your models here.
from TEAM3_F5_coFI.models import BaseModel


class Author(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=50)


class Comment(BaseModel):
    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.user

    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
