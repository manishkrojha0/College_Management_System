from django.db import models
# from django.contrib.auth.models import User
from core.models.user_address import UserAddress
from core.models.abstract_model import AbstractModel
from core.models.users import Users
from django.conf import settings

# Create your models here.

class Student(AbstractModel):
    """Model class for teacher."""

    roll_no = models.CharField(max_length=10, null=True, unique=True, db_index=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='core_users')
    user_address = models.OneToOneField(UserAddress, on_delete=models.CASCADE, related_name='student_address')

    def __str__(self):
        """Return name of entity."""
        return self.roll_no
    
    class Meta(AbstractModel.Meta):
        db_table = "students"
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def save(self, *args, **kwargs):
        self.user.is_student = True
        self.user.save()
        super().save(*args, **kwargs)
