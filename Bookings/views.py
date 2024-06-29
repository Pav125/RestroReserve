from django.shortcuts import render,redirect
from .models import Reservations, Images
from .forms import ReservationForm

# Create your views here.

def home(request):
    return render(request, "Bookings/home1.html", )

def about(request):
    return render(request, 'Bookings/About.html')

def status_table(request):
    tables = Reservations.objects.all()
    context = {
        'show_booknow': True,
        'tables': tables,
    }
    return render(request, 'Bookings/status_table.html', context)

def register(request, id):
    image = Images.objects.latest('id')

    details = Reservations.objects.get(id=id)

    if details:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')
        else:
            form = ReservationForm()
    
    context = {
        'form': form,
        'image': image.image.url,
        'table_number': details.table_number,
        'date': details.date,
        'show_booknow': True,
        }

    return render(request, 'Bookings/register.html', context )
