from custom_auth.models import Profile, Company
from django.db import models


class Card(models.Model):
    DISCOUNT = 0
    CUMULATIVE = 1
    TYPE_CHOICES = (
        (DISCOUNT, 'Discount'),
        (CUMULATIVE, 'Cumulative'),
    )
    profile = models.ForeignKey(Profile)
    company = models.ForeignKey(Company)
    card_code = models.CharField(max_length=50)
    card_type = models.SmallIntegerField(choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('company', 'card_code')
