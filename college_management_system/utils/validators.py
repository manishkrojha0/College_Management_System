import re
from django.core.exceptions import ValidationError

def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError("Invalid latitude")


def validate_longitude(value):
    if value < -180 or value > 180:
        raise ValidationError("Invalid longitude")

def validate_contact(value):
    regex = r'^(\+)?\d{10,15}$'
    if not re.match(regex, value):
        raise ValidationError("A valid number may start with \'+\' and have 10 to 15 digits")

def validate_pincode(value):
    regex = r'^[1-9][0-9]{5}$'
    if not re.match(regex, value):
        raise ValidationError("Not a valid pincode")