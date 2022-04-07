from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View


from bookmarkapp.models import Bookmark
from likeapp.models import ArticleLikes

# 게시글 목록
from articleapp.services.service_article import (
    create_article, delete_article, get_client_ip, get_page_context,
    hit_article, read_all_article, read_article_by_title,
    read_article_by_title_within_a_specific_period,
    read_article_containing_username,
    read_article_containing_username_within_a_specific_period,
    read_category_article, read_target_article, update_article)
# 단일 게시글 CRUD
from commentapp.models import Comment


from commentapp.services.comment_service import read_all_comment, read_target_article_comment, read_best_comment
from bookmarkapp.services.bookmark_service import bookmark_check
from userapp.models import Profile

from .forms import ArticleForm
from .models import Category


class ArticleView(View):
    def get(self, request, pk):
        article_id = pk
        all_articles = read_all_article()[:8]
        recent_comments = read_all_comment()[:5]
        check_bookmark = bookmark_check(request.user.id, article_id)
        try:
            user_img = Profile.objects.get(user_id=request.user.id)
        except:
            user_img='https://png.clipart.me/istock/previews/9349/93493545-people-icon.jpg'
        try:
            ip = get_client_ip(request)

            target_article = hit_article(ip, pk)
            best_comment = read_best_comment()

            target_comment = read_target_article_comment(article_id)
            print(type(target_comment))
            if target_comment:
                target_profiles = []
                for comment in target_comment:
                    try:
                        profile_img = Profile.objects.get(user_id=comment.user.id)
                    except:
                        profile_img = 'https://png.clipart.me/istock/previews/9349/93493545-people-icon.jpg'


                    target_profiles.append(profile_img)

                target_data =[]
                for data in zip(target_comment,target_profiles):
                    target_data.append(data)
            else:
                target_data = False

            try:
                like_article = ArticleLikes.objects.filter(article=article_id, user=request.user.id).get()

                if best_comment:
                    best_profile = Profile.objects.get(user_id=best_comment.user.id)
                else:
                    best_profile = False
                return render(request, 'articleapp/article_detail.html',
                              {'target_article': target_article, 'target_date': target_data,
                               'target_comment': target_comment, 'user_img': user_img,
                               'best_comment': best_comment,'best_profile':best_profile,
                               'left_content_articles': all_articles, 'left_content_recent_comments': recent_comments,
                               'like_article': like_article, 'check_bookmark': check_bookmark},
                              status=200)
            # 좋아요가 없을 때
            except ObjectDoesNotExist:
                if best_comment:
                    best_profile = Profile.objects.get(user_id=best_comment.user.id)
                else:
                    best_profile = False

                return render(request, 'articleapp/article_detail.html',
                              {'target_article': target_article, 'user_img': user_img,
                               'left_content_articles': all_articles, 'left_content_recent_comments': recent_comments,
                               'best_comment':best_comment,'best_profiles':best_profile, 'target_date': target_data,
                            'target_comment':target_comment, 'check_bookmark': check_bookmark}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'msg': "게시글이 존재하지 않습니다."}, status=404)

    def post(self, request):
        try:
            create_article(title=request.POST.get('title'),
                           user_id=request.user,
                           content=request.POST.get('content'),
                           category=request.POST.get('category'),
                           img=request.POST.get('img', ''))
            return JsonResponse({'result': '게시글이 생성 되었습니다.'}, status=200)

        except TypeError:
            return JsonResponse({'msg': "항목을 다시 확인 해 주세요."}, status=404)

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
@login_required(login_url="/users/login/")
def write_article(request):
    all_articles = read_all_article()[:8]
    recent_comments = read_all_comment()[:5]
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()


            return redirect(f'/communities/{category}/') # 작성한 게시판으로 리로드 해놓음.

    if request.method == 'GET':
        article_form = ArticleForm()

        return render(request, 'articleapp/article_write.html', {'article_form': article_form, 'left_content_articles':all_articles, 'left_content_recent_comments':recent_comments}, status=200)



# 홈
def show_all_article(request):
    all_articles = read_all_article()
    recent_comments = read_all_comment()[:5]
    page = int(request.GET.get('page', 1))
    board_list = get_page_context(all_articles, page)

    return render(request, 'articleapp/article_all.html',
                  {'main_area_article': all_articles, 'left_content_articles': all_articles[:8],
                   'board_list': board_list, 'left_content_recent_comments': recent_comments}, status=200)


