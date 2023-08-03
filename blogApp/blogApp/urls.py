from django.urls import path

from .views import HomePageView, PostDetailedView, PostCreationView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post_delete"),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name = "post_edit"),
    path("post/new/", PostCreationView.as_view(), name = "post_new"),
    path('post/<int:pk>/', PostDetailedView.as_view(), name = "post_detail"),
    path('', HomePageView.as_view(), name = "home")
]