# Given
# When
# Then
# expect
import self as self
from django.test import TestCase
from articleapp.models import Article, Author
from articleapp.services.service_article import create_article, read_all_article


class TestView(TestCase):
    def test_create_article(self):

        # Given
        user=Author.objects.create(name='test')
        title='test_title'
        content='test_content'
        category='test_category'

        # When
        article=create_article(title,user,content,category)

        # expect
        self.assertIsNotNone(Article.id)
        self.assertEqual(user.id,article.id)

    def test_read_all_article(self):
        # Given
        user=Author.objects.create(name='test')

        # When
        article1 = create_article('title', user, 'content', 'category1')
        article2 = create_article('title', user, 'content', 'category2')
        article3 = create_article('title', user, 'content', 'category3')

        # Then
        article_list = read_all_article().values()
        latest_article_list = [article3, article2, article1]

        # expect
        self.assertEqual(len(article_list), 3)
        for idx in range(len(article_list)):
            self.assertEqual(article_list[idx]['category'], latest_article_list[idx].category)






