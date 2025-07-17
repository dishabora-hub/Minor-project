from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm

def sign_up_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the user to the database
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('owner_auth:log_in')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'owner_auth/sign_up.html', {'form': form})


def log_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'owner_auth/log_in.html', {'form': form})

def dashboard_view(request):
    return render(request, 'gymdashboard/dashboard.html')  # Render the dashboard template
