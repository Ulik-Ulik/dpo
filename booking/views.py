from django.shortcuts import render, redirect
from .forms import BookingForm, Booking
from django.shortcuts import get_object_or_404

def create_booking(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.save()

            return redirect('/my-bookings/')

    else:

        form = BookingForm()

    return render(
        request,
        'booking_form.html',
        {
            'form': form
        }
    )
def delete_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    booking.delete()

    return redirect('my_bookings')