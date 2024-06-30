from django.shortcuts import render,redirect
from .models import Reservations, Media
from .forms import ReservationForm

# Create your views here.

def home(request):
    return render(request, "Bookings/home1.html", )

def about(request):
    latest_image = Media.objects.latest('id')
    context={
        'image1' : latest_image.about_header1.url,
        'image2' : latest_image.about_header2.url, 
        'image3' : latest_image.about_header3.url,   
        'image4' : latest_image.about_body1.url,   
        }
    return render(request, 'Bookings/About.html', context)

def status_table(request):
    tables = Reservations.objects.all()
    context = {
        'show_booknow': True,
        'tables': tables,
    }
    return render(request, 'Bookings/status_table.html', context)

def register(request, id):
    latest_image = Media.objects.latest('id')
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
        'image' :  latest_image.register_image.url,
        'form': form,
        'table_number': details.table_number,
        'date': details.date,
        'show_booknow': True,
        }

    return render(request, 'Bookings/register.html', context )
