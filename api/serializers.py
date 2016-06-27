from custom_auth.models import Profile, Company
from discounts.models import Card
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
