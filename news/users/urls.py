from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from .views import SignupView, UserLoginView

urlpatterns = [
    path("signup/", SignupView.as_view(), name = "signup"),
    path("login/", UserLoginView.as_view(), name = "login")

]