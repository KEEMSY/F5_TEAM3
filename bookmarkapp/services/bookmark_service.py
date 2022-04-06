from django.core.exceptions import ObjectDoesNotExist

from bookmarkapp.models import Bookmark


def bookmark_check(user_id, article_id):
    try:
        check = Bookmark.objects.filter(article_id=article_id, user_id=user_id).get()
        return check
    except ObjectDoesNotExist:
        return False


def do_bookmark(user_id: int, article_id: int) -> Bookmark:
    check = bookmark_check(user_id, article_id)

    if not check:
        Bookmark.objects.create(user_id=user_id, article_id=article_id)

    else:
        return False


def undo_bookmark(user_id: int, article_id: int) -> None:
    # print('user_id', user_id)
    # print('article_id', article_id)
    check = bookmark_check(user_id, article_id)
    if check:
        Bookmark.objects.get(user_id=user_id, article_id=article_id).delete()
    else:
        return False

