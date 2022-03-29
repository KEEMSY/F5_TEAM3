from django.shortcuts import render

# Create your views here.

def show_home(request):
    return render(request, 'base.html')


def show_community(request):
    return render(request, 'articleapp/temp_commnuity.html')

def show_article_list_question(request):
    return render(request, 'articleapp/article_list_question.html')

def show_article_list_free(request):
    return render(request, 'articleapp/article_list_free.html')

def show_article_list_tip(request):
    return render(request, 'articleapp/article_list_tip.html')

def show_article_write(request):
    return render(request, 'articleapp/article_write.html')