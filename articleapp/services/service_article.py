from articleapp.models import Article

# create
def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)

# read : QuerySet
def read_all_article():
    return Article.objects.all().order_by('-id')

def read_category_article(category):
    return Article.objects.filter(category=category)

def read_article_by_title(title):
    return Article.objects.filter(title=title)

def read_article_by_user(user_id):
    return Article.objects.filter(user=user_id)
