from django.urls import path
from . import views

app_name = 'likeapp'

urlpatterns = [
    path('articles/like', views.click_article_like, name='articlelike'),

    path('comments/like', views.click_comment_like, name='commentlike'),

]
