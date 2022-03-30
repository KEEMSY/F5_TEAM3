from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from likeapp.services.like_service import (do_article_like, do_comment_like,
                                           undo_article_like,
                                           undo_comment_like)


def click_article_like(request, article_id):
    user = request.user.is_authenticated
    if user:
        if request.method == "POST":
            try:
                do_article_like(request.user.id, article_id)
                return JsonResponse({'msg': '좋아요'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'msg': '삭제된 게시글입니다.'})
        elif request.method == "DELETE":
            try:
                undo_article_like(request.user.id, article_id)
                return JsonResponse({'msg': '좋아요 취소'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'msg': '삭제된 게시글입니다.'})

    else:
        return redirect("/sign-in")


def click_comment_like(request, comment_id):
    user = request.user.is_authenticated
    if user:
        if request.method == "POST":

            try:
                do_comment_like(request.user.id, comment_id)
                return JsonResponse({'msg': '좋아요'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'msg': '삭제된 댓글입니다.'})
        elif request.method == "DELETE":
            try:
                undo_comment_like(request.user.id, comment_id)
                return JsonResponse({'msg': '좋아요 취소'}, status=200)
            except ObjectDoesNotExist:
                return JsonResponse({'msg': '삭제된 댓글입니다.'})

    else:
        return redirect("/sign-in")