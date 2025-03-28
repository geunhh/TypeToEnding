from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("gameApp/", include("gameApp.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("dj_rest_auth.urls")),
    # 이렇게 라우팅 설정하면, dj_rest_auth 라이브러리에서 사용하는 기본 인증 기능들 사용 가능.
    # 회원가입, 로그인, 로그아웃, 비밀번호 변경 등의 기능을 RESTful API로 쉽게 제공.
    path("accounts/signup/", include("dj_rest_auth.registration.urls")),  # 회원가입
    path("api/auth/", include("dj_rest_auth.urls")),  # 비밀번호 변경 URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
