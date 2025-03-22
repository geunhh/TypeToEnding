from django.db.models.signals import (
    post_save,
)  # 모델 인스턴스가 저장된 후에 실행되는 신호
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# AUTH_USER_MODEL이 저장된 후에 실행
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
