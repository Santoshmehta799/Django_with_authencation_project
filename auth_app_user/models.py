from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.utils.translation import gettext_lazy as _

import secrets
# Create your models here.


class ModelMixin(models.Model):
    # user
    created_by = models.UUIDField(null=True, blank=True, help_text="User Id who created this record.")
    updated_by = models.UUIDField(null=True, blank=True, help_text="User Id who updated this record.")
    # datetime
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="Date and time at which this record is created")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, help_text="Date and time at which this record is last updated.")

    class Meta:
        abstract = True

# this is Abstractuser

class User(AbstractUser,ModelMixin):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    mobile_number = models.CharField(max_length=255, null=True, blank=True, unique=True)
    user_bio = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    auth_key = models.CharField(max_length=32, unique=True, default=secrets.token_hex(16))

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()



# this is abstractbaseuser 

# class User(AbstractBaseUser, PermissionsMixin):
#     mobile_number = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True, null=True, blank=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
    
#     objects = UserManager()
#     USERNAME_FIELD = "mobile_number"
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.mobile_number