# 카테고리 별 게시판 불러오기
def show_question_article(request):
    all_articles = read_all_article()
    recent_comments = read_all_comment()[:5]

    target_articles = read_category_article('question')
    if target_articles:
        page = int(request.GET.get('page', 1))
        board_list = get_page_context(target_articles, page)
        return render(request, 'articleapp/article_question.html',
                      {'board_list': board_list, 'left_content_articles': all_articles[:8],
                       'left_content_recent_comments': recent_comments}, status=200)
    else:
        return render(request, 'articleapp/article_question.html',
                      {'left_content_articles': all_articles,
                       'left_content_recent_comments': recent_comments, 'msg': 'article does not exist'}, status=200)


def show_free_article(request):
    all_articles = read_all_article()
    recent_comments = read_all_comment()[:5]

    target_articles = read_category_article('free')
    if target_articles:
        page = int(request.GET.get('page', 1))
        board_list = get_page_context(target_articles, page)
        return render(request, 'articleapp/article_free.html',
                      {'target_articles': target_articles, 'board_list': board_list,
                       'left_content_articles': all_articles[:8],
                       'left_content_recent_comments': recent_comments}, status=200)
    else:
        return render(request, 'articleapp/article_free.html',
                      {'left_content_articles': all_articles,
                       'left_content_recent_comments': recent_comments, 'msg': 'article does not exist'}, status=200)


def show_tip_article(request):
    all_articles = read_all_article()
    recent_comments = read_all_comment()[:5]

    target_articles = read_category_article('tip')
    print(target_articles)

    if target_articles:
        page = int(request.GET.get('page', 1))
        board_list = get_page_context(target_articles, page)
        return render(request, 'articleapp/article_tip.html',
                      {'target_articles': target_articles, 'board_list': board_list,
                       'left_content_articles': all_articles[:8],
                       'left_content_recent_comments': recent_comments}, status=200)
    else:
        return render(request, 'articleapp/article_tip.html',
                      {'left_content_articles': all_articles[:8],
                       'left_content_recent_comments': recent_comments, 'msg': 'article does not exist'}, status=200)


def show_category_article(request):
    all_articles = read_all_article()
    recent_comments = read_all_comment()[:5]

    target_articles = read_category_article(request.POST['category'])
    page = int(request.GET.get('page', 1))
    board_list = get_page_context(target_articles, page)
    return render(request, 'community.html',
                  {'target_articles': target_articles, 'board_list': board_list,
                   'left_content_articles': all_articles[:5],
                   'left_content_recent_comments': recent_comments}, status=200)


# 게시글 검색: 기간, 키워드(유저이름, 제목)
def search_article(request):
    all_articles = read_all_article()
    recent_comments = read_all_comment()[:5]

    standard = request.POST['standard']
    period = request.POST['period']
    keyword = request.POST['keyword']

    if period == 'all':
        if standard == 'title':
            target_articles = read_article_by_title(keyword)
            page = int(request.GET.get('page', 1))
            board_list = get_page_context(target_articles, page)
            return render(request, 'community.html',
                          {'articles': target_articles, 'board_list': board_list, 'left_content_articles': all_articles,
                           'left_content_recent_comments': recent_comments},
                          status=200)

        else:
            target_articles = read_article_containing_username(keyword)
            page = int(request.GET.get('page', 1))
            board_list = get_page_context(target_articles, page)
            return render(request, 'community.html',
                          {'articles': target_articles, 'board_list': board_list,
                           'left_content_articles': all_articles[:8],
                           'left_content_recent_comments': recent_comments},
                          status=200)

    else:
        if standard == 'title':
            try:
                target_articles = read_article_by_title_within_a_specific_period(period, keyword)
                page = int(request.GET.get('page', 1))
                board_list = get_page_context(target_articles, page)
                return render(request, 'community.html',
                              {'articles': target_articles, 'board_list': board_list,
                               'left_content_articles': all_articles[:8],
                               'left_content_recent_comments': recent_comments},
                              status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)

        else:
            try:
                target_articles = read_article_containing_username_within_a_specific_period(period, keyword)
                page = int(request.GET.get('page', 1))
                board_list = get_page_context(target_articles, page)
                return render(request, 'community.html',
                              {'articles': target_articles, 'board_list': board_list,
                               'left_content_articles': all_articles[:8],
                               'left_content_recent_comments': recent_comments},
                              status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)
