from django.db import models

from articleapp.models.Author import Author


class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=50)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article_hits = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.title