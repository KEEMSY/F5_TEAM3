from django.contrib import auth
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from . import forms

from .models import User


class SignUpView(FormView):

    template_name = "userapp/sign-up.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("home")

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
    return redirect(reverse("home"))


def my_page(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, "userapp/mypage.html", context)
