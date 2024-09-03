from django.contrib import admin
from auth_app_user import models
from .models import User

# Register your models here.

# ============  This is for abstract user=====================

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'user_uuid', 'mobile_number', 'email', 'auth_key', 'first_name', 'username','is_verified','is_active', 'created_at', 'updated_at')

# ====================================================================
from django.contrib.auth.admin import UserAdmin

# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ['mobile_number', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
#     list_filter = ['is_staff', 'is_active']
#     readonly_fields = ['date_joined'] 
#     fieldsets = (
#         (None, {'fields': ('mobile_number', 'email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('mobile_number', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ['mobile_number', 'email', 'first_name', 'last_name']
#     ordering = ['mobile_number']

# admin.site.register(User, UserAdmin)