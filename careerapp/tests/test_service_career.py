#
# # Given
# # When
# # Then
# # expect
# from django.test import TestCase
#
# from careerapp.models import Career, Author #테스트 유저정보
# from careerapp.services.service_career import show_career_info_by_skills
#
#
# class TestView(TestCase):
#     def test_career_load(self):
#         # Given
#         user_skill1 = Author.objects.create(skill='C#')  # 로그인한 유저의 정보
#         user_skill2 = Author.objects.create(skill='Python')
#         request = Career.objects.create(skills='C#')
#         # When
#
#         render = show_career_info_by_skills(request, user_skill2)
#         print(render)
#         # Then
#         # expect
#
#         self.assertIsNotNone(render)
#
#
#         return 0