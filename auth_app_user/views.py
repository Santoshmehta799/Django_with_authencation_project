from rest_framework import status
from django.shortcuts import render
from auth_app_user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from auth_app_user.serializer import UserGetSerializer, UserRegistrationSerializer, UserUpdateSerializer

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegistrationSerializer

class AllUserGet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserGetSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put (self, request):
        user = request.user
        auth_key = request.headers.get('X-Auth-Key')
        if not auth_key or auth_key != user.auth_key:
            raise AuthenticationFailed('Invalid or missing auth key')
        
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'user': serializer.data,
                'message': 'User updated successfully'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    