from django.db import models
from userapp.models import User


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    category = models.TextField(null=True)
    content = models.TextField(null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE())

    objects = models.Manager()
