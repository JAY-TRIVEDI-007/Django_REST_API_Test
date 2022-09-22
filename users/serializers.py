from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["userID", "f_name", "l_name", "age", "house_no", "street", "city", "country"]
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(UserSerializer, self).__init__(self, *args, **kwargs)

        # Custom validation
        # for key in self.fields:
        #     self.fields[key].error_messages["required"] = f"{key} is required."
        #     self.fields[key].error_messages["blank"] = f"{key} cannot be empty."
        #     print(f"{key} | {self.fields[key].error_messages}")
        # print(f"{self.fields}")
