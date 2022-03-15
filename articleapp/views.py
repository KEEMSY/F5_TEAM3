from django.shortcuts import render

# Create your views here.
from articleapp.models import Article


def show_article(requeset):
    articles = Article.objects.all()
    return render(requeset, 'community.html', {'articles':articles})