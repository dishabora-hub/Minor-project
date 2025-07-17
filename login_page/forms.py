from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Use the custom user model
User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SignUpForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
   

    # Optional: Validation to ensure email is unique
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    # Validate that both password fields match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Passwords do not match.")

        return cleaned_data

    # Create the user and save to the database
    def save(self, commit=True):
        # Extract the data from cleaned_data
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
       

        # Create a new user (use your custom user model)
        user = User.objects.create_user(
            name=name, email=email, password=password
        )
        if commit:
            user.save()
        return user
