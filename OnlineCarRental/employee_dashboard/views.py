from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_dashboard.models import Car


# Create your views here.
def getcarinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addcarinfo.html', c)


def addcarinfo(request):
    carid = request.POST.get('cid', '0')
    carname = request.POST.get('carcompany', '')
    carclasstype = request.POST.get('carclass', '')
    priceperkm = request.POST.get('price', '0')
    carnumber = request.POST.get('cnumber', '')
    fueltype = request.POST.get('fuel', '')
    cardescription = request.POST.get('description', '')
    caravailability = request.POST.get('availability', 'True')
    s = Car(car_id=carid, car_company=carname, car_class_type=carclasstype, price_per_km=priceperkm,
            car_number=carnumber,
            fuel_type=fueltype, car_description=cardescription, car_availability=caravailability)
    s.save()
    return HttpResponseRedirect('/employee_dashboard/addsuccess/')


def addsuccess(request):
    return render(request, 'addrecord.html')


class CarListView(generic.ListView):
    model = Car
