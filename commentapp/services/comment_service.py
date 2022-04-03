from commentapp.models import Comment


def create_comment(article_id, user_id, content):
    return Comment.objects.create(
        article_id=article_id,
        user_id=user_id,
        content=content
    )


def read_all_comment():
    return Comment.objects.all()


def update_comment(comment_id, content):

    target_comment = Comment.objects.get(id=comment_id)
    target_comment.content = content
    target_comment.save()


def delete_comment(comment_id):
    target_comment = Comment.objects.get(id=comment_id)
    target_comment.delete()
