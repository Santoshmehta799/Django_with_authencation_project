from django.contrib.auth.base_user import BaseUserManager
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password




# =========================================  abstract user======================================

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fileds):
        if not username:
            raise ValueError("user name is required")
        
        extra_fileds['email'] = self.normalize_email(extra_fileds.get('email',''))
        user = self.model(username=username, **extra_fileds)
        user.set_password(password)
        user.save(using = self.db)
        return user
    def create_superuser(self, username, password=None, **extra_fileds):
        extra_fileds.setdefault("is_staff", True)
        extra_fileds.setdefault('is_active',True)
        extra_fileds.setdefault("is_superuser", True)
        
        return self.create_user(username, password, **extra_fileds)


# ======================================  Abstractbaseuser =============================


# class UserManager(BaseUserManager):
#     def create_user(self, mobile_number, password=None, **extra_fields):
#         if not mobile_number:
#             raise ValueError("Mobile number is required")
        
#         # Normalize the email address by lowercasing the domain part of it
#         if 'email' in extra_fields:
#             extra_fields['email'] = self.normalize_email(extra_fields['email'])

#         user = self.model(mobile_number=mobile_number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, mobile_number, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         return self.create_user(mobile_number, password, **extra_fields)