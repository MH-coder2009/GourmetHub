from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class Itemserializers(serializers.ModelSerializer):
    user_name = UserSerializer(read_only=True)

    class Meta:
        model = Item
        fields = [
            "id",
            "user_name",
            "item_name",
            "item_desc",
            "item_price",
            "item_image",
        ]
