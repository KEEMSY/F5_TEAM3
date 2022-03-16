from django.shortcuts import render

# Create your views here.


def show_job(request):
    return render(request,'community.html')


# 수정해야하는 부분
def show_job_detail(request):
    return render(request,'community.html')
