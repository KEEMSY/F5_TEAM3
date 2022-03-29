from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from articleapp.models import Article
# 게시글 목록
from articleapp.services.service_article import (
    create_article, delete_article, get_client_ip, get_page, hit_article,
    read_all_article, read_article_by_title,
    read_article_by_title_within_a_specific_period,
    read_article_containing_username,
    read_article_containing_username_within_a_specific_period,
    read_category_article, read_target_article, update_article)


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



def board_list(request, pk: str):
    all_articles = Article.objects.filter(category=pk)
    paginator = Paginator(all_articles, 10)
    page = int(request.GET.get('page', 1))  # 1페이지 = 기본값
    board_list = paginator.get_page(page)
    return render(request, 'community.html', {'board_list': board_list, 'article_list': all_articles})


#####################

# 단일 게시글 CRUD
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
        return JsonResponse({'result': '게시글이 생성 되었습니다.'}, status=200)

    def patch(self, request, article_id):
        target_article = read_target_article(article_id)
        if request.user == target_article.user:
            try:
                update_article(request.PATCH.get('content'))
                return JsonResponse({'result': '게시글이 수정 되었습니다.'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)

    def delete(self, request, article_id):
        try:
            delete_article(article_id)
            return JsonResponse({'result': '게시글이 삭제되었습니다.'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)


# 게시글 작성
def write_article(request):
    return render(request, 'community.html',status=200)q

# 홈
def show_all_article(request):
    all_articles = read_all_article()
    page = int(request.GET.get('page', 1))
    board_list = get_page(all_articles, page)
    return render(request, 'community.html', {'articles': all_articles, 'board_list': board_list}, status=200)

# 카테고리 별 게시판 불러오기
def show_category_article(request):
    target_articles = read_category_article(request.POST['category'])
    page = int(request.GET.get('page', 1))
    board_list = get_page(target_articles, page)
    return render(request, 'community.html', {'articles': target_articles, 'board_list': board_list}, status=200)


# 게시글 검색
def search_article(request):
    standard = request.POST['standard']
    period = request.POST['period']
    keyword = request.POST['keyword']

    # 전체 기간 조건
    if period == 'all':
        if standard == 'title':
            target_articles = read_article_by_title(keyword)
            page = int(request.GET.get('page', 1))
            board_list = get_page(target_articles, page)
            return render(request, 'community.html', {'articles': target_articles, 'board_list': board_list}, status=200)

        else:
            target_articles = read_article_containing_username(keyword)
            page = int(request.GET.get('page', 1))
            board_list = get_page(target_articles, page)
            return render(request, 'community.html', {'articles': target_articles, 'board_list': board_list}, status=200)

    # 기간이 있을 때
    else:
        if standard == 'title':
            try:
                target_articles = read_article_by_title_within_a_specific_period(period, keyword)
                page = int(request.GET.get('page', 1))
                board_list = get_page(target_articles, page)
                return render(request, 'community.html', {'articles': target_articles, 'board_list': board_list},
                              status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)

        else:
            try:
                target_articles = read_article_containing_username_within_a_specific_period(period, keyword)
                page = int(request.GET.get('page', 1))
                board_list = get_page(target_articles, page)
                return render(request, 'community.html', {'articles': target_articles, 'board_list': board_list},
                              status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)


