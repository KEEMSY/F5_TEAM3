from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase

# Given
# When
# Then
# expect
from articleapp.models import Article, Category
from articleapp.services.service_article import create_article
from commentapp.models import  Comment
from commentapp.services.comment_service import (create_comment,
                                                 delete_comment,
                                                 update_comment)
from userapp.models import User


class TestView(TestCase):
    # comment 생성
    def test_create_comment(self):
        # Given
        user = User.objects.create(username='test_name', email='test@test.com')
        category = Category.objects.create(name='test_category')
        content = 'test'
        article = create_article('title', user, content, category, '')



        # When
        comment = create_comment(article.id, user.id, content)

        # expect
        self.assertIsNotNone(Comment.id)
        self.assertEqual(user.id, comment.user.id)
        self.assertEqual(article.id, comment.article.id)

    def test_when_create_comment_article_does_not_exist(self):
        # Given
        user = User.objects.create(username='test_name', email='test@test.com')
        article_id = 9999
        content = 'test'

        # Expect
        with self.assertRaises(IntegrityError):
            comment = create_comment(article_id, user.id, content)

    # comment 수정 시
    def test_update_target_comment(self):
        # Given
        user = User.objects.create(username='test_name', email='test@test.com')
        category = Category.objects.create(name='test_category')
        content = 'test'
        article = create_article('title', user, content, category, '')

        comment = create_comment(article.id, user.id, content)

        # When
        comment_id = comment.id
        update_content = 'update_Content!'
        update_comment(comment_id, update_content)

        # Expect
        comment = Comment.objects.get(id=comment_id)
        self.assertEqual(update_content, comment.content)

#     # comment 삭제 시
#     def test_comment_can_delete_by_deleting_article(self):
#         # Given
#         user = Author.objects.create(name="test_name")
#         article = Post.objects.create(title="test_title")
#         content = 'test'
#         comment = create_comment(article.id, user.id, content)
#
#         # When
#         article.delete()
#
#         # Expectdd
#         self.assertEqual(0, len(Comment.objects.all()))
#
#     def test_comment_can_delete_by_deleting_user(self):
#         # Given
#         user = Author.objects.create(name="test_name")
#         article = Post.objects.create(title="test_title")
#         content = 'test'
#         comment = create_comment(article.id, user.id, content)
#
#         # When
#         user.delete()
#
#         # Expectdd
#         self.assertEqual(0, len(Comment.objects.all()))
#
#     def test_comment_delete(self):
#         # Given
#         user = Author.objects.create(name="test_name")
#         article = Post.objects.create(title="test_title")
#         content = 'test'
#         comment = create_comment(article.id, user.id, content)
#
#         # When
#         delete_comment(comment.id)
#
#         # Expectdd
#         self.assertEqual(0, len(Comment.objects.all()))
#
#     def test_when_article_user_and_comment_are_deleteed_at_the_same_time(self):
#         # Given
#         user = Author.objects.create(name="test_name")
#         article = Post.objects.create(title="test_title")
#         content = 'test'
#         comment = create_comment(article.id, user.id, content)
#
#         # When
#         user.delete()
#         article.delete()
#
#         # Expect
#         with self.assertRaises(ObjectDoesNotExist):
#             delete_comment(comment.id)
