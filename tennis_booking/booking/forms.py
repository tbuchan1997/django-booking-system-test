from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookingfields = ['name', 'email', 'phone', 'slot']