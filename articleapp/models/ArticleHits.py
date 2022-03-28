from django.db import models

from articleapp.models.Article import Article


class ArticleHits(models.Model):
    class Meta:
        db_table = 'article_hits'
        Verbose_name = '조회수 모델'
        Verbose_name_plural = '조회수 모델'

    client_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, null=True, verbose_name='사용자 iP주소')
    date = models.DateTimeField(auto_now_add=True, verbose_name='조회날짜')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='게시글')

    def __str__(self):
        return str(self.article.id)