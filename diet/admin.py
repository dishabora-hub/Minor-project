from django.contrib import admin
from .models import DietPreference, WeeklyDietPlan

@admin.register(DietPreference)
class DietPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal', 'diet_type')  # Show user, goal, and diet type
    search_fields = ('user__username', 'goal', 'diet_type')  # Allow search by user, goal, or diet type
    list_filter = ('goal', 'diet_type')  # Filter by goal and diet type

@admin.register(WeeklyDietPlan)
class WeeklyDietPlanAdmin(admin.ModelAdmin):
    # Display key details in the admin list view
    list_display = ('day', 'goal', 'diet_type', 'breakfast', 'lunch', 'dinner', 'snacks')
    
    # Allow filtering by these fields
    list_filter = ('goal', 'diet_type', 'day')
    
    # Make it easier to search for specific meals or details
    search_fields = ('day', 'goal', 'diet_type', 'breakfast', 'lunch', 'dinner', 'snacks')
    
    # Customize form display to group related fields
    fieldsets = (
        ('Basic Information', {
            'fields': ('goal', 'diet_type', 'day')
        }),
        ('Breakfast', {
            'fields': ('breakfast', 'breakfast_ingredients', 'breakfast_recipe')
        }),
        ('Lunch', {
            'fields': ('lunch', 'lunch_ingredients', 'lunch_recipe')
        }),
        ('Dinner', {
            'fields': ('dinner', 'dinner_ingredients', 'dinner_recipe')
        }),
        ('Snacks', {
            'fields': ('snacks', 'snacks_ingredients', 'snacks_recipe')
        }),
    )
