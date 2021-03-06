from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

# Create your views here.
from articleapp.models import Article
from careerapp.models import Career, News
from userapp.models import Profile, User


def show_home(request):
    article_list = Article.objects.all().order_by("article_hits")
    news = News.objects.all().order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.

    skill = 'Python'
    board_lists = []
    career = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
    paginator = Paginator(career, 9)
    page = int(request.GET.get('page', 1))
    board = paginator.get_page(page)
    board_lists.append(board)

    if request.user.is_authenticated:
        target_user = request.user

        try:  # 유저 프로필 가져오는 걸 시도
            target_user_profile = Profile.objects.filter(user=target_user)
            if target_user_profile[0].skill is '':
                context = {'board_lists': board_lists, "news": news}
                return render(request, 'base.html', context)
            else:
                skills = []
                for i in target_user_profile:
                    skills.append(i.skill)
                board_lists = []

                for skill in skills:
                    career = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
                    paginator = Paginator(career, 9)
                    page = int(request.GET.get('page', 1))
                    board = paginator.get_page(page)
                    board_lists.append(board)

                context = {'board_lists': board_lists, "news": news}
                return render(request, 'base.html', context)
        except:  # 유저 프로필 가져오는 걸 실패하면 패스하고 위의 skill은 파이썬 으로 진행
            pass

            context = {'board_lists': board_lists, "news": news}
            return render(request, 'base.html', context)

    context = {'board_lists': board_lists, "news": news}
    return render(request, 'base.html', context)
    


def show_community(request):
    return render(request, 'articleapp/temp_commnuity.html')

def show_article_list_question(request):
    return render(request, 'articleapp/article_list_question.html')

def show_article_list_free(request):
    return render(request, 'articleapp/article_list_free.html')

def show_article_list_tip(request):
    return render(request, 'articleapp/article_list_tip.html')

def show_article_write(request):
    return render(request, 'articleapp/origin_article_write.html')

def show_404page(request):
    return render(request, '404page.html')





