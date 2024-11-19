# accounts/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomUserRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    sex = serializers.ChoiceField(choices=CustomUser.SEX_CHOICES, required=False)
    profile_photo = serializers.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'age', 'name', 'sex', 'profile_photo']

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', None)
        data['name'] = self.validated_data.get('name', None)
        data['sex'] = self.validated_data.get('sex', None)
        data['profile_photo'] = self.validated_data.get('profile_photo', None)
        return data

    def save(self, request):
        user = super().save(request)
        user.age = self.cleaned_data.get('age')
        user.name = self.cleaned_data.get('name')
        user.sex = self.cleaned_data.get('sex')
        user.profile_photo = self.cleaned_data.get('profile_photo')
        user.save()
        return user
    

