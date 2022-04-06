from django.core.exceptions import ObjectDoesNotExist

from commentapp.models import Comment


def create_comment(article_id, user_id, content):
    return Comment.objects.create(
        article_id=article_id,
        user_id=user_id,
        content=content
    )


def read_all_comment():
    return Comment.objects.all().order_by('-id')


def read_best_comment():
    try:
        target_comment = Comment.objects.filter(like_cnt__gte=1).order_by('like_cnt').get()
        return target_comment
    except:
        return False


def read_target_article_comment(pk):
    target_comment = Comment.objects.filter(article_id=pk).order_by()
    if len(target_comment) != 0:
        return target_comment
    else:
        return False


def update_comment(comment_id, content):
    try:
        target_comment = Comment.objects.get(id=comment_id)
        target_comment.content = content
        target_comment.save()
    except ObjectDoesNotExist:
        return False


def delete_comment(comment_id):
    try:
        target_comment = Comment.objects.get(id=comment_id)
        target_comment.delete()
    except ObjectDoesNotExist:
        return False
