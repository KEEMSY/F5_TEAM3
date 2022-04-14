from django.core.exceptions import ObjectDoesNotExist

from articleapp.models import Article
from commentapp.models import Comment
from likeapp.models import ArticleLikes, CommentLikes
from userapp.models import User

from django.db.models import F

def comment_like_check(user_id, comment_id):
    try:
        check = CommentLikes.objects.filter(comment_id=comment_id, user_id=user_id).get()
        return check
    except ObjectDoesNotExist:
        return False


def do_article_like(user_id: int, article_id: int) -> ArticleLikes:
    # article = Article.objects.filter(pk=article_id).get()
    # ArticleLikes.objects.create(user_id=user_id, article_id=article_id)
    # article.like_cnt += 1
    # article.save()

    User.objects.filter(id=user_id).get()
    Article.objects.filter(id=article_id).get()

    like = ArticleLikes.objects.create(user_id=user_id, article_id=article_id)
    Article.objects.filter(id=article_id).update(like_cnt=F("like_cnt") + 1)

    return like



def undo_article_like(user_id: int, article_id: int) -> None:
    # article = Article.objects.filter(pk=article_id).get()
    # ArticleLikes.objects.get(user_id=user_id, article_id=article_id).delete()
    # # delete_cnt, _ = ArticleLikes.objects.filter(
    # #     user_id=user_id, article_id=article_id
    # # ).delete()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    # article.like_cnt -= 1
    # article.save()

    deleted_cnt, _ = ArticleLikes.objects.filter(user_id=user_id, article_id=article_id).delete()
    if deleted_cnt:
        Article.objects.filter(id=article_id).update(like_cnt=F("like_cnt") - 1)


def do_comment_like(user_id: int, comment_id: int) -> CommentLikes:
    comment = Comment.objects.filter(pk=comment_id).get()
    Like = CommentLikes.objects.create(user_id=user_id, comment_id=comment_id)
    comment.like_count += 1
    comment.save()


def undo_comment_like(user_id: int, comment_id: int) -> None:
    comment = Comment.objects.filter(pk=comment_id).get()
    CommentLikes.objects.get(user_id=user_id, comment_id=comment_id).delete()
    # delete_cnt, _ = CommentLikes.objects.filter(
    #     user_id=user_id, comment_id=comment_id
    # ).delete()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    comment.like_count -= 1
    comment.save()