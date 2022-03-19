from likeapp.models import ArticleLikes
from likeapp.models import CommentLikes

def do_article_like(user_id: int, article_id: int) -> ArticleLikes:
    return ArticleLikes.objects.create(user_id=user_id, article_id=article_id)


def undo_article_like(user_id: int, article_id: int) -> None:
    like = ArticleLikes.objects.filter(user_id=user_id, article_id=article_id).get()
    like.delete()

def do_comment_like(user_id: int, comment_id: int) -> CommentLikes:
    return CommentLikes.objects.create(user_id=user_id, comment_id=comment_id)


def undo_comment_like(user_id: int, comment_id: int) -> None:
    like = CommentLikes.objects.filter(user_id=user_id, comment_id=comment_id).get()
    like.delete()