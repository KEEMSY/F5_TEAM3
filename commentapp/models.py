from django.db import models

# Create your models here.
from TEAM3_F5_coFI.models import BaseModel


class Comment(BaseModel):

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.writer


    article = models.TextField()
    writer = models.TextField()
    content = models.TextField()


