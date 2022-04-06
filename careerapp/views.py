from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from careerapp.models import Career
from userapp.models import Profile, User

# Create your views here.


def show_job(request):
    target_user_id = request.user.id
    target_user_profile = Profile.objects.filter(id=target_user_id)

    skill = 'Python'
    board_lists = []
    career = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
    paginator = Paginator(career, 9)
    page = int(request.GET.get('page', 1))
    board = paginator.get_page(page)
    board_lists.append(board)

    # 로그인했고, 로그인 한 사람이 스킬까지 있다면, **수정 필요
    if request.user.is_authenticated:
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

    context = {'board_lists': board_lists}
    return render(request, 'career.html', context)