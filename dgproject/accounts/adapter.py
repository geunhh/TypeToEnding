# accounts/adapter.py
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        data = request.data
        user.age = data.get("age")
        user.name = data.get("name")
        user.sex = data.get("sex")
        user.profile_photo = data.get("profile_photo")
        user.avg_win_point = data.get("avg_win_point")

        if commit:
            user.save()
        return user
