from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    data = {
        "user_id": user.id,
        "email": user.email,
        "name": user.name,
        # 필요한 추가 필드가 있다면 여기에 추가합니다.
    }
    return Response(data)
