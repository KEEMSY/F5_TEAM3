from django.test import TestCase


# Given
# When
# Then
# expect
from commentapp.services.comment_service import create_comment


class TestView(TestCase):

    def test_create_comment(self):
        # Given
        user = 'user1'
        article = 'article1'
        content = 'test'

        # When
        comment = create_comment(article, user, content)

        # expect
        self.assertEqual('user1', comment.user_id)


