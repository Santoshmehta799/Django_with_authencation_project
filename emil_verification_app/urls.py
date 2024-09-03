from django.urls import path
from emil_verification_app import views

app_name = 'emil_verification_app'

urlpatterns = [
    path('user-register/api/',views.RegisterEmailUser.as_view(), name="verification_register"),
    path('verify-otp/api/', views.VerifyOtp.as_view(), name='verify_otp')
]