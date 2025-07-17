from django.urls import path
from . import views

urlpatterns = [
    path('diet/', views.diet_form, name='diet_form'),
    path('today-meal/', views.today_meal, name='today_meal'), 
]

