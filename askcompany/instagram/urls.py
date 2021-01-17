# askcompany/instagram/urls.py

from django.urls import path, re_path, register_converter
from . import views

# 커스텀 Converter 정의
class YearConverter:
    regex = r"20\d{2}"
    
    # URL 매칭이 되었을 때, view함수를 호출하기 전에 인자를 정리함
    def to_python(self, value):
        return int(value)

    #URL Reverse를 할 때, 어떤 값을 URL로 전달할 문자열로 바꿈
    def to_url(self, value):
        return str(value)

# YearConverter를 year이란 문자열로 사용할 것임
register_converter(YearConverter, 'year')

# URL Reverse에서 name space 역할을 함
app_name = 'instagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('archives/<year:year>/', views.archives_year),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
]