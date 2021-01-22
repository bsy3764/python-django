# askcompany/instagram/modles.py
# -*- coding: cp949 -*- 

from django.db import models
# from django.contrib.auth.models import User   # 해당 모델을 사용하려면 FK에 'auth.User'로 작성 필요

# User모델을 직접 만들었다면 프로젝트의 setting에 설정하고 임포트하기
from django.conf import settings

from django.urls import reverse
from django.core.validators import MinLengthValidator

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, related_name='+')
    message = models.TextField(
        # 10글자 미만의 문자열을 받았을 때, forms.ValidationError 발생함
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d') # media폴더 밑에 upload_to 경로가 생성됨
    tag_set = models.ManyToManyField('Tag', blank=True) # Tag로 지정할 경우, Tag에 빨간 밑줄 그어짐(작성 당시엔 정의되어 있지 않음)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # java의 toString과 같은 기능
    def __str__(self):
        #return f"Custom Post object ({self.id})"
        return self.message
    
    # URL Reverse를 위한 get_absolute_url() 구현
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    # default 정렬
    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    # Post와 Comment가 1 : N 관계, 1의 PK를 N의 측에서 저장해야 함
    # 필드명_id 로 저장이 됨
    # Post를 'Post'나 'instagram.Post' 로 표현해도 됨
    # post는 가상의 필드
    post = models.ForeignKey(Post, on_delete=models.CASCADE,    # post_id란 필드가 생성됨
            limit_choices_to={'is_public': True})    # 선택 항목을 제한하기
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    # 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
    def __str__(self):
        return self.name