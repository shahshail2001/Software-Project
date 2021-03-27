from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_dashboard.models import Car
from datetime import date
from customer_login.models import Customer
from Car_Booking.models import Booking


# Create your views here.
def BookCar(request):
    cars = Car.objects.filter(car_availability=True)
    return render(request, 'book_car.html', {'cars': cars})


def booking(request):
    carid = request.POST.get('carid')
    cars = Car.objects.get(car_id=carid)
    return render(request, 'carbooking.html', {'cars': cars})


def book(request):
    carid = request.POST.get('carid')
    cardate = request.POST.get('cardate')
    returndate = request.POST.get('returndate')
    cars = Car.objects.get(car_id=carid)
    res1 = [int(i) for i in cardate.split('-') if i.isdigit()]
    d0 = date(res1[0], res1[1], res1[2])
    res2 = [int(i) for i in returndate.split('-') if i.isdigit()]
    d1 = date(res2[0], res2[1], res2[2])
    total_days = d1 - d0
    total_days = total_days.days
    total_amount = total_days * cars.price_per_day
    context = {
        "total_days": total_days,
        "total_amount": total_amount,
        "cars": cars,
        "carid": carid,
        "cardate": cardate,
        "returndate": returndate
    }
    return render(request, 'confirmbooking.html', context)


def b(request):
    carid = request.POST.get('carid')
    total_days = request.POST.get('total_days')
    total_amount = request.POST.get('total_amount')
    cardate = request.POST.get('cardate')
    returndate = request.POST.get('returndate')
    username = request.POST.get('username')
    password = request.POST.get('password')
    car = Car.objects.get(car_id=carid)
    if Customer.objects.filter(customer_username=username, customer_password=password).exists():
        customer = Customer.objects.get(customer_username=username, customer_password=password)
        s = Booking(customerid=customer.customer_id, customername=customer.customer_name, carid=carid,
                    carname=car.car_company, carnumber=car.car_number, carbookdate=cardate, carreturndate=returndate,
                    totalpayment=total_amount, total_no_of_days=total_days)
        s.save()
        car.car_availability = False
        car.save()
        return render(request, 'payment.html')
    else:
        return render(request, 'invalid_details.html')
