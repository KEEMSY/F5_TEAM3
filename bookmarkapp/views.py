from django.http import JsonResponse
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
            return JsonResponse({'msg': '스크랩'}, status=200)
        elif request.method == "DELETE":
            undo_bookmark(user_id, article_id)
            return JsonResponse({'msg': '스크랩 취소'}, status=200)

    else:
        return redirect("/sign-in")
