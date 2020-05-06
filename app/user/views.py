from rest_framework import generics, authentication, permissions
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create a new Auth Token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Manage the authenticated user """
    serializer_class = UserSerializer
    authentication_Classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """ Retrieve and return suthenticated user """
        """ user returned here will always be atuhticated user because of the authentication class written above"""
        return self.request.user
