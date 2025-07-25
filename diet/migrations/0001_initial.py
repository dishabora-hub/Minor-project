# Generated by Django 5.1.3 on 2024-11-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DietPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(choices=[('lose', 'Lose Weight'), ('gain', 'Gain Weight')], max_length=10)),
                ('preference', models.CharField(choices=[('vegetarian', 'Vegetarian'), ('non_vegetarian', 'Non-Vegetarian')], max_length=15)),
                ('diet_plan', models.TextField()),
            ],
        ),
    ]
