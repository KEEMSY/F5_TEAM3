from django.db import models


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    user = models.CharField(max_length=50, null=True)
    category = models.TextField(null=True)

    objects = models.Manager()



