from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from userapp.models import User

from . import forms
from .forms import ProfileForm, UserForm


def signup_view(request):
    if request.user.is_authenticated: #유저가 로그인이 된 상태라면, signup url 접근을 막는 예외 처리
        return redirect(reverse('home'))

    form = forms.SignUpForm()
    if request.method == "POST": #post 요청일 때, 이메일과 패스워드를 forms.py를 거쳐 유효성 검사를 마친다.
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email", '')
            password = form.cleaned_data.get("password", '')

            user = authenticate(request, email=email, password=password)
            #athenticate 함수는 메일과 패스워드와 같은 credentials 인자들을 받고 이메일(ID)의 객체를 object.get(username=email)
            # **우리의 서비스는 이메일로 아이디를 받기 때문에 모델에서 username 필드를 이메일로 커스터마이징 했다.
            # DoesNotExist 에러이면 return user
            # 객체가 존재한다면 return None
            if user is not None:
                auth.login(request, user)
                return redirect('/')  #로그인 후 홈 화면으로...(**현재 페이지로 가는 걸로 업데이틀 필요)
            else:
                return render(request, "userapp/sign-up.html", {"form": form})

    return render(request, "userapp/sign-up.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated: #유저가 로그인이 된 상태라면, signup url 접근을 막는 예외 처리
        return redirect(reverse('home'))

    if request.method == "POST":
        form = forms.LoginForm(request.POST) #POST 정보를 forms.py에 작성한 LoginForm에 보내고, 검증을 거친 데이터나 해당하는 에러를 받아온다.
        email = request.POST.get("email", '')
        password = request.POST.get("password", '')

        get_user = auth.authenticate(request, email=email, password=password)
        if get_user is not None:
            auth.login(request, get_user)
            return redirect("/") # signup 과 마찬가지로 로그인 후 최근 활동한 페이지로 이동할 수 있도록 업데이트 필요
        else:
            return render(request, "userapp/login.html", {"form": form}) #데이터 유호성 검사를 실패한 에러 메시지를 보내준다.

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
                        #request.POST 는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체, request.POST[key]에 해당하는 value는 항상 문자열! 만약, 해당하는 key의 value가 없다면 keyerror를 반환

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
        profile = profile_form.save(commit=False)  # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해줘야 하므로 commit=False를 통해 우선 디비 저장을 바로 안하고 유저를 지정 후에 디비에 저장
        #form.save()를 사용 시 자동적으로 DB에 내용이 저장되고 반영됩니다.
        #여기서 DB 저장 여부를 commit=True, False와 같은 flag를 통해 지정해줄 수 있습니다.
        #commit=False는 DB에 반영하지 않는 것을 의미합니다.

        profile.user = u
        profile.save()

    return redirect(f'/users/profile/{int(pk)}/', pk=request.user.pk)  # 수정된 화면 보여주기


#### 모델 합치면 import 해서 ajax 형식으로 마이페이지에 데이터 뿌려주는 get 형식 view
### 아티클, 북마크 겟 함수 // 현재는 모델이 꼬일까바 주석 처리로 해놓았음!
## form 데이터도 같이 뿌려줘야하나...? user_form, profile_form... ajax 형식이라 그부분에 대한 데이터만 필요한거 아닐까..??

# @login_required(login_url="/users/login/")
# def get_profile_article(request, pk):
#     if request.is_ajax:
#         all_articles = Article.objects.filter(user_id=pk)
#         return render(request, 'userapp/profile.html', {"all_articles": all_articles})


# @login_required(login_url="/users/login/")
# def get_profile_bookmark(request, pk):
#     if request.is_ajax:
#         all_bookmarks = Bookmark.objects.filter(user_id=pk)
#         return render(request, 'userapp/profile.html', {"all_bookmarks": all_bookmarks})

