from django.shortcuts import render,redirect
from .models import Reservations, Media, Feedbacks,Category
from .forms import ReservationForm,FeedbackForm
from datetime import date, timedelta
from django.contrib import messages
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
    latest_image = Media.objects.latest('id')
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
        'image' :  latest_image.register_image.url,
        'form': form,
        'table_number': details.table_number,
        'date': details.date,
        'show_booknow': True,
        }

    return render(request, 'Bookings/register.html', context )

def feedback_view(request):
    image = Media.objects.latest('id')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, f'{name}! Thankyou for your feedback')
            return redirect('home')
    else:
        form = FeedbackForm()
    context={
        'form': form,
        'image': image.feedback_image.url,
        }
    return render(request, 'Bookings/contact.html', context)

def menu_view(request):
    categories = Category.objects.all().prefetch_related('items')
    context = {
        'categories': categories,
    }
    return render(request, 'Bookings/menu.html', context)

