from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import PermissionsMixin


class Users(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    