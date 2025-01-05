from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Slot

def book_slot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            slot = form.cleaned_data['slot']
            if not slot.is_booked:
                slot.is_booked = Trueslot.save()
                form.save()
                return redirect("booking_success")
            else:
                form.add_error('slot', 'This slot is already booked.')
    else:
        form = BookingForm()
    available_slots = Slot.objects.filter(is_booked=False)
    return render(request, 'booking/book_slot.html', {'form': form, 'available_slots': available_slots})

# Create your views here.
