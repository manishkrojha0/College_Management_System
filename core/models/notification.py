"""Model for sending the notification."""
from django.db import models
from .base_model import BaseModel
from django.contrib.auth.models import User
# from .classes import Classes

class Notification(BaseModel):
    """Model class."""

    title = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    read = models.BooleanField(default=False, null=True)
    class_attendance = models.ForeignKey('Classes', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self) -> str:
        return self.title

