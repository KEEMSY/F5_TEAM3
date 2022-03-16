# Given
# When
# Then
# expect
from django.test import TestCase
from articleapp.models import Article
from articleapp.services.service_article import article_create, article_user_search, article_category_read, article_update, article_delete


class TestView(TestCase):

    def test_article_create(self):
        # Given   ##title = 'test_title' 제목 입력
        title = 'test_title'

        # When   ##article = article_create 하는데 title(제목) 필요 title = 'test_title'
                 ##article의 type 출력 (article = article_create ())

        article = article_create(title, 'user', 'category')
        print(type(article))

        # expect  ##article.title, title 이 두 개가 같을 것이다.
        self.assertEqual(article.title, title)

    def test_article_user_search(self):
        # Given   ##user1이 있음
        user1 = 'user1'

        # When   ##category,2,3,4에 맞는 title '검색'
        article_create('title', user1, 'category')
        article_create('title1', user1, 'category')
        article_create('title2', user1, 'category')

        article_create('title3', user1, 'category2')
        article_create('title4', user1, 'category3')
        article_create('title5', user1, 'category4')

        # expect   ##user1이 원하는 article_user_search 출력, 그 값 길이가 6과 같을 것이다.
        print(article_user_search(user1))
        self.assertEqual(len(article_user_search(user1)), 6)

    def test_article_category_read(self):   ##article main page
        # Given   ## user1이 category1,2,3 읽어옴
        category1 = 'category1'
        category2 = 'category2'
        category3 = 'category3'

        user1 = 'user1'


        # When    ##user1이 category 따라 각각 title 가져옴
        article_create('title', user1, category1)

        article_create('title2', user1, category2)
        article_create('title2', user1, category2)

        article_create('title3', user1, category3)
        article_create('title3', user1, category3)
        article_create('title3', user1, category3)


        # Then    ##category 따라 각각의 article 가져옴
        category1_read = article_category_read(category1)
        category2_read = article_category_read(category2)
        category3_read = article_category_read(category3)


        # expect   ##읽어온 자료의 객체 갯수 만큼 길이가 보여질 것이다.
        self.assertEqual(1, len(category1_read))
        self.assertEqual(2, len(category2_read))
        self.assertEqual(3, len(category3_read))

    def test_article_update(self):
        # Given  ##user1이 있음

        user1 = 'user1'


        # When   ##하나의 article 갱신 필요
        article_update('title', user1, 'category')

        # Then

        article_create('title', user1, category1)


        # expect

    def test_article_delete(self):
        # Given

        # When

        # Then

        # expect