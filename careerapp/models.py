from django.db import models

# Create your models here.



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
    news_date = models.CharField(max_length=30, blank=True)

    # writer = models.CharField(max_length=30)
    # info = models.CharField(max_length=500)
    # date = models.CharField(max_length=40)
    # from_site = models.CharField(max_length=40)
    # from_site_link = models.CharField(max_length=500)
