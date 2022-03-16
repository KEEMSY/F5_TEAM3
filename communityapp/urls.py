
from django.contrib import admin
from django.urls import path

from commentapp import views

app_name = 'communityapp'

urlpatterns = [
    path('', views.show_job, name='job'),
    path('/detail', views.show_job_detail, name="detail")

]
