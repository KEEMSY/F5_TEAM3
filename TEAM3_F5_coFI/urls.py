"""TEAM3_F5_coFI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from TEAM3_F5_coFI import views

urlpatterns = [

    path('mbtif5/', admin.site.urls),
    path('users/', include("userapp.urls")),

    path("", include("likeapp.urls")),
    path("articles/", include("bookmarkapp.urls")),

    path('', views.show_home, name='home'),

    path('communities/', include("articleapp.urls")),
    path('comments/', include("commentapp.urls")),
    path('careers/', include("careerapp.urls")),


    # path('temp/', views.show_community, name='temp'),
    # path('temp1/question/', views.show_article_list_question, name='temp1_question'),
    # path('temp1/tip/', views.show_article_list_tip, name='temp1_tip'),
    # path('temp1/free/', views.show_article_list_free, name='temp1_free'),
    # path('temp2/', views.show_article_write, name='temp2'),

    path('accounts/', include('allauth.urls')),
    path('google/', include('allauth.urls')),

    path('404/', views.show_404page, name='404page'),
]
