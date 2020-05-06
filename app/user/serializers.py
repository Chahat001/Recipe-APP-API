from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializzers fo the user object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'min_length': 5
                }
            }

    def create(self, validated_data):
        """ Create a new user with enryoted password and return it """
        print(validated_data)
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """ update the user, setting the password correctly and return it"""
        """ instance : model instance that is linked to out model serailizer in our case our user model"""
        """ validated data is the incoming validated data """

        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            """ write user back to database with edited password"""
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for the user authnication object """
    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type' : 'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        """ validate and autheicate the user """
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )

        if not user:
            msg = _('unable to autheicate with provided ceredentials')
            raise serializers.ValidationError(msg, code = 'authentication')

        attrs['user'] = user
        return attrs
