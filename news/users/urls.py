from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import SignupView, UserLoginView

urlpatterns = [
    path("signup/", SignupView.as_view(), name = "signup"),
    path("login/", UserLoginView.as_view(), name = "login"),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name = "password reset")

]