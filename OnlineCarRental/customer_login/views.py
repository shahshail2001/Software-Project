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


def deletecustomer(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'deletecustomer.html', c)


def customerlogin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    customer = Customer.objects.all()
    for i in customer:
        if i.customer_username == username and i.customer_password == password:
            return render(request, 'customerhomepage.html', {"customerusername": username})
        else:
            return HttpResponse("Invalid Credentials")


def customerinfo(request):
    try:
        customerusername = request.POST.get('username', '')
        customer = Customer.objects.all()
        for i in customer:
            if i.customer_username == customerusername:
                return HttpResponse("This username already exists")
    except:
        customerusername = request.POST.get('username', '')
        customerpassword = request.POST.get('password', '')
        customername = request.POST.get('name', '')
        customeremail = request.POST.get('email', '')
        customerphone = request.POST.get('phoneno', '')
        customeraadhar = request.POST.get('aadhar', '')
        customeraddress = request.POST.get('address', '')
        customerdob = request.POST.get('dob')
        s = Customer(customer_id=None, customer_username=customerusername, customer_password=customerpassword,
                     customer_name=customername, customer_email=customeremail, customer_phone_no=customerphone,
                     customer_aadhar_no=customeraadhar, customer_address=customeraddress,
                     customer_dob=customerdob)
        s.save()
        return HttpResponseRedirect('/customer_login/registersuccess/')


def registersuccess(request):
    return render(request, 'customerregistered.html')


def delete_customer(request):
    customerid = request.POST.get('customerid', '')
    customerusername = request.POST.get('customername', '')
    customer = Customer.objects.filter(customer_id=customerid, customer_username=customerusername)
    if not customer:
        return render(request, 'customernotfound.html')
    else:
        for i in customer:
            i.delete()
        return render(request, 'deletecustomerrecord.html')


def viewcustomer(request):
    customer = Customer.objects.all()
    return render(request, 'view_customers.html', {'customer': customer})


class CustomerListView(generic.ListView):
    model = Customer
