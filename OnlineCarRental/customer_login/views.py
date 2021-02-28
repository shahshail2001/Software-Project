from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from customer_login.models import Customer


def getcustomer(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addcustomerinfo.html', c)


def customerinfo(request):
    customerusername = request.POST.get('username', '')
    customerpassword = request.POST.get('password', '')
    customername = request.POST.get('name', '')
    customeremail = request.POST.get('email', '')
    customerphone = request.POST.get('phoneno', '')
    customeraadhar = request.POST.get('aadhar', '')
    customeraddress = request.POST.get('adress', '')
    customerdob = request.POST.get('dob')
    s = Customer(customer_id=None, customer_username=customerusername, customer_password=customerpassword,
                 customer_name=customername, customer_email=customeremail, customer_phone_no=customerphone,
                 customer_aadhar_no=customeraadhar, customer_address=customeraddress,
                 customer_dob=customerdob)
    s.save()
    return HttpResponseRedirect('/customer_login/registersuccess/')
