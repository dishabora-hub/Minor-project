from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BMIData

# Register the BMIData model in the admin interface
class BMIDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'weight', 'height_feet', 'height_inches', 'bmi', 'category', 'date_created')
    search_fields = ('name', 'age')
    list_filter = ('category',)
    ordering = ('-date_created',)

# Register the BMIData model with the custom admin class
admin.site.register(BMIData, BMIDataAdmin)
