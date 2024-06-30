from django.shortcuts import render,redirect
from .models import Reservations, Images
from .forms import ReservationForm
from datetime import date, timedelta
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "Bookings/home1.html", )

def about(request):
    return render(request, 'Bookings/About.html')

def status_table(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    max_date = today + timedelta(days=2)
    selected_date = request.GET.get('date') or today
    meal_type = request.GET.get('meal_type')
    if not meal_type:
        meal_type = 'Lunch'
    tables = Reservations.objects.filter(date = selected_date, lunch_or_dinner = meal_type)
    
    context = {
        'show_booknow': True,
        'tables': tables,
        'today': today,
        'tomorrow': tomorrow,
        'max_date': max_date,
        'selected_date': selected_date,
        
    }
    return render(request, 'Bookings/status_table.html', context)

def register(request, id):
    image = Images.objects.latest('id')

    details = Reservations.objects.get(id=id)
    if details:
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                
                details.name = name
                details.email = email
                details.reserved = True
                details.save()
                messages.success(request, f'Your reservation for {details.name} has been made successfully')
                return redirect('status')
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

def contact(request):
    return render(request, 'Bookings/contact.html')

def menu(request):
    return render(request, 'Bookings/menu.html')