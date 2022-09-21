from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, routers, generics



SUCCESS_RESPONSE = {'success': True}

# @api_view(["POST"])
# def create_user(request, *args, **kwargs):
#     return Response({'success': True})


# class UserDetailAPIView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = "userID"

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "userID"

    def update(self, request, *args, **kwargs):
        res = super().update(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res

    def destroy(self, request, *args, **kwargs):
        res = super().destroy(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res


# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserCreateListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        # print(type(res))
        res.data = SUCCESS_RESPONSE
        # print(f"Response: {res}")
        return res
