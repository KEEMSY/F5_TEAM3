# Given
# When
# Then
# expect
from django.test import TestCase

from articleapp.models import Article
from articleapp.services.service_article import (article_category_read,
                                                 article_create,
                                                 article_user_search)


class TestView(TestCase):

    def test_article_create(self):
        # Given
        title = 'test_title'

        # When
        article = article_create(title, 'user', 'category')
        print(type(article))

        # expect
        self.assertEqual(article.title, title)

    def test_article_user_search(self):
        # Given
        user1 = 'user1'

        # When
        article_create('title', user1, 'category')
        article_create('title1', user1, 'category')
        article_create('title2', user1, 'category')

        article_create('title3', user1, 'category2')
        article_create('title4', user1, 'category3')
        article_create('title5', user1, 'category4')

        # expect
        print(article_user_search(user1))
        self.assertEqual(len(article_user_search(user1)), 6)

    def test_article_category_read(self):
        # Given
        category1 = 'category1'
        category2 = 'category2'
        category3 = 'category3'

        user1 = 'user1'

        # When
        article_create('title',user1,category1)

        article_create('title2',user1,category2)
        article_create('title2',user1,category2)

        article_create('title3',user1,category3)
        article_create('title3',user1,category3)
        article_create('title3',user1,category3)


        # Then
        category1_read = article_category_read(category1)
        category2_read = article_category_read(category2)
        category3_read = article_category_read(category3)


        # expect
        self.assertEqual(1, len(category1_read))
        self.assertEqual(2, len(category2_read))
        self.assertEqual(3, len(category3_read))
