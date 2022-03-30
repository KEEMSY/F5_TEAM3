from django.contrib import admin
from django.urls import path

from careerapp import views

app_name = 'careerapp'

urlpatterns = [
    path('', views.show_job, name='job'),
]

