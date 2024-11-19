
from django.urls import path,include
from . import views

urlpatterns = [
    path('user-info/', views.get_user_info)
]
