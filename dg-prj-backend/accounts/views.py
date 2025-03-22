from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserDetailsSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    data = {
        "user_id": user.id,
        "email": user.email,
        # "username": user.username, # 더미필드 null이어도 노상관
        "name": user.name,
        "age": user.age,
        "sex": user.sex,
        # "profile_photo" : user.profile_photo
        "avg_win_point": user.avg_win_point,
    }
    return Response(data)


@api_view(["PUT"])
def update_profile(request):
    """
    프로필 수정 API 뷰
    - 단순 정보 수정은 serializer.save() 사용
    """
    # 부분 업데이트를 위한 partial=True 설정
    serializer = CustomUserDetailsSerializer(
        request.user, data=request.data, partial=True  # 일부 필드만 업데이트 가능
    )
    if serializer.is_valid():
        # 단순 정보 수정은 save() 메서드로 충분
        user = serializer.save()
        return Response(
            {
                "message": "프로필이 수정되었습니다.",
                "user": serializer.data,
            }
        )
