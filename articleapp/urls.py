from django.urls import path

from articleapp import views
from articleapp.views import ArticleView

app_name = 'articleapp'

urlpatterns = [

    path('', views.show_all_article, name='home'),
    path('<str:pk>', views.show_category_article, name='category_list'),

    path('article/', ArticleView.as_view(), name='article_CRUD'),


]