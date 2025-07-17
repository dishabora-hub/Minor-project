from django.urls import path
from . import views

#urlpatterns = [
#path('bmi/', views.bmi_view, name='bmi_view'),
#]
# bmigraph/views.py
#from django.shortcuts import render
#def login_view(request):
#if request.method == 'POST':
# Handle login logic here
# @ pass
# return render(request, 'bmigraph/login.html')  # Adjust the template name as needed
# bmigraph/urls.py

#from django.urls import path
#from . import views  # Import the views

#urlpatterns = [
 #   path('bmi/', views.bmi_view, name='bmi_view'),  # BMI view
  #  path('login/', views.login_view, name='login'),  # Add login view here if needed
    # Add other app-specific URL patterns here
#]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.bmi_view, name='bmi_view'),  # Redirect base URL to bmi_view
    path('bmi/', views.bmi_view, name='bmi_view'),
    path('bmi/result/<int:pk>/', views.bmi_result, name='bmi_result'),
    # Add other URL patterns as needed
]






