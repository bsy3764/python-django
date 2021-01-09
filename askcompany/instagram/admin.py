# askcompany/instagram/admin.py

from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe

# 장식자를 이용하기
@admin.register(Post)   # 어떠한 대상이라도 감싸는 것(wrapping)
class PostAdmin(admin.ModelAdmin):
    # models에 있는 속성명, 함수명(인자가 없는)이 들어갈 수 있음
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'create_at', 'update_at']
    
    # 내용으로 이동할 하이퍼링크를 적용할 속성
    list_display_links = ['message']
    
    # 검색
    search_fields = ['message']

    # 필터링
    list_filter = ['create_at', 'is_public']

    def message_length(self, post):
        return len(post.message)

    def photo_tag(self, post):
        if post.photo:
            # mark_safe를 붙이지 않으면 이미지를 보여주지 않음, 장고 보안기능
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;"/>')
        return None

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass