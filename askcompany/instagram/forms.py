# askcompany/instagram/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [  # 어떠한 필드를 추가함, 여기에 작성된 필드만 유효성 검사를 진행
            'message', 'photo', 'tag_set', 'is_public'
        ] 
        # exclude =[] #어떠한 필드를 배제함