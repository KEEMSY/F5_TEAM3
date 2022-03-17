from commentapp.models import Comment


def create_comment(article_id, user_id, content):
    return Comment.objects.create(
        article_id=article_id,
        user_id=user_id,
        content=content
    )
