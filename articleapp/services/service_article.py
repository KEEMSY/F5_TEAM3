
import datetime

from django.core.paginator import Paginator

from articleapp.models import Article, ArticleHits, Category
from userapp.models import User

"""
Service
1. article_CRUD
2. article_Hits
3. etc
"""

''' 1-1. C R E A T E '''


def create_article(title, user_id, content, category, img):
    return Article.objects.create(title=title, user=user_id, content=content, category=category, img=img)


''' 1-2. R E A D : QuerySet '''


def read_all_article():
    return Article.objects.all().order_by('-id')


def read_target_article(article_id):
    return Article.objects.get(pk=article_id)


def read_category_article(category):
    catetgory_id = Category.objects.get(name=category).id
    target_articles = Article.objects.filter(category=catetgory_id).order_by('-id')
    if len(target_articles) == 0:
        return False
    else:
        return target_articles


def read_article_by_title(title):
    return Article.objects.filter(title__icontains=title).order_by('-id')


def read_article_by_user(user_id):
    return Article.objects.filter(user=user_id).order_by('-id')


def read_article_containing_username(username):
    users = User.objects.filter(name__icontains=username).order_by('-id')

    article_list = []
    for user in users:
        article_list.append(read_article_by_user(user.id))
    try:
        article_queryset = article_list[0]
        for i in range(1, len(article_list)):
            article_queryset = article_queryset | article_list[i]

        return article_queryset
    except IndexError:
        return 0


def read_article_within_a_specific_period(date):
    return Article.objects.filter(created_at__gte=datetime.date.today() - datetime.timedelta(days=date)).order_by(
        '-created_at')


def read_article_containing_username_within_a_specific_period(date, name):
    before_article = read_article_containing_username(name)
    if before_article:
        return before_article.filter(created_at__gte=datetime.date.today() - datetime.timedelta(days=date))
    else:
        return 0


def read_article_by_title_within_a_specific_period(date, title):
    target_articles = Article.objects.filter(
        created_at__gte=datetime.date.today() - datetime.timedelta(days=date)).filter(
        title__icontains=title).order_by('-id')
    if len(target_articles):
        return target_articles
    else:
        return 0


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


''' 3. etc '''


def get_page_context(articles, page):
    paginator = Paginator(articles, 10)
    board_list = paginator.get_page(page)
    return board_list

