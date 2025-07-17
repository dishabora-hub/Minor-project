from django.db import models

# Define the Exercise model
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.name

# Define the DailyExercise model that associates exercises with each day
class DailyExercise(models.Model):
    day = models.CharField(max_length=20)  # Day of the week (e.g., 'Monday')
    muscle_group = models.CharField(max_length=100)  # Muscle group targeted (e.g., 'Chest')
    cardio = models.BooleanField(default=False)  # Whether cardio is included today
    exercises = models.ManyToManyField(Exercise, related_name='daily_exercises')

    def __str__(self):
        return self.day


  
