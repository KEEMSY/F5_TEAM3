from django.urls import path

from bookmarkapp import views

app_name = 'bookmarkapp'

urlpatterns = [
    path('', views.show_mypage, name='mypage'),
]