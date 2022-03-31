from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from careerapp.models import Career
from userapp.models import Profile, User


# Create your views here.


def show_job(request):
    ## 기본 화면##
    skill = 'Python'
    careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
    paginator = Paginator(careers, 9)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)

    ##로그인 했을 때 화면##
    # if request.user.is_authenticated:  # 로그인 했다면,
    #     u = get_object_or_404(User, pk=request.user.pk)  # 로그인한 유저의 객체를 가져오고
    #     try:
    #         target_user_id = request.user.id
    #         target_user_profile = Profile.objects.get(user_id=target_user_id)
    #         skills = target_user_profile.skill
    #
    #         if len(skills) >= 2:
    #             careers = Career.objects.filter(
    #                 id=-1)  # careers 에 빈 쿼리셋값을 정의하고 싶은데 정의할 방법이 없어 도저히 가져올 수 없는 id=-1로 필터해서 빈값을 넣어줌.
    #             for skill in skills:
    #                 career = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
    #                 careers = career | careers
    #                 # skills = User.objects.get(skill=skill)
    #                 # context에 모든 취업 정보를 저장
    #
    #             paginator = Paginator(careers, 9)
    #             page = int(request.GET.get('page', 1))
    #             board_list = paginator.get_page(page)
    #
    #             context = {'careers': careers, 'board_list': board_list}
    #             return render(request, 'career.html', context)
    #
    #         elif len(skills) == 1:
    #             skill = skills
    #             careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
    #             paginator = Paginator(careers, 9)
    #             page = int(request.GET.get('page', 1))
    #             board_list = paginator.get_page(page)
    #
    #             context = {'careers': careers, 'board_list': board_list}
    #             return render(request, 'career.html', context)
    #
    #         else:
    #             skill = 'Python'
    #             careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
    #             paginator = Paginator(careers, 9)
    #             page = int(request.GET.get('page', 1))
    #             board_list = paginator.get_page(page)
    #
    #             context = {'careers': careers, 'board_list': board_list}
    #             return render(request, 'career.html', context)
    #
    #     except:
    #         context = {'careers': careers, 'board_list': board_list}
    #         return render(request, 'career.html', context)

    context = {'careers': careers, 'board_list': board_list}
    return render(request, 'career.html', context)
