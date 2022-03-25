from django.shortcuts import render
from careerapp.models import Career, Author
from django.core.paginator import Paginator
# Create your views here.
from careerapp.services.service_career import get_context


def show_job(request):

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
        return render(request, 'base.html', context)
