from django.urls import path

from blogApp import admin
from .views import HomePageView, PostDetailedView

urlpatterns = [
    path('post/<int:pk>/', PostDetailedView.as_view(), name = "post_detail"),
    path('', HomePageView.as_view(), name = "home")
]