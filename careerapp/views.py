from django.shortcuts import render
from careerapp.models import Career, Author
from django.core.paginator import Paginator
# Create your views here.


def show_job(request):

    if request.user.is_authenticated:
        target_user_id = request.user.id
        target_user = Author.objects.get(pk=target_user_id)
        skills = target_user.skill

        if len(skills) >= 2:
            careers = Career.objects.filter(id=-1) #careers 에 빈 쿼리셋값을 정의하고 싶은데 정의할 방법이 없어 도저히 가져올 수 없는 id=-1로 필터해서 빈값을 넣어줌.
            for skill in skills:
                career = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
                careers = career | careers
                # context에 모든 취업 정보를 저장

            paginator = Paginator(careers, 9)
            page = int(request.GET.get('page', 1))
            board_list = paginator.get_page(page)

            context = {'careers': careers, 'board_list': board_list}
            print(careers)
            print(paginator)
            return render(request, 'career.html', context)
        else:
            skill = skills
            careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
            paginator = Paginator(careers, 9)
            page = int(request.GET.get('page', 1))
            board_list = paginator.get_page(page)

            context = {'careers': careers, 'board_list': board_list}
            return render(request, 'career.html', context)

    else:
        skill = 'Python'
        careers = Career.objects.filter(skills=skill).order_by("id")  # 받아온 스킬이 없으므로 python 관련 취업정보만 나오게 설정
        paginator = Paginator(careers, 9)
        page = int(request.GET.get('page', 1))
        board_list = paginator.get_page(page)

        context = {'careers': careers, 'board_list': board_list}
        return render(request, 'career.html', context)
