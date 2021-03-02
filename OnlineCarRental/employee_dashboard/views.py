from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_dashboard.models import Car
from employee_login.models import Employee
from django.contrib import auth


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
    return render(request, 'deleterecord.html')


def authorize(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(employee_username=username, employee_password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('http://localhost:8000/employee_dashboard/employeehomepage.html')
    else:
        return render(request, 'invalid.html')


def addcarinfo(request):
    carname = request.POST.get('carcompany', '')
    carclasstype = request.POST.get('carclass', '')
    priceperkm = request.POST.get('price', '0')
    carnumber = request.POST.get('cnumber', '')
    fueltype = request.POST.get('fuel', '')
    cardescription = request.POST.get('description', '')
    caravailability = request.POST.get('availability', 'True')
    s = Car(car_id=None, car_company=carname, car_class_type=carclasstype, price_per_km=priceperkm,
            car_number=carnumber,
            fuel_type=fueltype, car_description=cardescription, car_availability=caravailability)
    s.save()
    return HttpResponseRedirect('/employee_dashboard/addsuccess/')


def addsuccess(request):
    return render(request, 'addrecord.html')


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
