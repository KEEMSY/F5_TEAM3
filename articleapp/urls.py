from django.urls import path

from articleapp import views
from articleapp.views import ArticleView

app_name = 'articleapp'

urlpatterns = [

    path('', views.show_all_article, name='home'),
    path('question/', views.show_question_article, name='question'),
    path('question/<int:pk>', ArticleView.as_view(), name='question_RUD'),

    path('free/', views.show_free_article, name='free'),
    path('free/<int:pk>', ArticleView.as_view(), name='free_RUD'),

    path('tip/', views.show_tip_article, name='tip'),
    path('tip/<int:pk>', ArticleView.as_view(), name='tip_RUD'),

    path('article/<int:pk>', ArticleView.as_view(), name='article_CRUD'),
    path('article/write/', views.write_article, name='aritcle_write'),

    path('search/', views.search_article, name='article_search'),


]