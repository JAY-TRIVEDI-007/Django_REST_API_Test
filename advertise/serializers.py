from rest_framework import serializers
from .models import Ads, Post


class AdsSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ads
        fields = "__all__"

    def get_owner(self, obj):
        data = Post.objects.get(adID=obj.adID)
        if data is not None:
            return data.userID.userID
        return None

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
