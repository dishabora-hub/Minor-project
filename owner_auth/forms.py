from django import forms
from django.contrib.auth.forms import UserCreationForm
from login_page.models import CustomUser  # Use CustomUser from the login_page app

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser  # Use CustomUser instead of the default User model
        fields = [ 'email', 'password1', 'password2']  # Add any fields you want in the signup form
