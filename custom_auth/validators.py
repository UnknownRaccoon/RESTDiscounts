import re
from django.core.exceptions import ValidationError


def validate_username(value):
    if not re.match(r'^\+\d{9,15}$', value):
        raise ValidationError('Username must be a valid phone number')