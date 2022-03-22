from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from bookmarkapp.services.bookmark_service import do_bookmark, undo_bookmark
from likeapp.models import Author


def click_bookmark(request, article_id):
    user = request.user.is_authenticated
    if user:
        if request.method == "POST":
<<<<<<< HEAD
            try:
                do_bookmark(request.user.id, article_id)
                return JsonResponse({'msg': '스크랩'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'msg': '삭제된 게시글입니다.'})
        elif request.method == "DELETE":
            try:
                undo_bookmark(request.user.id, article_id)
                return JsonResponse({'msg': '스크랩 취소'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'msg': '삭제된 게시글입니다.'})
=======
            do_bookmark(request.user.id, article_id)
            return JsonResponse({'msg': '스크랩'}, status=200)
        elif request.method == "DELETE":
            undo_bookmark(request.user.id, article_id)
            return JsonResponse({'msg': '스크랩 취소'}, status=200)
>>>>>>> df062662d5041588bdfad40cd58c95bf9feb26fb

    else:
        return redirect("/sign-in")

