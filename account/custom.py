from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend




class EmailOrUsernameModelBackend(ModelBackend):

    def authenticate(self, request,**kwargs):
        User = get_user_model()
        username = kwargs['username']
        password = kwargs['password']

        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None
