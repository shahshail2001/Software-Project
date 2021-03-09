from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_dashboard.models import Car


# Create your views here.
def BookCar(request):
    cars = Car.objects.all()
    return render(request, 'book_car.html', {'cars': cars})


def booking(request):
    car_id = request.POST.get('carid', '')
    cars = Car.objects.filter(car_id=car_id)
    return render(request, 'carbooking.html', {'cars': cars})
