from django.urls import path
from . import views

urlpatterns = [
    path("user-info/", views.get_user_info),
    path("update-info/", views.update_profile),
]
