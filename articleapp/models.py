from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField()

class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=50)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.title





class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)    #unique=True로 설정하면 동일한 name을 갖는 카테고리를 또 만들 수 없다.
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
























# class Board(models.Model):
#     """
#         title: 제목
#         content: 내용
#         author: 작성자
#         like_count: 좋아요 카운트
#         pub_date: 배포일
#     """
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=500)
#     author = models.CharField(max_length=100)
#     like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
#     pub_date = models.DateTimeField()
#
#     def __str__(self):
#         return self.title
#
# class Reply(models.Model):
#     """
#         reply: Reply -> Board 연결관계
#         comment: 댓글내용
#         rep_date: 작성일
#     """
#     reply = models.ForeignKey(Board, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=200)
#     rep_date = models.DateTimeField()
#
#     def __str__(self):
#         return self.comment



