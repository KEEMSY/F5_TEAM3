from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from articleapp.models import Article, Author

# Create your views here.

# 게시글 목록
from articleapp.services.service_article import read_target_article, get_client_ip, hit_article, create_article, \
    update_article, delete_article, read_all_article, read_category_article, read_article_by_title


def article_read(request):
    all_articles = Article.objects.all().order_by("-created_at")  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_articles, 10)
    page = int(request.GET.get('page', 1))  # 1페이지 = 기본값
    board_list = paginator.get_page(page)
    return render(request, 'community.html', {'board_list': board_list, 'article_list': all_articles})


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


def board_list(request, pk: str):
    all_articles = Article.objects.filter(category=pk)
    paginator = Paginator(all_articles, 10)
    page = int(request.GET.get('page', 1))  # 1페이지 = 기본값
    board_list = paginator.get_page(page)
    return render(request, 'community.html', {'board_list': board_list, 'article_list': all_articles})
#####################

class ArticleView(View):
    def get(self, request, article_id):
        try:
            ip = get_client_ip(request)
            target_article = hit_article(ip, article_id)
            return render(request, 'article_detail.html', {'result': target_article}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'msg': "게시글이 존재하지 않습니다."}, status=404)

    def post(self, request):
        create_article(title=request.POST.get('title'),
                       user_id=request.user,
                       content=request.POST.get('content'))
        return JsonResponse({'result': '게시글이 생성 되었습니다.'})

    def patch(self, request, article_id):
        target_article = read_target_article(article_id)
        if request.user == target_article.user:
            try:
                update_article(request.PATCH.get('content'))
                return JsonResponse({'result': '게시글이 수정 되었습니다.'})
            except ObjectDoesNotExist:
                return JsonResponse({'result': '게시글이 존재하지 않습니다.'})

    def delete(self, request, article_id):
        try:
            delete_article(article_id)
            return redirect()
        except ObjectDoesNotExist:
            return JsonResponse({'result': '게시글이 존재하지 않습니다.'})


def show_all_article(request):
    articles = Article.objects.all()
    return render(request, 'community.html', {'articles': articles})


def show_category_article(request, category):
    target_articles = read_category_article(category)
    return render(request, {'articles': target_articles}, 'community.html')


def search_article_by_title(request, title):
    target_articles = read_article_by_title(title)
    return render(request,{'result':target_articles})
