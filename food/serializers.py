from typing import ReadOnly

from rest_framework import serializers
from .models import Item, Order
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

    def validate_item_price(self, value):
        if value < 1:
            raise serializers.ValidationError("price must be more than 1$")
        return value

    def validate(self, data):
        if data["item_name"].lower() == data["item_desc"]:
            raise serializers.ValidationError("item name and item desc are same")
        return data


class OrderSerializers(serializers.ModelSerializer):
    items = Itemserializers(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ["id", "user", "created_at", "items"]
