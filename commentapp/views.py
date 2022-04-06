from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View

from commentapp.services.comment_service import (create_comment,
                                                 delete_comment,
                                                 update_comment)


class CommentView(View):
    def post(self, request):
        try:
            comment = create_comment(article_id=request.POST['article_id'], user_id=request.user.id,
                                     content=request.POST['content'])
            print(comment.created_at.strftime('%Y년 %m월 %d일 %H:%M'))
            date = {
                'username': comment.user.username,
                'date': comment.created_at.strftime('%Y %m %d %H:%M'),
                'content': comment.content
            }
            return JsonResponse({'comment': date}, status=200)

        except IntegrityError:
            return JsonResponse({'msg': '게시글이 존재하지 않습니다.'}, status=400)

    def patch(self, request):
        try:
            update_comment(comment_id=request.comment_id, content=request.content)
            return JsonResponse({'msg': '댓글이 수정되었습니다.'}, status=200)


        except ObjectDoesNotExist:
            return JsonResponse({'msg': '댓글이 존재하지 않습니다.'}, status=400)

    def delete(self, request):
        try:
            delete_comment(comment_id=request.DELETE.get('pk'))
            return JsonResponse({'msg': '댓글이 삭제되었습니다.'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'msg': '댓글이 존재하지 않습니다.'}, status=400)


def show_home(request):
    return render(request, "base.html")
