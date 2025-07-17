from django.db import models
from django.utils import timezone 

class BMIData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height_feet = models.IntegerField()
    height_inches = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20)  # Optional: to store the BMI category
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BMI Data for {self.name}"


# Create your models here.
