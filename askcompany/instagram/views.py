# askcompany/instagram/views.py

from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')    # request.GET : 쿼리 스트링 문자
    if q:
        qs = qs.filter(message__icontains=q)
    # 장고의 templates를 사용해 html 화면  만들기
    # askcompany/instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs, 
        'q': q,
    })
