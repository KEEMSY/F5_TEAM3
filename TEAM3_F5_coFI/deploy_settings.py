# 도메인용 서버
import json
import os

from TEAM3_F5_coFI.settings import BASE_DIR

# ALLOWED_HOSTS = ['cofi-f5.com']
# DEBUG = False
ALLOWED_HOSTS = []
DEBUG = True



# aws.json 가져와서 버킷,db 접근권한 주기
with open(os.path.join(BASE_DIR, 'aws.json')) as f:
    secrets = json.loads(f.read())

# 정적파일 업로드를 위한 S3 연결 세팅
# https://kangraemin.github.io/django/2020/09/29/elasticbeanstalk-s3/    <<-- 블로그에 잘 정리되어있음.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# 아래 친구가 s3 경로의 스태틱을 쓰게 하는 친구
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
AWS_ACCESS_KEY_ID = secrets['AWS']['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS']['SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS']['STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = 'public-read' # 저같은 경우는 public-read로 지정 해 주었습니다. 공식문서를 반드시 참조 해주세요.
# AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com" # 공식 문서를 참조해주세요. ( cdn 사용이냐, s3 사용이냐에 갈리지만, 여기선 s3 이므로 저는 f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"를 사용 하였습니다.)
# STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/" # django 프로젝트에서 사용할 static 파일을 경로를 지정 해주세요. 저같은 경우는 f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"을 사용 하였습니다.
AWS_S3_REGION_NAME = 'ap-northeast-2'
# ck_editor를 위한 설정!!!
AWS_QUERYSTRING_AUTH = False


# AWS db 연결
DATABASES = {
    'default': {
        'ENGINE': secrets['default']['ENGINE'],
        'NAME': secrets['default']['NAME'],
        'USER': secrets['default']['USER'],
        'PASSWORD': secrets['default']['PASSWORD'],
        'HOST': secrets['default']['HOST'],
        'PORT': secrets['default']['PORT'],
        'OPTIONS': {
                'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}