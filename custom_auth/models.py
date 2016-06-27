from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)
    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['is_company']


class Profile(models.Model):
    user = models.OneToOneField(CustomUser)


class Company(models.Model):
    user = models.OneToOneField(CustomUser)
    logo = models.ImageField(null=True, blank=True)


class Address(models.Model):
    company = models.ForeignKey(Company)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
