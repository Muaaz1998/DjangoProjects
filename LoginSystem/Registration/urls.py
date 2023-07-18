from django.urls import path
from . import views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('', views.register, name = 'register'),
    path('register/', RegistrationView.as_view(success_url = '/home/'), name = 'registered')
]