from django.db import models


# Create your models here.

# 테스트를 위해 유저모델 작성 머지하고 위에 임포트해서 가져와야합니다.
class Author(models.Model):
    name = models.CharField(max_length=40)
    skill = models.CharField(max_length=40, default='Python')


#
class Career(models.Model):
    class Meta:
        db_table = "rocketpunch"

    logo = models.CharField(max_length=600, default='')
    name = models.CharField(max_length=100, default='')
    tabom = models.CharField(max_length=100, default='')
    desc = models.CharField(max_length=600, default='')
    work = models.CharField(max_length=600, default='')
    link = models.CharField(max_length=600, default='')
    w_desc = models.CharField(max_length=600, default='')
    info = models.CharField(max_length=500, default='')
    date = models.CharField(max_length=40, default='')
    recruit_site = models.CharField(max_length=40)
    skills = models.CharField(max_length=40, default='Python')


# 로켓펀치 skills 크롤링에 담기는 내역
# skills = [Android,iOS,C++,C#,Java,PHP,Python,Ruby,JSP,Node.js,AngularJS,jQuery,ASP.NET]

class News(models.Model):
    class Meta:
        db_table = "itnews"

    news_pic = models.CharField(max_length=600)
    news_title = models.CharField(max_length=100)
    # tabom = models.CharField(max_length=100)
    news_desc = models.TextField(null=True)
    news_link = models.CharField(max_length=600)

    # w_desc = models.CharField(max_length=600)
    # info = models.CharField(max_length=500)
    # date = models.CharField(max_length=40)
    # recruit_site = models.CharField(max_length=40)
    # skills = models.CharField(max_length=40)
