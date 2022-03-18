from django.test import TestCase

# Given
# When
# Then
# expect
from commentapp.models import Comment, Author, Post
from commentapp.services.comment_service import create_comment, update_comment


class TestView(TestCase):

    def test_create_comment(self):
        # Given
        user = Author.objects.create(name="test_name")
        article = Post.objects.create(title="test_title")
        content = 'test'

        # When
        comment = create_comment(article, user, content)

        # expect
        self.assertIsNotNone(Comment.id)
        self.assertEqual(user.id, comment.user.id)
        self.assertEqual(article.id, comment.article.id)

    def test_update_target_comment(self):
        # Given
        user = Author.objects.create(name="test_name")
        article = Post.objects.create(title="test_title")
        content = 'test'
        comment = create_comment(article, user, content)

        # When
        comment_id = comment.id
        user_id = comment.user_id
        update_content = 'update_Content!'
        update_comment(comment_id, user_id, update_content)

        # Expect
        self.assertEqual(update_content, comment.content)
