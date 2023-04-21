from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission
# from django.contrib.auth.models import PermissionsMixin


class Users(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='core_users')

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='auth_users_permissions', # specify a different related name
        related_query_name='user'
    )
    
