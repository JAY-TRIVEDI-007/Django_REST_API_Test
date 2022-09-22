from rest_framework import serializers
from .models import Car, Owner


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(CarSerializer, self).__init__(self, *args, **kwargs)
    #
    #     # Custom validation
    #     for key in self.fields:
    #         self.fields[key].error_messages["required"] = f"{key} is required."
    #         self.fields[key].error_messages["blank"] = f"{key} cannot be empty."


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(OwnerSerializer, self).__init__(self, *args, **kwargs)
    #
    #     # Custom validation
    #     for key in self.fields:
    #         self.fields[key].error_messages["required"] = f"{key} is required."
    #         self.fields[key].error_messages["blank"] = f"{key} cannot be empty."

