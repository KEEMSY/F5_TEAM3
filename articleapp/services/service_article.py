import datetime

from articleapp.models import Article, ArticleHits, Author

"""
Service
1. article_CRUD
2. article_Hits
"""

''' 1-1. C R E A T E '''


def create_article(title, user_id, content, category):
    return Article.objects.create(title=title, user=user_id, content=content, category=category)


''' 1-2. R E A D : QuerySet '''


def read_all_article():
    return Article.objects.all().order_by('-id')


def read_target_article(article_id):
    return Article.objects.get(pk=article_id)


def read_category_article(category):
    return Article.objects.filter(category=category).order_by('-id')


def read_article_by_title(title):
    return Article.objects.filter(title__icontains=title).order_by('-id')


def read_article_by_user(user_id):
    return Article.objects.filter(user=user_id).order_by('-id')


def read_article_containing_username(username):
    users = Author.objects.filter(name__icontains=username).order_by('-id')

    article_list = []
    for user in users:
        article_list.append(read_article_by_user(user.id))

    article_queryset = article_list[0]
    for i in range(1, len(article_list)):
        article_queryset = article_queryset | article_list[i]

    return article_queryset


def read_article_within_a_specific_period(date):
    return Article.objects.filter(created_at__gte=datetime.date.today() - datetime.timedelta(days=date))


def read_article_containing_username_within_a_specific_period(date, name):
    before_article = read_article_containing_username(name)
    return before_article.filter(created_at__gte=datetime.date.today() - datetime.timedelta(days=date))


def read_article_by_title_within_a_specific_period(date, title):
    return Article.objects.filter(created_at__gte=datetime.date.today() - datetime.timedelta(days=date)).filter(
        title=title)


''' 1-3. U P D A T E '''


def update_article(article_id, content):
    target_article = Article.objects.get(pk=article_id)
    target_article.content = content
    target_article.save()


''' 1-4. D E L E T E '''


def delete_article(article_id):
    target_article = Article.objects.get(pk=article_id)
    target_article.delete()


''' 2. Hits '''


def get_client_ip(request):
    raw_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if raw_ip:
        target_ip = raw_ip.split(',')[0]
    else:
        target_ip = request.META.get('REMOTE_ADDR')
    return target_ip


def hit_article(ip, article_id):
    target_article = Article.objects.get(pk=article_id)

    if not ArticleHits.objects.filter(client_ip=ip, article=article_id):
        target_article.article_hits += 1
        target_article.save()

        ArticleHits.objects.create(client_ip=ip, article_id=article_id)

    return Article.objects.get(pk=article_id)
