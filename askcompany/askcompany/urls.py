"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# askcompany/ursl.py

from django.contrib import admin
from django.urls import path, include

# django.conf의 global_settings와 askcompany의 settings를 합친 settings가 필요(오버라이트)
from django.conf import settings

from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

# 최상위 URL처리
# class RootView(TemplateView):
#     template_name = 'root.html'

urlpatterns = [
    # path('', RootView.as_view(), name='root'),
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),   # RootView가 없다면
    path('', RedirectView.as_view(
        # url='/instagram/', 
        pattern_name='instagram:post_list' # app_name:pattern_name
        ), name='root'),
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('k-instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:  # 개발모드일 경우에만 실행
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
