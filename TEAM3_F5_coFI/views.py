from django.shortcuts import render

# Create your views here.

def show_home(request):
    return render(request, 'base.html')


def show_community(request):
    return render(request, 'articleapp/temp_commnuity.html')
