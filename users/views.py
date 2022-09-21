from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, routers, generics


# @api_view(["POST"])
# def create_user(request, *args, **kwargs):
#     return Response({'success': True})


class UserListAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "userID"


class UserDetailAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
