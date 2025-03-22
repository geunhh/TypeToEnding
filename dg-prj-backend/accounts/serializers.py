from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class CustomUserRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    sex = serializers.ChoiceField(choices=CustomUser.SEX_CHOICES, required=False)
    profile_photo = serializers.ImageField(required=False)
    avg_win_point = serializers.FloatField(required=False)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password1",
            "password2",
            "age",
            "name",
            "sex",
            "profile_photo",
            "avg_win_point",
        ]

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["age"] = self.validated_data.get("age", None)
        data["name"] = self.validated_data.get("name", None)
        data["sex"] = self.validated_data.get("sex", None)
        data["profile_photo"] = self.validated_data.get("profile_photo", None)
        data["avg_win_point"] = self.validated_data.get("avg_win_point", None)
        return data

    def save(self, request):
        user = super().save(request)
        user.age = self.cleaned_data.get("age")
        user.name = self.cleaned_data.get("name")
        user.sex = self.cleaned_data.get("sex")
        user.profile_photo = self.cleaned_data.get("profile_photo")
        user.avg_win_point = self.cleaned_data.get("avg_win_point")
        user.save()
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    name = serializers.CharField(
        required=False, allow_blank=True, max_length=30, help_text="사용자 닉네임"
    )
    sex = serializers.CharField(
        required=False, allow_blank=True, max_length=1, help_text="사용자 성별"
    )
    age = serializers.IntegerField(
        required=False, allow_null=True, help_text="사용자 나이"
    )

    # username 필드 제거
    username = None

    class Meta:
        model = User
        fields = ("pk", "email", "age", "name", "sex", "avg_win_point")
        read_only_fields = ("email",)

    def update(self, instance, validated_data):
        """사용자 정보 업데이트"""
        try:
            instance.age = validated_data.get("age", instance.age)
            instance.name = validated_data.get("name", instance.name)
            instance.sex = validated_data.get("sex", instance.sex)

            instance.save()
            return instance

        except Exception as e:
            raise serializers.ValidationError(
                f"프로필 업데이트 중 오류가 발생했습니다: {str(e)}"
            )
