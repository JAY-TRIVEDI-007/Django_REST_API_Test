from django.shortcuts import render
from django.http import JsonResponse
from .models import Ads, Post
from .serializers import AdsSerializer, PostSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cars24_api.authentication import CustomAuthentication


SUCCESS_RESPONSE = {'success': True}


class AdRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    lookup_field = "adID"
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        res = super().update(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res

    def destroy(self, request, *args, **kwargs):
        res = super().delete(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res


class AdListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    lookup_field = "adID"
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res
