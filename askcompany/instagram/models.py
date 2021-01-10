# askcompany/instagram/modles.py
# -*- coding: cp949 -*- 

from django.db import models
# from django.contrib.auth.models import User   # �ش� ���� ����Ϸ��� FK�� 'auth.User'�� �ۼ� �ʿ�

# User���� ���� ������ٸ� ������Ʈ�� setting�� �����ϰ� ����Ʈ�ϱ�
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, related_name='+')
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d') # media���� �ؿ� upload_to ��ΰ� ������
    tag_set = models.ManyToManyField('Tag', blank=True) # Tag�� ������ ���, Tag�� ���� ���� �׾���(�ۼ� ��ÿ� ���ǵǾ� ���� ����)
    is_public = models.BooleanField(default=False, verbose_name='��������')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # java�� toString�� ���� ���
    def __str__(self):
        #return f"Custom Post object ({self.id})"
        return self.message

    # default ����
    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    # Post�� Comment�� 1 : N ����, 1�� PK�� N�� ������ �����ؾ� ��
    # �ʵ��_id �� ������ ��
    # Post�� 'Post'�� 'instagram.Post' �� ǥ���ص� ��
    # post�� ������ �ʵ�
    post = models.ForeignKey(Post, on_delete=models.CASCADE,    # post_id�� �ʵ尡 ������
            limit_choices_to={'is_public': True})    # ���� �׸��� �����ϱ�
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    # �ν��Ͻ� ��ü�� ��� �� ���� ������ �������ִ� �Լ�
    def __str__(self):
        return self.name