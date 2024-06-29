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

def register(request):
    image = Images.objects.latest('id')
    table_number = request.GET.get('table_number', None)
    initial_data = {'table_number': table_number} if table_number else {}

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ReservationForm(initial=initial_data)
    
    context = {
        'form': form,
        'image': image.image.url,
        }

    return render(request, 'Bookings/register.html', context )
