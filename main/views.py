from django.shortcuts import render, redirect

from reviews.models import Review
from reviews.forms import ReviewForm


def home(request):

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = ReviewForm()

    reviews = Review.objects.order_by(
        '-created_at'
    )

    return render(
        request,
        'home.html',
        {
            'reviews': reviews,
            'form': form
        }
    )


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


def events(request):
    return render(request, 'events.html')


def vacancies(request):
    return render(request, 'vacancies.html')


def promotions(request):
    return render(request, 'promotions.html')


def register(request):
    return render(request, 'register.html')