from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from booking.models import Booking

from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            return redirect('/')

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )
def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user
            )

            return redirect('/')

    else:

        form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )






@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by(
        'booking_date',
        'booking_time'
    )

    return render(
        request,
        'my_bookings.html',
        {
            'bookings': bookings
        }
    )
def logout_view(request):

    logout(request)

    return redirect('/')
