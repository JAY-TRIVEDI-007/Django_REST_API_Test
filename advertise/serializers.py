from rest_framework import serializers
from .models import Ads, Post


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(AdsSerializer, self).__init__(self, *args, **kwargs)
    #
    #     # Custom validation
    #     for key in self.fields:
    #         self.fields[key].error_messages["required"] = f"{key} is required."
    #         self.fields[key].error_messages["blank"] = f"{key} cannot be empty."


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(PostSerializer, self).__init__(self, *args, **kwargs)
    #
    #     # Custom validation
    #     for key in self.fields:
    #         self.fields[key].error_messages["required"] = f"{key} is required."
    #         self.fields[key].error_messages["blank"] = f"{key} cannot be empty."
