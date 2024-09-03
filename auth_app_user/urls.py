from django.urls import path
from auth_app_user import views
# from auth_app_user.views import UserRegistrationView
app_name = "auth_app_user"


urlpatterns = [
    path('register/api/',views.UserRegistrationView.as_view(), name='register-api'),
    path('all-user/',views.AllUserGet.as_view(),name='all-user'),
    path('update/api',views.UserUpdateView.as_view(),name='user-update')
]