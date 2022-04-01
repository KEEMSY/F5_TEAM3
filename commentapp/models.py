from django.db import models

from articleapp.models import Article
# Create your models here.
from TEAM3_F5_coFI.models import BaseModel
from userapp.models import User


class Comment(BaseModel):
    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.user

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
