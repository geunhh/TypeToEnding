from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(
        max_length=30, unique=False, blank=True, null=True
    )  # 얘가 실질적인 닉네임
    age = models.PositiveIntegerField(null=True, blank=True)
    username = models.CharField(
        max_length=30, unique=False, null=True, blank=True
    )  # 더미 필드, 없으면 고장남
    avg_win_point = models.FloatField(null=True)

    SEX_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    sex = models.CharField(
        max_length=1, choices=SEX_CHOICES, blank=True, null=True
    )  # 필수 수정 부분
    profile_photo = models.ImageField(
        upload_to="profile_photos/", null=True, blank=True
    )

    def __str__(self):
        return self.email

    objects = CustomUserManager()
    # 메타정보
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
