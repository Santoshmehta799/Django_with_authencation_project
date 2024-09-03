
from google_app import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'google_app'

urlpatterns = [
    path('login-page/',views.login, name='login_page'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('home/',views.home, name='home'),
]
