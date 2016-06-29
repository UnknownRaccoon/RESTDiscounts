from custom_auth.models import Profile, Address, Company
from discounts.models import Card
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import empty


class UserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        instance = kwargs['context']['view'].get_object()
        if instance.is_company:
            self.fields['company'] = CompanySerializer(instance=instance)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

    def create(self, validated_data):
        try:
            role = int(self.initial_data.get('role'))
            if role > 1:
                raise ValueError
        except (ValueError, TypeError):
            raise serializers.ValidationError({'role': 'role field must be specified and valid'})
        instance = super(UserSerializer, self).create(validated_data)
        if role == 0:
            Profile.objects.create(user=instance)
        else:
            Company.objects.create(user=instance)
        return instance

    def update(self, instance, validated_data):
        if instance.is_company:
            values = instance.company.__dict__
            values.update({key: value for key, value in self.initial_data.items()})
            company_data = CompanySerializer(instance=instance.company, data=values)
            try:
                if company_data.is_valid():
                    company_data.save()
            except ValueError:
                company_data.save()
        return super(UserSerializer,self).update(instance, validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'safe_logo')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
