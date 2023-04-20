"""Model for storing addresses related to a user."""


from django.db import models
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from core.utils.validators import validate_latitude, validate_longitude, validate_pincode


class UserAddress(BaseModel):
    """Model for storing addresses for a user."""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    street_address = models.TextField()
    landmark = models.TextField(null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   validators=[validate_latitude], null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                    validators=[validate_longitude], null=True)
    pincode = models.CharField(null=True, validators=[validate_pincode], max_length=6)

    class Meta:
        db_table = 'user_address'
        verbose_name = 'Address related to a user'
        verbose_name_plural = 'Adresses related to a user'
    
    def __str__(self) -> str:
        return self.street_address
