# accounts/adapter.py
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # 기본 사용자 저장 로직을 실행하고 추가적인 필드를 설정합니다.
        user = super().save_user(request, user, form, commit=False)
        user.age = form.cleaned_data.get('age')
        user.name = form.cleaned_data.get('name')
        user.sex = form.cleaned_data.get('sex')
        user.profile_photo = form.cleaned_data.get('profile_photo')
        
        if commit:
            user.save()
        return user
