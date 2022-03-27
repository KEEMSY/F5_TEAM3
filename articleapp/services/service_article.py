from articleapp.models import Article, Author

''' C R E A T E '''


def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)


''' R E A D : QuerySet '''


def read_all_article():
    return Article.objects.all().order_by('-id')


def read_category_article(category):
    return Article.objects.filter(category=category)



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


''' U P D A T E '''


def update_article(article_id, content):
    target_article = Article.objects.get(pk=article_id)
    target_article.content = content
    target_article.save()


''' D E L E T E '''


def delete_article(article_id):
    target_article = Article.objects.get(pk=article_id)
    target_article.delete()
