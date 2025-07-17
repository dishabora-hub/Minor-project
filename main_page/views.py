# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact  # Import the Contact model

# Home page view
def homepage(request):
    return render(request, 'main_page/index.html')

# Main page view
def main_page_home(request):
    return render(request, 'main_page/index.html')

# Contact form view
def contact_us(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                enquiry=form.cleaned_data['enquiry']
            )
            # Add a success message
            messages.success(request, "Your issue has been successfully submitted. We'll look into it.")
            return redirect('contact_us')  # Redirect to the same page to avoid resubmitting on refresh
    return render(request, 'contact_us.html', {'form': form})  # Render the form even if it is not valid

# About us view
def aboutus(request):
    return render(request, 'aboutus.html')
