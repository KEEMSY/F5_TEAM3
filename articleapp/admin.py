from django.contrib import admin

from .models import Article, ArticleHits, Category

# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleHits)
admin.site.register(Category)


