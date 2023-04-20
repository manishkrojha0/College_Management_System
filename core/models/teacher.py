from django.db import models
from django.contrib.auth.models import User
from core.models.user_address import UserAddress
from core.models.abstract_model import AbstractModel

# Create your models here.

class Teacher(AbstractModel):
    """Model class for teacher."""
    
    emp_id = models.CharField(max_length=10, null=True, unique=True, db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    user_address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, related_name='teacher_address')

    
    def __str__(self):
        """Return name of entity."""
        return self.emp_id
    
    class Meta(AbstractModel.Meta):
        db_table = "teachers"
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

