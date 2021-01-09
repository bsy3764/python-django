# askcompany/instagram/admin.py

from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe

# ����ڸ� �̿��ϱ�
@admin.register(Post)   # ��� ����̶� ���δ� ��(wrapping)
class PostAdmin(admin.ModelAdmin):
    # models�� �ִ� �Ӽ���, �Լ���(���ڰ� ����)�� �� �� ����
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'create_at', 'update_at']
    
    # �������� �̵��� �����۸�ũ�� ������ �Ӽ�
    list_display_links = ['message']
    
    # �˻�
    search_fields = ['message']

    # ���͸�
    list_filter = ['create_at', 'is_public']

    def message_length(self, post):
        return len(post.message)

    def photo_tag(self, post):
        if post.photo:
            # mark_safe�� ������ ������ �̹����� �������� ����, ��� ���ȱ��
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;"/>')
        return None

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass