from django.urls import path

from articleapp import views
#
app_name = 'articleapp'

urlpatterns = [
    path('', views.show_article, name='home'),
    path('new', views.new, name='new'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]