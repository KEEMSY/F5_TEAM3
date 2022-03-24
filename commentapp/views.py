from django.shortcuts import render
from articleapp.models import Article
# Create your views here.



def show_home(request):
    article = Article.objects.all()
    return render(request, 'base.html', {'article':article})




