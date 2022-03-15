from django.urls import path

from articleapp import views

app_name = 'articleapp'

urlpatterns = [
    path('', views.show_article, name='home'),

]