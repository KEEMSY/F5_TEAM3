# # Given
# # When
# # Then
# # Expect
# import datetime
#
# from django.core.exceptions import ObjectDoesNotExist
# from django.test import TestCase
#
# from articleapp.models import Article, Author, Category
# from articleapp.services.service_article import (
#     create_article, delete_article, read_all_article, read_article_by_title,
#     read_article_by_title_within_a_specific_period, read_article_by_user,
#     read_article_containing_username,
#     read_article_containing_username_within_a_specific_period,
#     read_article_within_a_specific_period, read_category_article,
#     read_target_article, update_article)
#
#
# class TestView(TestCase):
#     """ C R E A T E """
#
#     def test_create_article(self):
#         # Given
#         user = Author.objects.create(name='test')
#         title = 'test_title'
#         content = 'content'
#         category = Category.objects.create(name='test_category')
#         img = ''
#
#         # When
#         article = create_article(title, user, content, category, img)
#
#         # expect
#         self.assertIsNotNone(Article.id)
#         self.assertEqual(user.id, article.id)
#
#     def test_when_there_is_not_enough_argument(self):
#         # Given
#         user = Author.objects.create(name='test')
#         title = 'test_title'
#         content = 'content'
#         category = Category.objects.create(name='test_category')
#
#         # Expect
#         with self.assertRaises(TypeError):
#             article = create_article(title, user, content, category)
#
#     ''' R E A D '''
#
#     def test_when_article_does_not_exist(self):
#         # Given
#         user = Author.objects.create(name='test')
#         category = Category.objects.create(name='test_category')
#         article1 = create_article('title', user, 'content', category, '')
#         target_id = article1.id
#         article1.delete()
#
#         # Expect
#         with self.assertRaises(ObjectDoesNotExist):
#             target_article = read_target_article(target_id)
#
#     def test_read_all_article(self):
#         # Given
#         user = Author.objects.create(name='test')
#         category = Category.objects.create(name='test_category')
#
#         # When
#         article1 = create_article('title', user, 'content', category, '')
#         article2 = create_article('title', user, 'content', category, '')
#         article3 = create_article('title', user, 'content', category, '')
#
#         # Then
#         article_list = read_all_article().values()
#         latest_article_list = [article3, article2, article1]
#
#         # expect
#         self.assertEqual(len(article_list), 3)
#         for idx in range(len(article_list)):
#             self.assertEqual(article_list[idx]['content'], latest_article_list[idx].content)
#
#     def test_read_category_article(self):
#         # Given
#         user = Author.objects.create(name="test")
#         category_1 = Category.objects.create(name='test_category1')
#         category_2 = Category.objects.create(name='test_category2')
#         category_3 = Category.objects.create(name='test_category3')
#
#         article1 = create_article("title", user, "content", category_1, '')
#
#         article2 = create_article("title", user, "content", category_2, '')
#         article3 = create_article("title", user, "content", category_2, '')
#
#         article4 = create_article("title", user, "content", category_3, '')
#         article5 = create_article("title", user, "content", category_3, '')
#         article6 = create_article("title", user, "content", category_3, '')
#
#         # When
#         article_1_list = read_category_article(category_1.name)
#         article_2_list = read_category_article(category_2.name)
#         article_3_list = read_category_article(category_3.name)
#
#         # expect
#         self.assertEqual(1, len(article_1_list))
#         self.assertEqual(2, len(article_2_list))
#         self.assertEqual(3, len(article_3_list))
#
#     def test_read_article_by_title(self):
#         # Given
#         user = Author.objects.create(name="test")
#         category = Category.objects.create(name='test_category')
#
#         article1 = create_article("title", user, "content", category, '')
#         article2 = create_article("title2", user, "content", category, '')
#         article2 = create_article("title2_2", user, "content", category, '')
#
#         # When
#         target_articles = read_article_by_title("title")
#
#         # Expect
#         self.assertEqual(3, len(target_articles))
#
#     def test_read_article_by_user(self):
#         user1 = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article1 = create_article("title_1", user1, "content", category, '')
#         user2 = Author.objects.create(name="test2")
#         article2 = create_article("title_2", user2, "content", category, '')
#
#         # When
#         article_by_user1 = read_article_by_user(user1.id).get()
#         article_by_user2 = read_article_by_user(user2.id).get()
#
#         # Expect
#         self.assertEqual("title_1", article_by_user1.title)
#         self.assertEqual("title_2", article_by_user2.title)
#
#     def test_read_articles_by_user(self):
#         user1 = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article1 = create_article("title_1", user1, "content", category, '')
#         article2 = create_article("title_2", user1, "content", category, '')
#
#         # When
#         article_by_user1 = read_article_by_user(user1.id)
#
#         # Expect
#         expect_title = ["title_2", "title_1"]
#         for i in range(len(article_by_user1)):
#             self.assertEqual(expect_title[i], article_by_user1[i].title)
#
#     def test_read_article_containing_username(self):
#         # Given
#         user1 = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article1_1 = create_article("title_1", user1, "content", category, '')
#
#         user2 = Author.objects.create(name="test2")
#         article2_1 = create_article("title_2", user2, "content", category, '')
#         article2_2 = create_article("title_3", user2, "content", category, '')
#
#         # When
#         article_list = read_article_containing_username('test')
#
#         # Expeect
#         self.assertEqual(3, len(article_list))
#
#     def test_read_article_within_a_specific_period(self):
#         # Given
#         user1 = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article1 = create_article("title_day", user1, "content", category, '')
#         article1_1 = create_article("title_one_day", user1, "content", category, '')
#         article1_2 = create_article("title_one_week", user1, "content", category, '')
#         article1_3 = create_article("title_one_month", user1, "content", category, '')
#         article1_4 = create_article("title_six_month", user1, "content", category, '')
#         article1_5 = create_article("title_one_year", user1, "content", category, '')
#
#         article1_1.created_at = datetime.date.today() - datetime.timedelta(days=1)
#         article1_1.save()
#
#         article1_2.created_at = datetime.date.today() - datetime.timedelta(days=7)
#         article1_2.save()
#
#         article1_3.created_at = datetime.date.today() - datetime.timedelta(days=30)
#         article1_3.save()
#
#         article1_4.created_at = datetime.date.today() - datetime.timedelta(days=180)
#         article1_4.save()
#
#         article1_5.created_at = datetime.date.today() - datetime.timedelta(days=365)
#         article1_5.save()
#
#         # When
#         within_one_day = read_article_within_a_specific_period(1)
#         within_one_week = read_article_within_a_specific_period(7)
#         within_one_month = read_article_within_a_specific_period(30)
#         within_six_month = read_article_within_a_specific_period(180)
#         within_one_year = read_article_within_a_specific_period(365)
#
#         # Expect
#         self.assertEqual(2, len(within_one_day))
#         self.assertEqual(3, len(within_one_week))
#         self.assertEqual(4, len(within_one_month))
#         self.assertEqual(5, len(within_six_month))
#         self.assertEqual(6, len(within_one_year))
#
#         self.assertEqual("title_day", within_one_day[0].title)
#
#     def test_read_article_containing_username_within_a_specific_period(self):
#         # Given
#         user1 = Author.objects.create(name="test1")
#         user2 = Author.objects.create(name="test2")
#         category = Category.objects.create(name='test_category')
#
#         article1_1 = create_article("title_one_day", user1, "content", category, '')
#         article1_2 = create_article("title_one_week", user2, "content", category, '')
#
#         article1_1.created_at = datetime.date.today() - datetime.timedelta(days=1)
#         article1_1.save()
#
#         article1_2.created_at = datetime.date.today() - datetime.timedelta(days=7)
#         article1_2.save()
#
#         # When
#         within_one_day_username = read_article_containing_username_within_a_specific_period(1, 'test')
#         within_one_week_username = read_article_containing_username_within_a_specific_period(7, 'test')
#
#         # Expect
#         self.assertEqual('test1', within_one_day_username[0].user.name)
#         self.assertEqual('test2', within_one_week_username[0].user.name)
#         self.assertEqual('test1', within_one_week_username[1].user.name)
#
#     def test_when_article_can_not_read_article_containing_username_within_a_specific_period(self):
#         # Given
#         user1 = Author.objects.create(name="test1")
#         user2 = Author.objects.create(name="test2")
#         category = Category.objects.create(name='test_category')
#
#         article1_1 = create_article("title_one_day", user1, "content", category, '')
#         article1_2 = create_article("title_one_week", user2, "content", category, '')
#
#         # When
#         within_one_week_username = read_article_containing_username_within_a_specific_period(7, 'abc')
#
#         # Expect
#         self.assertEqual(False, within_one_week_username)
#
#     def test_read_article_containing_title_within_a_specific_period(self):
#         # Given
#         user1 = Author.objects.create(name="test1")
#         user2 = Author.objects.create(name="test2")
#         category = Category.objects.create(name='test_category')
#
#         article1_1 = create_article("title_one_day", user1, "content", category, '')
#         article1_2 = create_article("title_one_week", user2, "content", category, '')
#
#         article1_1.created_at = datetime.date.today() - datetime.timedelta(days=1)
#         article1_1.save()
#
#         article1_2.created_at = datetime.date.today() - datetime.timedelta(days=7)
#         article1_2.save()
#
#         # When
#         within_one_day_title = read_article_by_title_within_a_specific_period(1, 'title_one_day')
#         within_one_week_title = read_article_by_title_within_a_specific_period(7, 'title_one')
#
#         # Expect
#         self.assertEqual('title_one_day', within_one_day_title[0].title)
#         self.assertEqual('title_one_week', within_one_week_title[0].title)
#         self.assertEqual('title_one_day', within_one_week_title[1].title)
#
#     def test_when_article_can_not_read_article_by_title_within_a_specific_period(self):
#         # Given
#         user1 = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article1_1 = create_article("title_one_day", user1, "content", category, '')
#         article1_2 = create_article("title_one_week", user1, "content", category, '')
#
#         # When
#         within_one_week_title = read_article_by_title_within_a_specific_period(7, 'abc')
#
#         # Expect
#         self.assertEqual(False, within_one_week_title)
#
#     ''' U P D A T E '''
#
#     def test_update_article(self):
#         # Given
#         user = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#         article = create_article("title", user, "before_content", category, '')
#
#         # When
#         update_article(article.id, 'after content')
#
#         # Expect
#         check_article = Article.objects.get(pk=article.id)
#         self.assertEqual(check_article.content, 'after content')
#
#     def test_when_article_does_not_exist(self):
#         # Given
#         user = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article = create_article("title", user, "before_content", category, '')
#
#         # When
#         article = Article.objects.get(pk=article.id)
#         article.delete()
#
#         # Expect
#         with self.assertRaises(ObjectDoesNotExist):
#             update_article(article.id, 'after content')
#
#     ''' D E L E T E '''
#
#     def test_delete_article(self):
#         # Given
#         user = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article = create_article("title", user, "before_content", category, '')
#
#         # When
#         delete_article(article.id)
#
#         # Expect
#         self.assertEqual(0, len(Article.objects.all()))
#
#     def test_when_article_delete_twice(self):
#         # Given
#         user = Author.objects.create(name="test1")
#         category = Category.objects.create(name='test_category')
#
#         article = create_article("title", user, "before_content", category, '')
#
#         # When
#         delete_article(article.id)
#
#         # Expect
#         with self.assertRaises(ObjectDoesNotExist):
#             delete_article(article.id)
