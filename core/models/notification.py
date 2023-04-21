"""Model for sending the notification."""
from django.db import models
from .base_model import BaseModel
from core.models.users import Users
# from django.contrib.auth.models import User
# from core.models.user import User
# from .classes import Classes
# from django.conf import settings

class Notification(BaseModel):
    """Model class."""

    title = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='notification')
    read = models.BooleanField(default=False, null=True)
    class_attendance = models.ForeignKey('Classes', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self) -> str:
        return self.title

