from django.contrib import admin
from django.urls import path


from core.views import UserRegistrationView, UserLoginView, UserRetrieveUpdateView, PasswordUpdateView

urlpatterns = [
    path("signup", UserRegistrationView.as_view()),
    path("login", UserLoginView.as_view()),
    path("profile", UserRetrieveUpdateView.as_view()),
    path("update_password", PasswordUpdateView.as_view()),
]
