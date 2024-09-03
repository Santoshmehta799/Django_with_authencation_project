from django.shortcuts import render
from rest_framework.views import APIView

from jwt_app.serializer import LoginJwtSerializer
from rest_framework.response import Response  
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
 
# Create your views here.

class LoginApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginJwtSerializer(data=data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return Response({
                    'status': 400,
                    'message': "username and password are incorrect",
                    'data': serializer.errors
                }, status=400)
        
        except Exception as e:
            print(f"Error {e}")
            return Response({
                'status': 500,
                'message': "Internal server error",
                'error': str(e)
            }, status=500)


# class LoginApi(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginJwtSerializer(data=data)
            
#             if serializer.is_valid():
#                 print("yes this is valid")
#                 user = serializer.validated_data['user']  # Get the authenticated user
                
#                 # Generate JWT tokens
#                 refresh = RefreshToken.for_user(user)
                
#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 })
#             else:
#                 return Response({
#                     'status': 400,
#                     'message': "Mobile number and password are incorrect",
#                     'data': serializer.errors
#                 }, status=400)
        
#         except Exception as e:
#             print(f"Error {e}")
#             return Response({
#                 'status': 500,
#                 'message': "Internal server error",
#                 'error': str(e)
#             }, status=500)