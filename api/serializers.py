from custom_auth.models import CustomUser
from discounts.models import Card
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
