from django.urls import path

from articleapp import views
from articleapp.views import ArticleView

app_name = 'articleapp'

urlpatterns = [

    path('', views.show_all_article, name='home'),
    path('question/', views.show_question_article, name='question'),
    path('free/', views.show_free_article, name='free'),
    path('tip/', views.show_tip_article, name='tip'),

    path('article/', ArticleView.as_view(), name='article_CRUD'),
    path('write/', views.write_article, name='aritcle_write'),

    path('search/', views.search_article, name='article_search'),

]