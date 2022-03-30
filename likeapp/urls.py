from django.urls import path

from . import views

app_name = "likeapp"

urlpatterns = [
    path(
        "articles/like/<int:article_id>", views.click_article_like, name="articlelike"
    ),
    path(
        "comments/like/<int:comment_id>", views.click_comment_like, name="commentlike"
    ),
]
