from django.shortcuts import render, redirect
import random
from django.http import JsonResponse
from .models import DailyExercise
import datetime

# Create your views here.

def dashboard(request):
    today = datetime.datetime.today().strftime('%A')  # Get today's day (e.g., 'Monday')
    
    try:
        # Fetch the daily exercise for the current day
        daily_exercise = DailyExercise.objects.prefetch_related('exercises').get(day=today)
    except DailyExercise.DoesNotExist:
        daily_exercise = None  # If no daily exercise for today, set it to None
    
    # Render the user dashboard with the daily exercise context
    return render(request, 'user_dashboard/dashboard.html', {'daily_exercise': daily_exercise})


def simulate_payment(request):
    return render(request, 'user_dashboard/simulate_payment.html')


# Exercise view with added checks
def exercise_view(request):
    today = datetime.datetime.today().strftime('%A')  # Get today's day (e.g., 'Monday')
    print(f"Today is: {today}")
    
    try:
        # Fetch the daily exercise for the current day
        daily_exercise = DailyExercise.objects.prefetch_related('exercises').get(day=today)
        exercises = daily_exercise.exercises.all()  # Get the exercises for today
        print(f"Exercises for today: {exercises}")
    except DailyExercise.DoesNotExist:
        daily_exercise = None  # If no daily exercise for today, set it to None
        exercises = []  # Ensure exercises is defined as an empty list
        print("No daily exercise found for today.")
    except Exception as e:
        print(f"Error fetching daily exercises: {e}")
        exercises = []  # Handle unexpected errors
    
    # Pass the daily exercise and exercises to the template
    return render(request, 'user_dashboard/exercise.html', {
        'daily_exercise': daily_exercise,
        'exercises': exercises  # Pass the list of exercises
    })
