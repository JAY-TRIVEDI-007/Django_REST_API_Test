from .models import Car, Owner
from .serializers import CarSerializer, OwnerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, routers, generics
from rest_framework.permissions import IsAuthenticated
from cars24_api.authentication import CustomAuthentication


SUCCESS_RESPONSE = {'success': True}


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "carID"
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        res = super().update(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res

    def destroy(self, request, *args, **kwargs):
        res = super().destroy(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res


class CarCreateListAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        res.data = SUCCESS_RESPONSE
        return res
