from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

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



@login_required(login_url="/users/login/")
def get_profile(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, "userapp/profile.html", context)

# @login_required(login_url="/users/login/")
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'userapp/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })