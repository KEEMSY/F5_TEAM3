from articleapp.models import Article

def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)

