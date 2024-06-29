from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ['date', 'table_number', 'lunch_or_dinner', 'name', 'email', 'reserved']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'table_number': forms.NumberInput(attrs={'min': 1}),
            'lunch_dinner': forms.Select(choices=Reservations.lunch_or_dinner),
            'reserved': forms.CheckboxInput(),
        }
