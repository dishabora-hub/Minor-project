from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import CustomUser

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None


