from rest_framework import serializers
from dataclasses import field
from auth_app_user.models import User
from django.contrib.auth import authenticate


class LoginJwtSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    auth_key = serializers.CharField()  

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        auth_key = data.get('auth_key')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password must be provided.")
        
        if not self.is_valid_auth_key(user, auth_key):
            raise serializers.ValidationError("Invalid auth_key.")

        data['user'] = user
        return data
    
    def is_valid_auth_key(self, user, auth_key):
        return user.auth_key == auth_key





