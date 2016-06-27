from custom_auth.models import CustomUser
from django.db import models


class Card(models.Model):
    DISCOUNT = 0
    CUMULATIVE = 1
    TYPE_CHOICES = (
        (DISCOUNT, 'Discount'),
        (CUMULATIVE, 'Cumulative'),
    )
    profile = models.ForeignKey(CustomUser)
    company = models.ForeignKey(CustomUser, related_name='company')
    card_code = models.CharField(max_length=50)
    card_type = models.SmallIntegerField(choices=TYPE_CHOICES)
