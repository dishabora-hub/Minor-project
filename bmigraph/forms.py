from django import forms

class BMIForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    height_feet = forms.IntegerField(label='Height (feet)')
    height_inches = forms.IntegerField(label='Height (inches)')
    weight = forms.DecimalField(decimal_places=2, max_digits=5)



