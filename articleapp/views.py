from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from articleapp.models import Article, Author

# Create your views here.

#게시글 목록
def article_read(request):
    all_articles = Article.objects.all().order_by("-created_at")  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_articles, 10)
    page = int(request.GET.get('page', 1))  # 1페이지 = 기본값
    board_list = paginator.get_page(page)
    return render(request, 'community.html', {'board_list':board_list, 'article_list':all_articles})

# 'community.html', {'article_list':article_list, 'all_Articles':all_Articles})
def detail_read(request, article_id):
    feed = Article.objects.filter(id=article_id)
    print(feed)
    return render(request, 'detail.html', {'feed': feed})


def move_to_write(request):
    return render(request, 'new.html')


# @login_required() 해피패스를 위해 임시로 if else문 첨부
def write_Article(request):
    if request.user.is_authenticated:
        user = request.user.id
        b = Article(title=request.POST['title'], content=request.POST['detail'], user_id=user)
        b.save()
        return HttpResponseRedirect(reverse('articleapp:home'))
    else:
        b = Article(title=request.POST['title'], content=request.POST['detail'], user_id=1)
        b.save()
        return HttpResponseRedirect(reverse('articleapp:home'))

def article_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articleapp:home')


def board_list(request, pk:str):
    all_articles = Article.objects.filter(category=pk)
    paginator = Paginator(all_articles, 10)
    page = int(request.GET.get('page', 1))  # 1페이지 = 기본값
    board_list = paginator.get_page(page)
    return render(request, 'community.html', {'board_list':board_list, 'article_list':all_articles})



























#
# def show_article(request):
#     articles = Article.objects.all()
#     return render(request, 'community.html', {'articles': articles})

# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'blog/index.html', {'articles': articles})
