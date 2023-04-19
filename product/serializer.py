from rest_framework import serializers

from .models import *

# serializer for Products


class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class OSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
