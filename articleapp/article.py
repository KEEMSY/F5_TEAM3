from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from articleapp.models import Article

# from articleapp.services.service_article import article_delete, article_category_read, article_create, article_update, article_user_search



#게시글 목록
# def article_read(request):
#     all_Articles = Article.objects.all().order_by("-created_at") # 모든 데이터 조회, 내림차순(-표시) 조회
#     return render(request, 'community.html', {'title':'Article List', 'Article_list':all_Articles})
#
# def detail_read(request, Article_id):
#     feed = Article.objects.get(id=Article_id)
#     return render(request, 'detail.html', {'feed': feed})
#
# def move_to_write(request):
#     return render(request, 'new.html')
#
# def write_Article(request):
#     b = Article(title=request.POST['title'], content=request.POST['detail'], user="Kang", created_at=timezone.now())
#     b.save()
#     return HttpResponseRedirect(reverse('articleapp:home'))
#


#together

# class TestView(TestCase):
#
#     def article_create(self):
#         # Given   ##title = 'test_title' 제목 입력
#         title = 'test_title'
#
#         # When   ##article = article_create 하는데 title(제목) 필요 title = 'test_title'
#                  ##article의 type 출력 (article = article_create ())
#
#         article = article_create(title, 'user', 'category')
#         print(type(article))
#
#         # expect  ##article.title, title 이 두 개가 같을 것이다.
#         self.assertEqual(article.title, title)
#
#     def article_user_search(self):
#         # Given   ##user1이 있음
#         user1 = 'user1'
#
#         # When   ##category,2,3,4에 맞는 title '검색'
#         article_create('title', user1, 'category')
#         article_create('title1', user1, 'category')
#         article_create('title2', user1, 'category')
#
#         article_create('title3', user1, 'category2')
#         article_create('title4', user1, 'category3')
#         article_create('title5', user1, 'category4')
#
#         # expect   ##user1이 원하는 article_user_search 출력, 그 값 길이가 6과 같을 것이다.
#         print(article_user_search(user1))
#         self.assertEqual(len(article_user_search(user1)), 6)
#
#     def article_category_read(self):   ##article main page
#         # Given   ## user1이 category1,2,3 읽어옴
#         category1 = 'category1'
#         category2 = 'category2'
#         category3 = 'category3'
#
#         user1 = 'user1'
#
#         # When    ##user1이 category 따라 각각 title 가져옴
#         article_create('title', user1, category1)
#
#         article_create('title2', user1, category2)
#         article_create('title2', user1, category2)
#
#         article_create('title3', user1, category3)
#         article_create('title3', user1, category3)
#         article_create('title3', user1, category3)
#
#         # Then    ##category 따라 각각의 article 가져옴
#         category1_read = article_category_read(category1)
#         category2_read = article_category_read(category2)
#         category3_read = article_category_read(category3)
#
#         # expect   ##읽어온 자료의 객체 갯수 만큼 길이가 보여질 것이다.
#         self.assertEqual(1, len(category1_read))
#         self.assertEqual(2, len(category2_read))
#         self.assertEqual(3, len(category3_read))


    #alone
    # def article_update(self):
    #     # Given  ##user1이 있음
    #
    #     user1 = 'user1'
    #
    #     # When   ##하나의 article 갱신 필요
    #     article_update(user1)
    #
    #     # Then   ##title, category 맞는 하나의 article 갱신
    #     article_update(title, user1, category1)
    #
    #     # expect ##갱신 전 Ccategory1의 길이와 같아짐
    #     self.assertEqual(1, len(category1))

    # def article_delete(self):
    #     # Given  ##user1이 있음
    #
    #     user1 = 'user1'
    #
    #     # When   ##user1이 게시글 삭제 필요
    #     article_delete(user1)
    #
    #     # Then   ## title, category2 맞는 하나의 article 삭제
    #     article_delete('title', user1, category1)
    #
    #     # expect ## category2 길이가 1이 됨
    #     self.assertEqual(1, len(category1))
