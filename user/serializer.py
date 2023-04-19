from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import *


class USerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = CustomUser
        fields = ["id", "name", "username", "password"]

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(USerializer, self).create(validated_data)
