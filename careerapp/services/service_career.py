
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

