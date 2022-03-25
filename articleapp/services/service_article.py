from articleapp.models import Article

def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)

def read_all_article():
    return Article.objects.all().order_by('-id')

def read_category_article(category):
    return Article.objects.filter(category=category)

def read_article(title):
    return Article.objects.get(title=title)

# def update_article(content):
#     return Article.objects.update(content=content)
#
# def delete_article(article_id):
#     return Article.objects.delete(article_id=article_id)

