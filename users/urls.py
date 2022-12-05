from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import GoogleLogin, VKLogin, FacebookLogin

urlpatterns = [
    path('token-create/', TokenObtainPairView.as_view()),
    path('oauth/google/', GoogleLogin.as_view(), name='google_login'),
    path('oauth/vk/', VKLogin.as_view(), name='vk_login'),
    path('oauth/facebook/', FacebookLogin.as_view(), name='facebook_login'),
]