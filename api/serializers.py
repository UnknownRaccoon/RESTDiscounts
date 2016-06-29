import re
from custom_auth.models import Profile, Address
from discounts.models import Card
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
