from jwt_app import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'jwt_app'

urlpatterns = [
    path('token/', views.LoginApi.as_view(), name='access-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]