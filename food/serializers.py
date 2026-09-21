from rest_framework import serializers
from .models import Item


class Itemserializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "item_name", "item_desc", "item_price", "item_image"]
