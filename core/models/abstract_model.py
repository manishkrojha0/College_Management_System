from core.models.base_model import BaseModel
from django.db import models
from core.utils.constants import GENDER_OPTIONS
from core.utils.validators import validate_contact

class AbstractModel(BaseModel):
    """Abstract model to store combined record."""
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_OPTIONS)
    email_id = models.EmailField(null=True)
    contact = models.CharField(max_length=15, validators=[validate_contact])

    class Meta(BaseModel.Meta):
        abstract = True

