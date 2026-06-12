from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('events/', views.events, name='events'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('promotions/', views.promotions, name='promotions'),
]