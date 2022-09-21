from django.urls import path, include
from .views import UserRetrieveUpdateDestroyAPIView, UserCreateListAPIView


# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('users', UserDetailAPIView)
# urlpatterns = [
#     path('', include(router)),
# ]


urlpatterns = [
    path('users/', UserCreateListAPIView.as_view()),
    path('users/<int:userID>/', UserRetrieveUpdateDestroyAPIView.as_view())
]
