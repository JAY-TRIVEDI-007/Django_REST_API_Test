from django.urls import path, include
from .views import UserListAPIView, UserDetailAPIView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('users', UserDetailAPIView)
# urlpatterns = [
#     path('', include(router)),
# ]


urlpatterns = [
    path('users/', UserDetailAPIView.as_view()),
    path('users/<int:userID>/', UserListAPIView.as_view())
]
