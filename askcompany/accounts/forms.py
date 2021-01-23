# accounts/forms.py

from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm    # 해당 폼이 이미 로그인뷰에 적용이 되어 있음

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zipcode']

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3 + 3 = ?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        if answer != 6:
            raise forms.ValidationError('틀렸습니다.')
        return answer