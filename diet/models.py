from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class DietPreference(models.Model):
    GOAL_CHOICES = [
        ('lose', 'Lose Weight'),
        ('gain', 'Gain Weight'),
    ]
    DIET_CHOICES = [
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES)
    diet_type = models.CharField(max_length=10, choices=DIET_CHOICES, default='veg')

    def __str__(self):
        if self.user:
            return f"{self.user.email}'s Diet: {self.goal} - {self.diet_type}"
        return f"Anonymous Diet: {self.goal} - {self.diet_type}"


class WeeklyDietPlan(models.Model):
    DIET_DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    goal = models.CharField(max_length=10, choices=[('lose', 'Lose Weight'), ('gain', 'Gain Weight')], default='gain')
    diet_type = models.CharField(max_length=10, choices=[('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian')], default='veg')
    day = models.CharField(max_length=10, choices=DIET_DAYS)
    
    # Fields for separate meals
    breakfast = models.TextField(default='Not specified')
    breakfast_ingredients = models.TextField(default='Not specified')
    breakfast_recipe = models.TextField(default='Not specified')

    lunch = models.TextField(default='Not specified')
    lunch_ingredients = models.TextField(default='Not specified')
    lunch_recipe = models.TextField(default='Not specified')

    dinner = models.TextField(default='Not specified')
    dinner_ingredients = models.TextField(default='Not specified')
    dinner_recipe = models.TextField(default='To be added')

    snacks = models.TextField(default='Not specified')
    snacks_ingredients = models.TextField(default='Not specified')
    snacks_recipe = models.TextField(default='Not specified')

    def __str__(self):
        return f"{self.day} - {self.goal} - {self.diet_type} Diet Plan"
