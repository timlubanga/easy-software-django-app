from django.urls import path
from userAuth.views import UserRegistrationView, SigninView


authurlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', SigninView.as_view(), name="login")]
