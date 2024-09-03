from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from emil_verification_app.serializer import UserEmailSerializer, VerifySerializer
from .emails import *
# Create your views here.


class RegisterEmailUser(APIView):
    def post(self, request):
        try:
            data = request.data 
            serializer = UserEmailSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'Register successfully, check your email',
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            }, status=400)
        except Exception as e:
            print(f"Error message: {e}")
            return Response({
                'status': 500,
                'message': 'An internal error occurred',
                'error': str(e)
            }, status=500)


class VerifyOtp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifySerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                    'status':200,
                    'message':'something went wrong',
                    'data': 'invalid email'
                    })
                user=user.first()

                if user.otp != otp:
                    return Response({
                    'status':200,
                    'message':'something went wrong',
                    'data': 'wrong otp'
                    })
                user.is_verified=True
                user.save()

                return Response({
                    'status':200,
                    'message':'regsiter successfully check email',
                    'data': {}
                })
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':serializer.errors
            })

        except Exception as e:
            print(e)

