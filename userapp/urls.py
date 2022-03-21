from django.urls import path

from userapp import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('sign_up/', views.sign_up_page, name='sign-up'),

]