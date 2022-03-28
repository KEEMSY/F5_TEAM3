from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from userapp.models import User

from . import forms
from .forms import ProfileForm, UserForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email", '')
            password = form.cleaned_data.get("password", '')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, "userapp/sign-up.html", {"form": form})

    return render(request, "userapp/sign-up.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

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
    return redirect(reverse("home"))



def get_profile(request, pk):
    user = get_object_or_404(User, pk=pk)  # 로그인중인 사용자 객체를 얻어옴
    user_form = UserForm(initial={
        'username': user.username,
    })

    if hasattr(user, 'profile'):  # user가 profile을 가지고 있으면 True, 없으면 False (회원가입을 한다고 profile을 가지고 있진 않으므로)
        profile = user.profile
        profile_form = ProfileForm(initial={
            'img': profile.img,
            'skill': profile.skill,
            'github': profile.github,
            'blog': profile.blog,
        })
    else:
        profile_form = ProfileForm()

    #articles = Artilce.objects.filter(user_id=request.user.pk).order_by('-created_at') #-는 역순으로 정렬해서 준다는 의미
            #{'articles': articles} 를 아래 추가


    return render(request, 'userapp/profile.html', {"user_form": user_form, "profile_form": profile_form})


@login_required(login_url="/users/login/")
def update_profile(request, pk):
    u = User.objects.get(id=pk)  # 로그인중인 사용자 객체를 얻어옴
    user_form = UserForm(request.POST, instance=u)  # 기존의 것의 업데이트하는 것 이므로 기존의 인스턴스를 넘겨줘야한다. 기존의 것을 가져와 수정하는 것

    # User 폼
    if user_form.is_valid():
        user_form.save()

    if hasattr(u, 'profile'):
        profile = u.profile
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)  # 기존의 것 가져와 수정하는 것
    else:
        profile_form = ProfileForm(request.POST, request.FILES)  # 새로 만드는 것

    # Profile 폼
    if profile_form.is_valid():
        profile = profile_form.save(commit=False)  # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해줘야 하므로
        profile.user = u
        profile.save()

    return redirect(f'/users/profile/{int(pk)}/', pk=request.user.pk)  # 수정된 화면 보여주기


#def bookmark_ajax_get(request)  profile/<int:pk>/bookmarks/
#bookmark  Bookmark 모델에서 filter request.user.id

#def article_ajax_get(request)  profile/<int:pk>/artilce/
#articles  Article 모델에서 filter request.user.id

