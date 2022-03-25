"""TEAM3_F5_coFI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from TEAM3_F5_coFI import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/', include("userapp.urls")),
    path("", include("likeapp.urls")),
    path('', views.show_home, name='home'),
    path('communities/', include("articleapp.urls")),
    path('careers/', include("careerapp.urls")),
    path("articles/", include("bookmarkapp.urls")),
    path('accounts/', include('allauth.urls')),
    path('google/', include('allauth.urls')),

    #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
  
]

#Django에서는 정적 파일을 static file과 media file로 구분한다.
#static file은 웹 서비스에 제공하기 위해 준비한 정적 파일이고, media file은 웹 서비스 사용자가 서버에 업로드하는 정적 파일이다.
#지금 단계에서는 사용자가 자신의 프로필 사진을 업로드할 수 있도록 만들 것이기 때문에 이는 media file에 해당한다.

#media file을 저장하기 위해서는 이 파일이 어떤 url을 타고 들어와 어디에 모일지 지정해주어야 한다.
# 이를 settings.py와 urls.py에서 설정한다.