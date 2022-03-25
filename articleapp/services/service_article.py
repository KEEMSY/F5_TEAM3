from articleapp.models import Article, Author


# create
def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)


# read : QuerySet
def read_all_article():
    return Article.objects.all().order_by('-id')


def read_category_article(category):
    return Article.objects.filter(category=category)

# 입력한 타이틀을 포함하는 모든 게시글을 모두 보여주도록 수정해야함
def read_article_by_title(title):
    return Article.objects.filter(title__icontains=title).order_by('-id')


def read_article_by_user(user_id):
    return Article.objects.filter(user=user_id).order_by('-id')


def read_article_containing_username(name):
    users = Author.objects.filter(name__icontains=name)

    article_list = []
    for user in users:
        article_list.append(read_article_by_user(user.id))

    article_queryset = article_list[0]
    for i in range(1, len(article_list)):
        article_queryset = article_queryset | article_list[i]

    return article_queryset
