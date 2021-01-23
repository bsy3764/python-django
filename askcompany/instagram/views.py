# askcompany/instagram/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy

# 직접 함수로 구현(FBV)
# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')    # request.GET : 쿼리 스트링 문자
#     if q:
#         qs = qs.filter(message__icontains=q)

#     messages.info(request, 'messages test')  # 메시지 등록만 함(소비는 x)

#     # 장고의 templates를 사용해 html 화면  만들기
#     # askcompany/instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs, 
#         'q': q,
#     })

# 위의 post_list 함수를 장고가 지원해 주는 클래스로 구현(CBV)
# 장식자를 이미 생성된 함수에 입힘
# post_list =login_required(ListView.as_view(model=Post, paginate_by=10))

# @method_decorator(login_required, name='dispatch')
# 바로 위의 장식자 대신에 LoginRequiredMixin을 추가해도 됨
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })

# request.user 로 인하여 이 뷰는 로그인 상태임을 보장 받아야 함
# @login_required
# def post_new(request):
#     if request.method == 'POST':    # POST 요청일 때
#         # POST 인자는 request.POST, request.FILES를 제공받음
#         form = PostForm(request.POST, request.FILES)

#         # 인자로 받은 값에 대해 유효성 검증 수행
#         if form.is_valid(): # 검증이 성공하면 True 반환
#             post = form.save(commit=False)  # 바로 저장하지 않고 대기
#             post.author = request.user  # 작성자를 현재 로그인 유저로 채우기
#             post.save()
#             messages.success(request, '포스팅을 저장했습니다.')
#             return redirect(post)   # get_absolute_url이 있어서 post_detail로 이동함
#     else:   # GET 요청일 때
#         form = PostForm()   # form 초기화하기
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None,
#     })

# 위의 post_new 함수를 CBV로 구현
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')
        return super().form_valid(form)

post_new = PostCreateView.as_view()


# 모든 사용자(유저)마다 DetailView가 동일하게 적용됨
post_detail = DetailView.as_view(
    model=Post,
    queryset=Post.objects.filter(is_public=True))   # 공개된 것만 보임

# 유저마다 DetailView를 다르게 하려면
class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)  # 공개된 것만 보임
    def get_queryset(self):
        qs = super().get_queryset()  # 부모의 함수를 호출해서 재정의
        if not self.request.user.is_authenticated:  # 현재 로그인된 유저 인스턴스가 없다면(로그인 안한 상태면)
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     # 작성자일 경우에만 수정 가능
#     if  post.author != request.user:    # 작성자와 로그인 유저가 다르면
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)

#     if request.method == 'POST':    # POST 요청일 때
#         # POST 인자는 request.POST, request.FILES를 제공받음
#         form = PostForm(request.POST, request.FILES, instance=post)

#         # 인자로 받은 값에 대해 유효성 검증 수행
#         if form.is_valid(): # 검증이 성공하면 True 반환
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다.')
#             return redirect(post)   # get_absolute_url이 있어서 post_detail로 이동함
#     else:   # GET 요청일 때
#         form = PostForm(instance=post)   # form 초기화하기
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post,
#     })

# 위의 post_edit 함수를 CBV로 구현
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)

post_edit = PostUpdateView.as_view()

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, '포스팅을 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })

# 위의 post_delete 함수를 CBV로 구현
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')

    # def get_success_url(self):
    #     return reverse('instagram:post_list')

post_delete = PostDeleteView.as_view()



# def archives_year(request, year):
#     return HttpResponse(f"{year} archives")

post_archive = ArchiveIndexView.as_view(
    model=Post, date_field='create_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(
    model=Post, date_field='create_at', make_object_list=True)