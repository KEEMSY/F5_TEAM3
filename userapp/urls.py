from django.urls import path

from userapp import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path("logout/", views.log_out, name="logout"),
    path('sign_up/', views.signup_view, name='sign-up'),
    path('profile/<int:pk>/', views.get_profile, name='profile'),
    path('profile/<int:pk>/bookmark/', views.get_profile_bookmark, name='profile_bookmark'),
    path('profile/<int:pk>/update/', views.update_profile, name='update_profile'),


]
