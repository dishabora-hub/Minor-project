"""
URL configuration for fitfusion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmigraph/', include('bmigraph.urls')),  # Include URLs from bmigraph app
    path('login/', include('login_page.urls')),  # Login and signup app
    path('chatbot/', include('chatbot.urls')),
    path('main_page/', include('main_page.urls')),  # Uncomment this if main_page should handle root instead of login
    path('gymdashboard/', include('gymdashboard.urls')),
    path('dashboard/', include('user_dashboard.urls')),
    path('', RedirectView.as_view(url='login/', permanent=True)),  # Redirect root to login page
    path('', include('diet.urls')),  # Include URLs from the diet app
    path('auth/', include('owner_auth.urls')),  # Add this line
  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

















 









