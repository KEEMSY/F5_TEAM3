from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from articleapp.models import Article
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.

#게시글 목록
def article_read(request):
    all_articles = Article.objects.all().order_by("-created_at")  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_articles, 10)
    page = int(request.GET.get('page', 1))  # 1페이지 = 기본값
    board_list = paginator.get_page(page)
    return render(request, 'community.html', {'board_list':board_list, 'article_list':all_articles})

# 'community.html', {'article_list':article_list, 'all_Articles':all_Articles})
def detail_read(request, Article_id):
    feed = Article.objects.get(id=Article_id)
    return render(request, 'detail.html', {'feed': feed})

def move_to_write(request):
    return render(request, 'new.html')

def write_Article(request):
    b = Article(title=request.POST['title'], content=request.POST['detail'], user="Kang")
    b.save()
    return HttpResponseRedirect(reverse('articleapp:home'))

def article_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articleapp:home')

# #페이지네이터
# def home(request):
#     all_Articles = Article.objects.all().order_by("-created_at")   # 모든 데이터 조회, 내림차순(-표시) 조회
#     paginator = Paginator(all_Articles, 5)
#     page = int(request.GET.get('page', 1))    #1페이지 = 기본값
#     article_list = paginator.get_page(page)
#     return render(request, 'community.html', {'article_list':article_list, 'all_Articles':all_Articles})



































#
# def show_article(request):
#     articles = Article.objects.all()
#     return render(request, 'community.html', {'articles': articles})

# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', {'articles': articles})
