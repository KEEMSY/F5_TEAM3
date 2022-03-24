from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from . import forms


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

    #왜 겟으로 하면 안되지??
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
def profile(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, "userapp/profile.html", context)


# class SignUpView(FormView):
#     template_name = "userapp/sign-up.html"
#     form_class = forms.SignUpForm
#     success_url = reverse_lazy("home")
#
#     def form_valid(self, form):
#         form.save()
#         email = form.cleaned_data.get("email", '')
#         password = form.cleaned_data.get("password", '')
#         user = authenticate(self.request, email=email, password=password)
#         if user is not None:
#             login(self.request, user)
#
#         return super().form_valid(form)