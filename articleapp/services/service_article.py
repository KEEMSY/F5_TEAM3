from articleapp.models import Article

def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)

#전체, 게시판 별로, 하나만 불러오기
def read_all_article():
    return Article.objects.all().order_by('-id')

def read_category_article(category):
    return Article.objects.filter(category)









