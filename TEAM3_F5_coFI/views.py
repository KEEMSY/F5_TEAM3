from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from careerapp.models import Career, Author


def show_home(request):
    login_user = auth.authenticate(request)
    # print(me_username)
    if login_user is not None:
        target_user_id = request.user.id
        target_user = Author.objects.get(pk=target_user_id)
        skills = target_user.skill

        if len(skills) >= 2:
            for skill in skills:
                careers = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
                # skills = Author.objects.get(skill=skill)
                # context에 모든 취업 정보를 저장

                paginator = Paginator(careers, 9)
                page = int(request.GET.get('page', 1))
                board_list = paginator.get_page(page)

                context = {'careers': careers, 'board_list': board_list}
            return render(request, 'base.html', context)
        else:
            skill = skills
            careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
            paginator = Paginator(careers, 9)
            page = int(request.GET.get('page', 1))
            board_list = paginator.get_page(page)

            context = {'careers': careers, 'board_list': board_list}
            return render(request, 'base.html', context)

    else:
        skill = 'python'
        careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
        paginator = Paginator(careers, 9)
        page = int(request.GET.get('page', 1))
        board_list = paginator.get_page(page)

        context = {'careers': careers, 'board_list': board_list}
        return render(request, 'base.html', context)




