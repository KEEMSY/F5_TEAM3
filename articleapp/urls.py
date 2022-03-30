from django.urls import path

from articleapp import views
from articleapp.views import ArticleView

app_name = 'articleapp'

urlpatterns = [

    path('', views.show_all_article, name='home'),
    path('category/', views.show_category_article, name='category_list'),

    path('article/', ArticleView.as_view(), name='article_CRUD'),
    path('write/', views.write_article, name='aritcle_write'),

    path('search/', views.search_article, name='article_search'),

]