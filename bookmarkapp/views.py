from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from bookmarkapp.services.bookmark_service import do_bookmark, undo_bookmark


def click_bookmark(request, article_id):
    user = request.user.is_authenticated
    if user:
        if request.method == "POST":
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
    else:
        return redirect("/sign-in")

