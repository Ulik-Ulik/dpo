from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

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