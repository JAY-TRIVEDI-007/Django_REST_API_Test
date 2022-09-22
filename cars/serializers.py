from rest_framework import serializers
from .models import Car, Owner
from users.serializers import UserDataSerializer


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


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = [
            "carID",
            "brand",
            "model",
            "number_plate",
            "owner"
        ]

    def get_owner(self, obj):
        data = Owner.objects.get(carID=obj.carID)
        if data is not None:
            return data.userID.userID
        return None

    # def __init__(self, *args, **kwargs):
    #     super(CarSerializer, self).__init__(self, *args, **kwargs)
    #
    #     # Custom validation
    #     for key in self.fields:
    #         self.fields[key].error_messages["required"] = f"{key} is required."
    #         self.fields[key].error_messages["blank"] = f"{key} cannot be empty."



