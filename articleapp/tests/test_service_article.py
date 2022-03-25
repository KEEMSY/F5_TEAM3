# Given
# When
# Then
# Expect

from django.test import TestCase
from articleapp.models import Article, Author
from articleapp.services.service_article import create_article, read_all_article, \
    read_category_article, read_article_by_title, read_article_by_user, read_article_containing_username


class TestView(TestCase):
    ''' C R E A T E '''

    def test_create_article(self):
        # Given
        user = Author.objects.create(name='test')
        title = 'test_title'
        content = 'test_content'
        category = 'test_category'

        # When
        article = create_article(title, user, content, category)

        # expect
        self.assertIsNotNone(Article.id)
        self.assertEqual(user.id, article.id)

    ''' R E A D '''

    def test_read_all_article(self):
        # Given
        user = Author.objects.create(name='test')

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

    def test_read_article_by_title(self):
        # Given
        user = Author.objects.create(name="test")
        article1 = create_article("title", user, "content", "category1")
        article2 = create_article("title", user, "content", "category2")

        # When
        target_articles = read_article_by_title("title")

        # Expect
        self.assertEqual(2, len(target_articles))

    def test_read_article_by_user(self):
        user1 = Author.objects.create(name="test1")
        article1 = create_article("title_1", user1, "content", "category1")
        user2 = Author.objects.create(name="test2")
        article2 = create_article("title_2", user2, "content", "category2")

        # When
        article_by_user1 = read_article_by_user(user1.id).get()
        article_by_user2 = read_article_by_user(user2.id).get()

        # Expect
        self.assertEqual("title_1", article_by_user1.title)
        self.assertEqual("title_2", article_by_user2.title)


    def test_read_articles_by_user(self):
        user1 = Author.objects.create(name="test1")
        article1 = create_article("title_1", user1, "content", "category1")
        article2 = create_article("title_2", user1, "content", "category1")

        # When
        article_by_user1 = read_article_by_user(user1.id)

        # Expect
        expect_title = ["title_1", "title_2"]
        for i in range(len(article_by_user1)):
            self.assertEqual(expect_title[i], article_by_user1[i].title)

    def test_read_article_containing_username(self):
        # Given
        user1 = Author.objects.create(name="test1")
        article1_1 = create_article("title_1", user1, "content", "category1")

        user2 = Author.objects.create(name="test2")
        article2_1 = create_article("title_2", user2, "content", "category2")
        article2_2 = create_article("title_3", user2, "content", "category2")

        # When
        article_list = read_article_containing_username('test')

        # Expeect
        self.assertEqual(3, len(article_list))