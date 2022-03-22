from django.shortcuts import redirect, render
# Create your views here.
from likeapp.models import ArticleLikes, Author, CommentLikes, Datcle
from likeapp.services.like_service import (do_article_like, do_comment_like,
                                           undo_article_like,
                                           undo_comment_like)


def click_article_like(request, article_id):
    user = request.user.is_authenticated
    user_id = Author.objects.get(user_id=request.user)
    if user:
        if request.method == "POST":
            do_article_like(user_id, article_id)
            return render(request, "userapp/article.html")
        elif request.method == "DELETE":
            undo_article_like(user_id, article_id)
            return render(request, "userapp/article.html")

    else:
        return redirect("/sign-in")


def click_comment_like(request, comment_id):
    user = request.user.is_authenticated
    user_id = Author.objects.get(user_id=request.user)
    if user:
        if request.method == "POST":
            do_comment_like(user_id, comment_id)
            return render(request, "userapp/article.html")
        elif request.method == "DELETE":
            undo_comment_like(user_id, comment_id)

            return render(request, "userapp/article.html")

    else:
        return redirect("/sign-in")
