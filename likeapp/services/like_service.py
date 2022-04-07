from django.core.exceptions import ObjectDoesNotExist

from articleapp.models import Article
from commentapp.models import Comment
from likeapp.models import ArticleLikes, CommentLikes


def do_article_like(user_id: int, article_id: int) -> ArticleLikes:
    article = Article.objects.filter(pk=article_id).get()
    ArticleLikes.objects.create(user_id=user_id, article_id=article_id)
    article.like_cnt += 1
    article.save()



def undo_article_like(user_id: int, article_id: int) -> None:
    article = Article.objects.filter(pk=article_id).get()
    ArticleLikes.objects.get(user_id=user_id, article_id=article_id).delete()
    # delete_cnt, _ = ArticleLikes.objects.filter(
    #     user_id=user_id, article_id=article_id
    # ).delete()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    article.like_cnt -= 1
    article.save()


def do_comment_like(user_id: int, comment_id: int) -> CommentLikes:
    comment = Comment.objects.filter(pk=comment_id).get()
    Like = CommentLikes.objects.create(user_id=user_id, comment_id=comment_id)
    comment.like_count += 1
    comment.save()
    return Like


def undo_comment_like(user_id: int, comment_id: int) -> None:
    delete_cnt, _ = CommentLikes.objects.filter(
        user_id=user_id, comment_id=comment_id
    ).delete()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    if delete_cnt:
        comment = Comment.objects.filter(pk=comment_id).get()
        comment.like_count -= 1
        comment.save()