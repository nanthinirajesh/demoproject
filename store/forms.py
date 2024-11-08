from django import forms
from .models import *

class Dateinput(forms.DateInput):
    input_type = 'date'
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
            'booking_date': Dateinput(),
        }
        
        labels={
            'p_name': "Patient Name",
            'p_phone': "Patient Phone no",
            'p_email': "Patient Email",
            'booking_date': "Booking Date",
        }

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')