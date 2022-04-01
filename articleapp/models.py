
from django.db import models

from TEAM3_F5_coFI.models import BaseModel
from userapp.models import User


class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=50)


class Article(BaseModel):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    img = models.TextField(null=True)
    like_cnt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    article_hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title



class ArticleHits(models.Model):
    class Meta:
        db_table = 'article_hits'
        verbose_name = '조회수 모델'
        verbose_name_plural = '조회수 모델'

    client_ip = models.CharField(max_length=100, db_index=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='조회날짜')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='게시글')

    def __str__(self):
        return str(self.article.id)


