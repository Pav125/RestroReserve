from django.shortcuts import render
from .models import Reservations

# Create your views here.
def status_table(request):
    reservations = Reservations.objects.all()
    context = {
        'tables' : reservations,
        'notshow_booknow' : True
    }
    return render(request, 'Bookings/status_table.html', context)

def home(request):
    return render(request, "Bookings/base1.html")
