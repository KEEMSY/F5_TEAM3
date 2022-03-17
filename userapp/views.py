from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from user.models import UserModel

# AWS json 가져오기 위한 장치
# import os
# import json
# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent.parent
# with open(os.path.join(BASE_DIR, 'aws.json')) as f:
#     secrets = json.loads(f.read())
# AWS json 가져오기 위한 장치 여기까지


def login_page(request):
    return render(request,'userapp/login.html')


def sign_up_page(request):
    return render(request,'userapp/sign-up.html')