from custom_auth.validators import validate_username
from django.contrib.auth.models import User
from django.db import models

User.is_company = property(lambda self: hasattr(self, 'company'))
User._meta.get_field('username').validators.append(validate_username)


class Profile(models.Model):
    user = models.OneToOneField(User)


class Company(models.Model):
    user = models.OneToOneField(User)
    logo = models.ImageField(null=True, blank=True)


class Address(models.Model):
    company = models.ForeignKey(Company)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
