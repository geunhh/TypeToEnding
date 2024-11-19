from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    username = models.CharField(max_length=30, unique=False, null=True, blank=True)

    SEX_CHOICES = [
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)  # 필수 수정 부분
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.email

    # 메타정보
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []





    

    