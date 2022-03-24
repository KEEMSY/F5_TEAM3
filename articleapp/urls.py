from django.urls import path
from articleapp import views


app_name = 'articleapp'

urlpatterns = [

    # path('', views.home, name='home'), #페이지네이터
    path('', views.article_read, name='home'),
    path('<str:pk>', views.board_list, name='board_list'),
    path('<int:Article_id>', views.detail_read, name='detail_read'),
    path('write/', views.move_to_write, name='move_to_write'),
    path('write/write_Article', views.write_Article, name='write_Article'),
    path('article_delete/<int:article_id>', views.article_delete, name='article_delete'),

]