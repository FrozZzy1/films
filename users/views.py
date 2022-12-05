from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.vk.views import VKOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from dj_rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class VKLogin(SocialLoginView):
    adapter_class = VKOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
