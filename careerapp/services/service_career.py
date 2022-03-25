from typing import Any

from django.core.paginator import Paginator

from careerapp.models import Career


def get_context(skill: str, page: int = 1) -> dict[str, Any]:
    careers = Career.objects.filter(skills=skill).order_by("id")
    paginator = Paginator(careers, 9)  # 한페이지당 채용정보를 9개씩 담아서 보여줌.
    return {'careers': careers, 'board_list': paginator.get_page(page)}


# from django.shortcuts import render
#
# from careerapp.models import Career
#
#
# def show_career_info_by_skills(request, skill: str):
#     careers = Career.objects.filter(skills=skill).order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
#
#     # context에 모든 취업 정보를 저장
#
#
#     context = {'careers': careers}
#     return render(request, 'career.html', context)

