# Given
# When
# Then
# expect
import self as self
from django.test import TestCase
from articleapp.models import Article, Author
from articleapp.services.service_article import create_article

#together



class TestView(TestCase):
    def test_create_article(self):

        # Given
        user=Author.objects.create(name='test')
        title='test_title'
        content='test_content'
        category='test_category'

        # When
        article=create_article(title,user,content,category)

        # Then

        # expect
        self.assertIsNotNone(Article.id)
        self.assertEqual(user.id,article.id)








