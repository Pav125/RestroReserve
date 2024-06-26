from django.shortcuts import render

# Create your views here.
def status_table(request):
    tables = [
        {'name': 'Table1', 'available': False},
        {'name': 'Table2', 'available': True},
        {'name': 'Table3', 'available': True},
        {'name': 'Table4', 'available': False},
        {'name': 'Table5', 'available': False},
        {'name': 'Table6', 'available': True},
        {'name': 'Table4', 'available': True},
        {'name': 'Table5', 'available': False},
        {'name': 'Table6', 'available': True},
        {'name': 'Table6', 'available': True},
    ]
    context = {
        'tables' : tables,
        'notshow_booknow' : True
    }
    return render(request, 'Bookings/status_table.html', context)

def home(request):
    return render(request, "Bookings/home.html")
