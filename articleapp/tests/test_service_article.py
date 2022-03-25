# Given
# When
# Then
# expect
import self as self
from django.test import TestCase
from articleapp.models import Article, Author
from articleapp.services.service_article import create_article, read_all_article, read_category_article, read_article ,update_article


class TestView(TestCase):
    def test_create_article(self):

        # Given
        user=Author.objects.create(name='test')
        title='test_title'
        content='test_content'
        category='test_category'

        # When
        article=create_article(user,title,content,category)

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

    def test_read_category_article(self):
        # Given
        user = Author.objects.create(name="test")

        article1 = create_article("title", user, "content", "category1")

        article2 = create_article("title", user, "content", "category2")
        article3 = create_article("title", user, "content", "category2")

        article4 = create_article("title", user, "content", "category3")
        article5 = create_article("title", user, "content", "category3")
        article6 = create_article("title", user, "content", "category3")

        # When
        article_1_list = read_category_article('category1')
        article_2_list = read_category_article('category2')
        article_3_list = read_category_article('category3')

        # expect
        self.assertEqual(1, len(article_1_list))
        self.assertEqual(2, len(article_2_list))
        self.assertEqual(3, len(article_3_list))

    def test_read_article(self):
        # Given
        user = Author.objects.create(name="test")

        # When
        article = create_article("title", user, "content", "category")
        read_article()

        # expect
        self.assertIsNotNone(article.id)
        self.assertEqual(user.id, article.id)

    # def test_update_article(self):
    #     # Given
    #     user = Author.objects.create(name="test")
    #
    #     # When
    #     article = create_article("title", user, "content", "category")
    #     edit = update_article("title", user, "content", "category")
    #
    #     # expect
    #     self.assertIsNotNone(article, update_article)
    #     self.assertNotEqual(article, update_article)
    #
    #



