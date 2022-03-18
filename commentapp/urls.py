from django.urls import path
from .views import CommentView

app_name='commentapp'

urlpatterns = [
   path('',CommentView.as_view(),name='interatction_comment'),
]