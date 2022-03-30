from django.db import IntegrityError
from django.test import TestCase

from articleapp.models import Article
from likeapp.models import ArticleLikes, CommentLikes
from likeapp.services.like_service import (do_article_like, do_comment_like,
                                           undo_article_like,
                                           undo_comment_like)
from userapp.models import User
from articleapp.models import Article
from commentapp.models import Comment


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given
        user = User.objects.create(email="test")
        article = Article.objects.create(title="test_title")
        # When
        like = do_article_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(email="test")
        article = Article.objects.create(title="test_title")

        # Expect
        do_article_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            do_article_like(user.id, article.id)

    # def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
    #     # Given
    #     invalid_user_id = 9988
    #     article = Article.objects.create(title="test_title")
    #
    #     # Expect
    #     with self.assertRaises(IntegrityError):
    #         do_article_like(invalid_user_id, article.id)
    #
    # def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
    #     # Given
    #     user = Author.objects.create(email="test")
    #     invalid_article_id = 9988
    #
    #     # Expect
    #     with self.assertRaises(IntegrityError):
    #         do_article_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(email="test")
        article = Article.objects.create(title="test_title")

        # When
        do_article_like(user.id, article.id)

        # Then
        article = Article.objects.get(id=article.id)
        self.assertEqual(article.like_count, 1)

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = User.objects.create(email="test")
        article = Article.objects.create(title="test_title")
        like = do_article_like(user_id=user.id, article_id=article.id)

        # When
        undo_article_like(user.id, article.id)

        # Then
        with self.assertRaises(ArticleLikes.DoesNotExist):
            ArticleLikes.objects.get(id=like.id)

    # def test_it_should_raise_exception_when_undo_like_which_does_not_exist(self) -> None:
    #     # Given
    #     user = Author.objects.create(email="test")
    #     article = Post.objects.create(title="test_title")
    #
    #     # Expect
    #     with self.assertRaises(ArticleLikes.DoesNotExist):
    #         undo_article_like(user.id, article.id) #like를 select해야함


######################### comment #########################


class TestCommentLikeService(TestCase):
    def test_a_user_can_like_an_comment(self) -> None:
        # Given
        user = User.objects.create(email="test")
        comment = Comment.objects.create(comment="comment")
        # When
        like = do_comment_like(user.id, comment.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(comment.id, like.comment_id)

    def test_a_user_can_like_an_comment_only_once(self) -> None:
        # Given
        user = User.objects.create(email="test")
        comment = Comment.objects.create(comment="comment")

        # Expect
        do_comment_like(user.id, comment.id)
        with self.assertRaises(IntegrityError):
            do_comment_like(user.id, comment.id)

    # def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
    #     # Given
    #     invalid_user_id = 9988
    #     article = Article.objects.create(title="test_title")
    #
    #     # Expect
    #     with self.assertRaises(IntegrityError):
    #         do_article_like(invalid_user_id, article.id)
    #
    # def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
    #     # Given
    #     user = Author.objects.create(email="test")
    #     invalid_article_id = 9988
    #
    #     # Expect
    #     with self.assertRaises(IntegrityError):
    #         do_article_like(user.id, invalid_article_id)

    def test_comment_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(email="test")
        comment = Comment.objects.create(comment="comment")

        # When
        do_comment_like(user.id, comment.id)

        # Then
        comment = Comment.objects.get(id=comment.id)
        self.assertEqual(comment.like_count, 1)

    def test_a_user_can_undo_commentlike(self) -> None:
        # Given
        user = User.objects.create(email="test")
        comment = Comment.objects.create(comment="comment")
        like = do_comment_like(user_id=user.id, comment_id=comment.id)

        # When
        undo_comment_like(user.id, comment.id)

        # Then
        with self.assertRaises(CommentLikes.DoesNotExist):
            CommentLikes.objects.get(id=like.id)