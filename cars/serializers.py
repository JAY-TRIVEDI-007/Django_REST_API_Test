from rest_framework import serializers
from .models import Car, Owner


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = "__all__"
