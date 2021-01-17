# askcompany/instagram/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView

# 직접 함수로 구현(FBV)
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')    # request.GET : 쿼리 스트링 문자
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # 장고의 templates를 사용해 html 화면  만들기
#     # askcompany/instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs, 
#         'q': q,
#     })

# 위의 post_list 함수를 장고가 지원해 주는 클래스로 구현(CBV)
post_list = ListView.as_view(model=Post)

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })

post_detail = DetailView.as_view(model=Post)

def archives_year(request, year):
    return HttpResponse(f"{year} archives")