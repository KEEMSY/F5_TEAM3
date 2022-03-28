from articleapp.models import Article
from likeapp.models import ArticleLikes, CommentLikes, Datcle, Post
from userapp.models import User


def do_article_like(user_id: int, article_id: int) -> ArticleLikes:
    article = Post.objects.filter(pk=article_id).get()
    Like = ArticleLikes.objects.create(user_id=user_id, article_id=article_id)
    article.like_count += 1
    article.save()
    return Like


def undo_article_like(user_id: int, article_id: int) -> None:
    delete_cnt, _ = ArticleLikes.objects.filter(
        user_id=user_id, article_id=article_id
    ).delete()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    if delete_cnt:
        article = Post.objects.filter(pk=article_id).get()
        article.like_count -= 1
        article.save()


def do_comment_like(user_id: int, comment_id: int) -> CommentLikes:
    comment = Datcle.objects.filter(pk=comment_id).get()
    Like = CommentLikes.objects.create(user_id=user_id, comment_id=comment_id)
    comment.like_count += 1
    comment.save()
    return Like


def undo_comment_like(user_id: int, comment_id: int) -> None:
    delete_cnt, _ = CommentLikes.objects.filter(
        user_id=user_id, comment_id=comment_id
    ).delete()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    if delete_cnt:
        comment = Datcle.objects.filter(pk=comment_id).get()
        comment.like_count -= 1
        comment.save()
