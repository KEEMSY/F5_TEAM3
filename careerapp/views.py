from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from careerapp.models import Career
from userapp.models import Profile, User


# Create your views here.


def show_job(request):

    skill = 'Python'
    board_lists = []
    career = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
    paginator = Paginator(career, 9)
    page = int(request.GET.get('page', 1))
    board = paginator.get_page(page)
    board_lists.append(board)

    if request.user.is_authenticated:
        target_user = request.user

        try: # 유저 프로필 가져오는 걸 시도
            target_user_profile = Profile.objects.filter(user=target_user)
            if target_user_profile[0].skill is '':
                context = {'board_lists': board_lists}
                return render(request, 'career.html', context)
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

                context = {'board_lists': board_lists}
                return render(request, 'career.html', context)
        except: # 유저 프로필 가져오는 걸 실패하면 패스하고 위의 skill은 파이썬 으로 진행
            pass

            context = {'board_lists': board_lists}
            return render(request, 'career.html', context)

    context = {'board_lists': board_lists}
    return render(request, 'career.html', context)
