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
    carid = request.POST.get('carid')
    cars = Car.objects.get(car_id=carid)
    print(cars)
    return render(request, 'carbooking.html', {'cars': cars})


def book(request):
    carid = request.POST.get('carid')
    cardate = request.POST.get('cardate')
    returndate = request.POST.get('returndate')
    context = {
        "carid": carid,
        "cardate": cardate,
        "returndate": returndate
    }
    return render(request, 'confirmbooking.html', context)
