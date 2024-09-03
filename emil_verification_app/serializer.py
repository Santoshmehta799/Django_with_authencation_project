from rest_framework import serializers
from auth_app_user.models import User

class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['email','password', 'username', 'is_verified']

class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()