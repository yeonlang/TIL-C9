from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import AbstractUser
    
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # 유저가 만들어질때에는 아이디와 비밀번호만으로도 가입이 가능하도록
    # 빈값을 허용해 준다. (blank = True)
    nickname = models.CharField(max_length = 40, blank = True)
    introduction = models.TextField(blank = True)
    image = ProcessedImageField(
            upload_to = 'profile/images',       # 저장 위치
            processors=[ResizeToFill(300,300)], # 처리할 작업 목록
            format='JPEG',                      # 저장포맷
            options={'quality':90},             # 옵션
            blank = True,
        )

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    