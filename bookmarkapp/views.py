from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from bookmarkapp.models import Bookmark

# Create your views here.


def show_mypage(request):
    return render(request,'userapp/mypage.html')