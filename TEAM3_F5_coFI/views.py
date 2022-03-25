from django.shortcuts import render

# Create your views here.
from careerapp.models import Career, Author, News
from careerapp.services.service_career import get_context


def show_home(request):



# -------------------------------------------------------  채용정보 예외처리 시작 -------------------------------------------------------
    if request.user.is_authenticated:
        target_user_id = request.user.id
        target_user = Author.objects.get(pk=target_user_id)
        skills = target_user.skill

        if len(skills) >= 2:
            for skill in skills:
                context = get_context(skill)
            return render(request, 'base.html', context)
        else:
            context = get_context(skills)
            return render(request, 'base.html', context)

    else:
        context = get_context("python")
# -------------------------------------------------------  채용정보 예외처리 끝 -------------------------------------------------------
# -------------------------------------------------------  뉴스정보 보내주기 시작 -------------------------------------------------------
        news = News.objects.all().order_by("id")  # 모든 데이터 조회, id +순으로 해야 최신업데이트된게 위로 나옴.
# -------------------------------------------------------  뉴스정보 보내주기 끝 -------------------------------------------------------
        context['news'] = news # context에 news 값 딕셔너리로 추가
        return render(request, 'base.html', context)
