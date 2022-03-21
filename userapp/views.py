from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.views.generic import FormView


# AWS json 가져오기 위한 장치
# import os
# import json
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# with open(os.path.join(BASE_DIR, 'aws.json')) as f:
#     secrets = json.loads(f.read())
# AWS json 가져오기 위한 장치 여기까지
# def login_page(request):
#     if request.method == 'GET':
#
#         return render(request,'userapp/login.html')
#
#     elif request.method == 'POST':
#         #로그인 성공하면
#         return redirect('/')
#
#
#
#
# def sign_up_page(request):
#     if request.method == 'GET':
#         return render(request,'userapp/sign-up.html')
#
#     elif request.method == 'POST':
#         #회원 가입 성공하면
#         return redirect('/')
from . import forms

# from user.models import UserModel



class SignUpView(FormView):

    template_name = "userapp/sign-up.html"
    form_class = forms.SignUpForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email", '')
        password = form.cleaned_data.get("password", '')
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        email = request.POST.get("email", '')
        password = request.POST.get("password", '')


        get_user = auth.authenticate(request, email=email, password=password)
        if get_user is not None:
            auth.login(request, get_user)
            return redirect("/")
        else:
            return render(request, "userapp/login.html", {"form": form})

    elif request.method == "GET":
        form = forms.LoginForm()
        return render(request, "userapp/login.html", {"form": form})


@login_required(login_url="/users/login/")
def log_out(request):
    auth.logout(request)
    return redirect('/')
