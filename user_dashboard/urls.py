from django.urls import path
from . import views

  

urlpatterns = [
    path('', views.dashboard, name='user_dashboard'),
    path('simulate_payment/', views.simulate_payment, name='simulate_payment'),
    path('exercise/', views.exercise_view, name='exercise'),
  
]

