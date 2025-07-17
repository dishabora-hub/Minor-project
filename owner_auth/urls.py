from django.urls import path
from . import views

app_name = 'owner_auth'

urlpatterns = [
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('log_in/', views.log_in_view, name='log_in'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
