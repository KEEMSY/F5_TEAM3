import json

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View

from commentapp.services.comment_service import (create_comment,
                                                 delete_comment,
                                                 update_comment)
from userapp.models import Profile


class CommentView(View):
    def post(self, request):
        try:
            comment = create_comment(article_id=request.POST['article_id'], user_id=request.user.id,
                                     content=request.POST['content'])
            print(comment.created_at.strftime('%Y년 %m월 %d일 %H:%M'))
            print(Profile.objects.get(user_id=comment.user.id).img)
            try:
                user_img = 'https://cofi.s3.ap-northeast-2.amazonaws.com/' + str(
                    Profile.objects.get(user_id=comment.user.id).img)
            except:
                user_img = 'https://png.clipart.me/istock/previews/9349/93493545-people-icon.jpg'
            print(user_img)
            data = {
                'username': comment.user.username,
                'date': comment.created_at.strftime('%Y %m %d %H:%M'),
                'content': comment.content,
                'comment_pk': comment.id,
                'user_pk': comment.user.id,
                'user_img': user_img
            }

            return JsonResponse({'comment': data}, status=200)

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
            print(request.body)
            print(type(request.body))
            # comment_pk = request.DELETE.get('pk')
            comment_pk = json.loads(request.body)['pk']
            print(comment_pk)
            delete_comment(comment_id=comment_pk)
            return JsonResponse({'msg': '댓글이 삭제되었습니다.'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'msg': '댓글이 존재하지 않습니다.'}, status=400)


def show_home(request):
    return render(request, "base.html")
