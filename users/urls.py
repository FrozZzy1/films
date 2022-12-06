from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateAPIView, UserProfileDetailAPIView


urlpatterns = [
    path('all-users', UserProfileListCreateAPIView.as_view(), name='all-users'),
    path('user/<int:pk>', UserProfileDetailAPIView.as_view(), name='user'),
]