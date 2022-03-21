from django.shortcuts import render, redirect
from articleapp.models import Article

# Create your views here.
from likeapp.models import Author, ArticleLikes, CommentLikes
from likeapp.services.like_service import do_article_like, undo_article_like, do_comment_like, undo_comment_like


def click_article_like(request, article_id):
    user = request.user.is_authenticated
    if user:
        article = Article.objects.get(article_id=article_id)
        user_exist = Author.objects.get(user_id=request.user)
        like_post = ArticleLikes.objects.filter(article_id=article_id, user_id=user_exist)
        if request.method == 'POST':
            do_article_like(user_exist, article_id)
            article_like_count = article.articlelikes_set.count()
            return render(request, 'userapp/article.html',
                          {'article_like_count': article_like_count})
        elif request.method == 'DELETE':
            undo_article_like(user_exist, article_id)
            article_like_count = article.articlelikes_set.count()

            return render(request, 'userapp/article.html', {'article_like_count':article_like_count} )

    else:
        return redirect('/sign-in')


def click_comment_like(request, comment_id):
    user = request.user.is_authenticated
    if user:
        comment = Comment.objects.get(comment_id=comment_id)
        user_exist = Author.objects.get(user_id=request.user)
        like_post = CommentLikes.objects.filter(comment_id=comment_id, user_id=user_exist)
        if request.method == 'POST':
            do_article_like(user_exist, comment_id)
            comment_like_count = comment.commentlikes_set.count()
            return render(request, 'userapp/article.html',
                          {'comment_like_count': comment_like_count})
        elif request.method == 'DELETE':
            undo_article_like(user_exist, comment_id)
            article_like_count = comment.commentlikes_set.count()

            return render(request, 'userapp/article.html', {'comment_like_count':comment_like_count} )

    else:
        return redirect('/sign-in')




