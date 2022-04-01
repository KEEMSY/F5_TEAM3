# from django.db import IntegrityError
# from django.test import TestCase
#
# from bookmarkapp.models import Bookmark
# from bookmarkapp.services.bookmark_service import do_bookmark, undo_bookmark
# from likeapp.models import Author, Post
#
#
# class TestBookmarkService(TestCase):
#     def test_a_user_can_bookmark_an_article(self) -> None:
#         # Given
#         user = Author.objects.create(name="test")
#         article = Post.objects.create(title="test_title")
#         # When
#         scrap = do_bookmark(user.id, article.id)
#
#         # Then
#         self.assertIsNotNone(scrap.id)
#         self.assertEqual(user.id, scrap.user_id)
#         self.assertEqual(article.id, scrap.article_id)
#
#     def test_a_user_can_bookmark_an_article_only_once(self) -> None:
#         # Given
#         user = Author.objects.create(name="test")
#         article = Post.objects.create(title="test_title")
#
#         # Expect
#         do_bookmark(user.id, article.id)
#         with self.assertRaises(IntegrityError):
#             do_bookmark(user.id, article.id)
#
#     def test_a_user_can_undo_bookmark(self) -> None:
#         # Given
#         user = Author.objects.create(name="test")
#         article = Post.objects.create(title="test_title")
#         scrap = do_bookmark(user_id=user.id, article_id=article.id)
#
#         # When
#         undo_bookmark(user.id, article.id)
#
#         # Then
#         with self.assertRaises(Bookmark.DoesNotExist):
#             Bookmark.objects.get(id=scrap.id)