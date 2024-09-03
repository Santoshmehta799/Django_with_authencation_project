from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
from django.db.models import fields

user = get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__' 
        # fields = ('mobile_number', 'email', 'password', 'password2' )
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    
    def create(self, validated_data):
        print("------validated_data------>>",validated_data)
        validated_data.pop('password2')
        user = User.objects.create_user(
            mobile_number = validated_data['mobile_number'],
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user
    
class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_bio']

