from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exercise, DailyExercise

# Register Exercise model
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sets', 'reps')  # Customize what you want to see in the list

admin.site.register(Exercise, ExerciseAdmin)

# Register DailyExercise model
class DailyExerciseAdmin(admin.ModelAdmin):
    list_display = ('day', 'muscle_group', 'cardio')  # Customize as needed
    filter_horizontal = ('exercises',)  # This allows easy selection of exercises in the admin

admin.site.register(DailyExercise, DailyExerciseAdmin)
