from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_dashboard.models import Car
from employee_login.models import Employee
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'employeelogin.html', c)


def getcarinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addcarinfo.html', c)


def deleteinfo(request):
    c = {}
    c.update(csrf(request))
    car = Car.objects.filter(car_availability=True)
    return render(request, 'deleterecord.html', {'car': car})


def back_to_homepage(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'employeehomepage.html', {"username": request.user.username})


def authorize(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'employeehomepage.html', {"username": request.user.username})
    else:
        return render(request, 'invalid.html')


def update_car(request):
    car = Car.objects.filter(car_availability=True)
    return render(request, 'updatecar.html', {'car': car})


def carupdated(request):
    carid = request.POST.get('carid', '')
    carname = request.POST.get('carcompany', '')
    carclasstype = request.POST.get('carclass', '')
    price = request.POST.get('price', '0')
    carnumber = request.POST.get('carnumber', '')
    fueltype = request.POST.get('fuel', '')
    cardescription = request.POST.get('description', '')
    caravailability = request.POST.get('availability', 'True')
    c = Car.objects.get(car_id=carid)
    c.car_company = carname
    c.car_class_type = carclasstype
    c.price_per_day = price
    c.car_number = carnumber
    c.fuel_type = fueltype
    c.car_description = cardescription
    c.car_availability = caravailability
    c.save()
    return render(request, 'employeehomepage.html')


def addcarinfo(request):
    carname = request.POST.get('carcompany', '')
    carclasstype = request.POST.get('carclass', '')
    priceperkm = request.POST.get('price', '0')
    carnumber = request.POST.get('cnumber', '')
    fueltype = request.POST.get('fuel', '')
    cardescription = request.POST.get('description', '')
    caravailability = request.POST.get('availability', 'True')
    s = Car(car_company=carname, car_class_type=carclasstype, price_per_day=priceperkm,
            car_number=carnumber,
            fuel_type=fueltype, car_description=cardescription, car_availability=caravailability)
    s.save()
    return HttpResponseRedirect('/employee_dashboard/addsuccess/')


def addsuccess(request):
    return render(request, 'addrecord.html')


def logout(request):
    auth.logout(request)
    return render(request, 'addcustomerinfo.html')


def getcars(request):
    cars = Car.objects.all()
    return render(request, 'viewcars.html', {'cars': cars})


def deleteunsuccessful(request):
    return render(request, 'notfound.html')


def deletecarinfo(request):
    carid = request.POST.get('carid', '')
    car = Car.objects.filter(car_id=carid)
    if not car:
        return HttpResponseRedirect('/employee_dashboard/deleteunsuccessful')
    else:
        for c in car:
            c.delete()
        return render(request, 'deletecarrecord.html')


class CarListView(generic.ListView):
    model = Car
