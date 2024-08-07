from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from datetime import date, timedelta
# Create your models here.
class Reservations(models.Model):
    date = models.DateField()
    table_number = models.CharField(max_length=30)

    lunch_or_dinner = models.CharField(max_length=10, choices=[('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Lunch')
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Reservation for {self.name} on {self.date} at table {self.table_number}'
    
    
class Media(models.Model):
    about_header1 = models.ImageField(upload_to='about_header1/', null= True, blank= True)
    about_header2 = models.ImageField(upload_to='about_header2/', null= True, blank= True)
    about_header3 = models.ImageField(upload_to='about_header3/', null= True, blank= True)
    about_body1 = models.ImageField(upload_to='about_body1/', null= True, blank= True)
    register_image = models.ImageField(upload_to='register_image/', null= True, blank= True)
    feedback_image = models.ImageField(upload_to='feedback_image/', null= True, blank= True)

        
class Feedbacks(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    rate_us = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    feedback = models.CharField(max_length=500, blank=True , null= True)
    def __str__(self):
        return f'feedback from {self.name}'
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField(default=True,null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='Menu_image/', null= True, blank= True)

    def __str__(self):
        return self.name
    
# Signal receiver function to create default entries
@receiver(post_migrate)
def create_default_reservations(sender, **kwargs):
    if sender.name == 'Bookings':  # Replace 'your_app_name' with your actual Django app name
        today = date.today()
        for i in range(3):  # Create entries for 3 days
            for table_number in range(1, 9):  # Create 6 tables per day
                for meal_type in ['Lunch', 'Dinner']:  # Create entries for both lunch and dinner
                    Reservations.objects.get_or_create(
                        date=today + timedelta(days=i),
                        table_number=table_number,
                        lunch_or_dinner=meal_type
                    )