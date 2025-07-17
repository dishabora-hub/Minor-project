from django.shortcuts import render, get_object_or_404
from .forms import BMIForm
import matplotlib.pyplot as plt
import io
import urllib.parse, base64
from decimal import Decimal
from .models import BMIData
from django.utils import timezone

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

def bmi_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            height_feet = form.cleaned_data['height_feet']
            height_inches = form.cleaned_data['height_inches']
            weight = form.cleaned_data['weight']

            # Convert height to meters
            total_height_meters = (height_feet * 0.3048) + (height_inches * 0.0254)
            weight_decimal = Decimal(weight)
            height_decimal = Decimal(total_height_meters)

            bmi = calculate_bmi(weight_decimal, height_decimal)

            # Determine BMI category
            category = bmi_category(bmi)

            # Save the BMI data (without the graph)
            bmi_data = BMIData(
                name=name,
                age=age,
                weight=weight_decimal,
                height_feet=height_feet,
                height_inches=height_inches,
                bmi=bmi,
                category=category,
                date_created=timezone.now()  # Auto-filled by Django
            )
            bmi_data.save()

            # Create a BMI chart (in-memory, not saved)
            fig, ax = plt.subplots()
            ax.barh(['BMI'], [bmi], color='blue')
            ax.set_xlim(0, 50)  # Set limit for BMI scale
            ax.set_xlabel('BMI')
            ax.set_title(f'BMI for {name} (Age: {age})')

            # Save the figure to a byte stream
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

            # Pass the result to the template
            context = {
                'form': form,
                'bmi': round(bmi, 2),
                'category': category,
                'name': name,
                'image_uri': uri
            }
            return render(request, 'bmigraph/bmi_result.html', context)
    else:
        form = BMIForm()

    return render(request, 'bmigraph/bmi_form.html', {'form': form})

# This is the new function you need
def bmi_result(request, pk):
    bmi_data = get_object_or_404(BMIData, pk=pk)

    context = {
        'bmi_data': bmi_data,
        'bmi': round(bmi_data.bmi, 2),
        'category': bmi_data.category,
        'name': bmi_data.name,
    }
    return render(request, 'bmigraph/bmi_result.html', context)
