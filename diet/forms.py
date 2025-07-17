from django import forms
from .models import DietPreference

class DietPreferenceForm(forms.ModelForm):
    class Meta:
        model = DietPreference
        fields = ['goal', 'diet_type']
