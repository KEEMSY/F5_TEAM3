from django.shortcuts import redirect, render

# Create your views here.
from bookmarkapp.services.bookmark_service import do_bookmark, undo_bookmark
from likeapp.models import Author


def click_bookmark(request, article_id):
    user = request.user.is_authenticated
    user_id = Author.objects.get(user_id=request.user)
    if user:
        if request.method == "POST":
            do_bookmark(user_id, article_id)
            return render(request, "userapp/mypage.html")
        elif request.method == "DELETE":
            undo_bookmark(user_id, article_id)
            return render(request, "userapp/mypage.html")

    else:
        return redirect("/sign-in")
