from django.test import TestCase

# Given
# When
# Then
# expect
from commentapp.models import Comment
from commentapp.services.comment_service import create_comment, update_comment


class TestView(TestCase):

    def test_create_comment(self):
        # Given
        user = 'user1'
        article_id = 'article1'
        content = 'test'

        # When
        comment = create_comment(article_id, user, content)

        # expect
        self.assertIsNotNone(Comment.id)
        self.assertEqual('user1', comment.user_id)

    def test_update_target_comment(self):
        # Given
        user = 'user1'
        article = 'article1'
        content = 'test'
        comment = create_comment(article, user, content)

        # When
        comment_id = comment.id
        user_id = comment.user_id
        update_content = 'update_Content!'
        update_comment(comment_id, user_id, update_content)

        # Expect
        self.assertEqual(update_content, comment.content)
