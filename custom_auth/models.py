from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)
    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['is_company']


class Address(models.Model):
    company = models.ForeignKey(CustomUser)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
