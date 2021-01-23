# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from accounts.models import Profile
from accounts.forms import ProfileForm

# FBV 프로필
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')

# CBV 프로필
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

# 프로필 수정 FBV
@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:    # 프로필이 없다면
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })

# 회원가입
def signup(request):
    pass

# 로그아웃
def logout(request):
    pass