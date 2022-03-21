from django.db import IntegrityError
from django.test import TestCase

from likeapp.models import ArticleLikes
from likeapp.models import CommentLikes
from articleapp.models import Article
from likeapp.models import Author
from likeapp.services.like_service import do_article_like, undo_article_like
from likeapp.services.like_service import do_comment_like, undo_comment_like

class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given
        user = Author.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_article_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = Author.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        do_article_like(user.id, article.id)
        with self.assertRaises(Exception):
            do_article_like(user.id, article.id)




    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Expect
        with self.assertRaises(IntegrityError):
            do_article_like(invalid_user_id, article.id)

    def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
        # Given
        user = Author.objects.create(name="test")
        invalid_article_id = 9988

        # Expect
        with self.assertRaises(IntegrityError):
            do_article_like(user.id, invalid_article_id)


    def test_like_count_should_increase(self) -> None:
        # Given
        user = Author.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        do_article_like(user.id, article.id)

        # Then
        article = Article.objects.get(id=article.id)
        self.assertEqual(1, article.articlelikes_set.count())

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = Author.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = do_article_like(user_id=user.id, article_id=article.id)

        # When
        undo_article_like(user.id, article.id)

        # Then
        with self.assertRaises(ArticleLikes.DoesNotExist):
            ArticleLikes.objects.get(id=like.id)


    def test_it_should_raise_exception_when_undo_like_which_does_not_exist(self) -> None:
        # Given
        user = Author.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        with self.assertRaises(ArticleLikes.DoesNotExist):
            undo_article_like(user.id, article.id)