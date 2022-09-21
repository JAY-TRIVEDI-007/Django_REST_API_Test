from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["userID", "f_name", "l_name", "age", "house_no", "street", "city", "country"]
        fields = "__all__"
