from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'main_page'

urlpatterns = [
    # Use a unique path for each view
    #path('', views.homepage, name='homepage'),  # Home page view
    path('mainpage/', views.main_page_home, name='main_page_home'),  # Main page view (different view if needed)
    path('home_page/', views.homepage, name='homepage'),  # If you want both 'home_page' and 'homepage' to map to the same page
    path('contact/', views.contact_us, name='contact_us'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login:login'), name='logout'),
]

