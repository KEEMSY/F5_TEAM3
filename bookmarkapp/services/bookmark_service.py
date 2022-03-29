from bookmarkapp.models import Bookmark
from likeapp.models import Post


def do_bookmark(user_id: int, article_id: int) -> Bookmark:
    Scrap = Bookmark.objects.create(user_id=user_id, article_id=article_id)
    return Scrap


def undo_bookmark(user_id: int, article_id: int) -> None:
    Scrap = Bookmark.objects.filter(
        user_id=user_id, article_id=article_id
    ).get()  # 삭제된 로우의 개수(deleted_cnt)와 딕셔너리(_)
    Scrap.delete()
    # Scrap = Bookmark.objects.filter(pk=article_id).get()
