from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from customer_login.models import Customer
from django.contrib.auth.models import User
from django.contrib import auth


def getcustomer(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addcustomerinfo.html', c)


def deletecustomer(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'deletecustomer.html', c)


def customerloginpage(request):
    return render(request, 'customerlogin.html')


def customerlogin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'customerhomepage.html')
    return HttpResponse("Invalid Credentials")


def update(request):
    c = request.user.username
    customer = Customer.objects.get(customer_username=c)
    return render(request, 'update.html', {'customer': customer})


def updatedetails(request):
    customerid = request.POST.get('cus_id', '')
    customerusername = request.POST.get('username', '')
    customername = request.POST.get('name', '')
    customeremail = request.POST.get('email', '')
    customerphone = request.POST.get('phoneno', '')
    customeraadhar = request.POST.get('aadhar', '')
    customeraddress = request.POST.get('address', '')
    customerdob = request.POST.get('dateofbirth', '')
    c = Customer.objects.get(customer_id=customerid)
    user = User.objects.get(username=c.customer_username)
    c.customer_username = customerusername
    c.customer_name = customername
    c.customer_email = customeremail
    c.customer_phone_no = customerphone
    c.customer_aadhar_no = customeraadhar
    c.customer_address = customeraddress
    c.customer_dob = customerdob
    c.save()
    user.username = customerusername
    user.email = customeremail
    user.save()
    return render(request, 'customerhomepage.html')


def signout(request):
    auth.logout(request)
    return render(request, 'addcustomerinfo.html')


def home_page(request):
    return render(request, 'customerhomepage.html')


def customerinfo(request):
    customerusername = request.POST.get('username', '')
    customerpassword = request.POST.get('password', '')
    customername = request.POST.get('name', '')
    customeremail = request.POST.get('email', '')
    customerphone = request.POST.get('phoneno', '')
    customeraadhar = request.POST.get('aadhar', '')
    customeraddress = request.POST.get('address', '')
    customerdob = request.POST.get('dateofbirth', '')
    s = Customer(customer_id=None, customer_username=customerusername, customer_password=customerpassword,
                 customer_name=customername, customer_email=customeremail, customer_phone_no=customerphone,
                 customer_aadhar_no=customeraadhar, customer_address=customeraddress,
                 customer_dob=customerdob)
    user = User.objects.create_user(username=customerusername, email=customeremail, password=customerpassword)
    user.save()
    s.save()
    return HttpResponseRedirect('/customer_login/registersuccess/')


def registersuccess(request):
    return render(request, 'customerhomepage.html')


def delete_customer(request):
    val = request.POST.get('submit')
    if val == "YES":
        u = request.user.username
        c = Customer.objects.get(customer_username=u)
        user = User.objects.get(username=c.customer_username)
        user.delete()
        c.delete()
        return render(request, 'deletecustomerrecord.html')
    elif val == "NO":
        return render(request, 'customerhomepage.html')


def viewcustomer(request):
    customer = Customer.objects.all()
    return render(request, 'view_customers.html', {'customer': customer})


class CustomerListView(generic.ListView):
    model = Customer
