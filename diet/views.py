from django.shortcuts import render, redirect
from datetime import datetime
from .models import DietPreference, WeeklyDietPlan
from django.contrib.auth.decorators import login_required
from .forms import DietPreferenceForm

# Protect the diet_form view for guests (optional)
def diet_form(request):
    if request.method == 'POST':
        goal = request.POST.get('goal')
        preference = request.POST.get('preference')
        
        if request.user.is_authenticated:
            # Create or update the user's diet preference in the database
            diet_preference, created = DietPreference.objects.update_or_create(
                user=request.user, 
                defaults={'goal': goal, 'diet_type': preference}
            )
        else:
            # For guests, store the preference in the session
            diet_preference = DietPreference.objects.create(
                goal=goal, diet_type=preference
            )
            # Store the diet_preference ID in session
            request.session['diet_preference_id'] = diet_preference.id

        # Redirect to the "today's meal" view
        return redirect('today_meal')

    return render(request, 'diet/diet_form.html')


def today_meal(request):
    today = datetime.now().strftime('%A')  # Get the current day of the week
    
    if request.user.is_authenticated:
        # Fetch the user's diet preference
        diet_preference = DietPreference.objects.filter(user=request.user).first()
    else:
        # Get diet preference from session if the user is not logged in
        diet_preference_id = request.session.get('diet_preference_id')
        if diet_preference_id:
            diet_preference = DietPreference.objects.get(id=diet_preference_id)
        else:
            diet_preference = None

    if diet_preference:
        # Fetch meals based on goal, diet_type, and day of the week
        meals = WeeklyDietPlan.objects.filter(
            goal=diet_preference.goal,
            diet_type=diet_preference.diet_type,
            day=today
        )
        return render(request, 'diet/today_meal.html', {'meals': meals, 'day': today})

    # Redirect to diet form if no preference exists
    return redirect('diet_form')
