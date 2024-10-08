from django.core.mail import send_mail
from django.conf import settings
import random
from auth_app_user.models import User


def send_otp_via_email(email):
    subject = "your account verification email"
    otp = random.randint(1000, 9999)
    message = f"your otp is: {otp}"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()