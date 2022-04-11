import json

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View

from commentapp.services.comment_service import (create_comment,
                                                 delete_comment,
                                                 update_comment)
from likeapp.models import CommentLikes
from likeapp.services.like_service import comment_like_check
from userapp.models import Profile
from commentapp.models import Comment

class CommentView(View):
    def post(self, request):
        try:
            comment = create_comment(article_id=request.POST['article_id'], user_id=request.user.id,
                                     content=request.POST['content'])


            try:
                Profile.objects.filter(user_id=comment.user.id)

                if Profile.objects.get(user_id=comment.user.id).img is not None or Profile.objects.get(user_id=comment.user.id) == '':
                    user_img = 'https://cofi.s3.ap-northeast-2.amazonaws.com/' + str(
                        Profile.objects.get(user_id=comment.user.id).img)
                else:
                    user_img = 'https://png.clipart.me/istock/previews/9349/93493545-people-icon.jpg'
            except ObjectDoesNotExist:
                user_img = 'https://png.clipart.me/istock/previews/9349/93493545-people-icon.jpg'

            data = {
                'username': comment.user.username,
                'date': comment.created_at.strftime('%Y %m %d %H:%M'),
                'content': comment.content,
                'comment_pk': comment.id,
                'user_pk': comment.user.id,
                'user_img': user_img,


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
            # comment_pk = request.DELETE.get('pk')
            comment_pk = json.loads(request.body)['pk']
            delete_comment(comment_id=comment_pk)
            return JsonResponse({'msg': '댓글이 삭제되었습니다.'}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'msg': '댓글이 존재하지 않습니다.'}, status=400)


def show_home(request):
    return render(request, "base.html")
