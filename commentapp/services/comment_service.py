from commentapp.models import Comment


def create_comment(article, user, content):
    return Comment.objects.create(
        article=article,
        user=user,
        content=content
    )


def update_comment(user_id, comment_id, content):
    target_comment = Comment.objects.get(id=comment_id)
    target_comment.content = content
    target_comment.save()
