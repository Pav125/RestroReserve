from django.db import models

# Create your models here.
class Reservations(models.Model):
    date = models.DateField()
    table_number = models.CharField(max_length=30)
    lunch_or_dinner = models.CharField(max_length=10, choices=[('Lunch', 'Lunch'), ('Dinner', 'Dinner')])
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reserved = models.BooleanField(default=False)