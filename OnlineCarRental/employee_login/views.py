from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_login.models import Employee
from django.contrib.auth.models import User
from customer_login.models import Customer
from django.contrib import auth
from employee_dashboard.models import Car
from customer_login.models import Customer


def getemployee(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addemployeeinfo.html', c)


def deleteemployeeinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'deleteemployeerecord.html', c)


def adminlogin(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'adminsignin.html', c)


def addemployeeinfo(request):
    try:
        username = request.POST.get('employeeusername')
        user = User.objects.get(username=username)
        return HttpResponse("This Username already exists")

    except:
        username = request.POST.get('employeeusername', '')
        password = request.POST.get('employeepassword', '')
        employeename = request.POST.get('name', '')
        employeeemail = request.POST.get('email', '')
        employeephone = request.POST.get('phoneno', '')
        employeeadhar = request.POST.get('aadharno', '')
        employeeaddress = request.POST.get('address', '')
        employeedob = request.POST.get('dob', '')
        employeesalary = request.POST.get('salary', '0')
        employeedesignation = request.POST.get('designation', '')
        employeejoin = request.POST.get('join', '')
        employeeavailability = request.POST.get('availability', 'True')
        user = User.objects.create_user(username=username, email=employeeemail, password=password)
        user.save()
        s = Employee(employee_id=None, employee_username=username, employee_password=password,
                     employee_name=employeename,
                     employee_email=employeeemail, employee_phone_no=employeephone, employee_aadhar_no=employeeadhar,
                     employee_address=employeeaddress, employee_dob=employeedob, employee_salary=employeesalary,
                     employee_designation=employeedesignation, date_of_join=employeejoin,
                     check_availability=employeeavailability)
        s.save()
        return HttpResponseRedirect('/employee_login/success/')


def success(request):
    return render(request, 'addemployee.html')


def adminsignup(request):
    adminusername = request.POST.get('username', '')
    adminpassword = request.POST.get('password', '')
    user = auth.authenticate(username=adminusername, password=adminpassword)
    if user is not None:
        auth.login(request, user)
        return render(request, 'adminhome.html', {"username": request.user.username})
    else:
        return render(request, 'invalid.html')


def adminhome(request):
    return render(request, 'adminhome.html', {"username": request.user.username})


def deleteemployee(request):
    employeeid = request.POST.get('employeeid', '')
    employeename = request.POST.get('employeename', '')
    employee = Employee.objects.filter(employee_id=employeeid, employee_username=employeename)
    if not employee:
        return HttpResponseRedirect('/employee_login/employeedeleteunsuccessful')
    else:
        for e in employee:
            e.delete()
        return render(request, 'deletedemployeerecord.html', '')


def employeedeleteunsuccessful(request):
    return render(request, 'employeenotfound.html')


def getemployeesinfo(request):
    employees = Employee.objects.all()
    return render(request, 'viewemployee.html', {'employees': employees})


def updateemployee(request):
    employee = Employee.objects.all()
    return render(request, 'update_employee.html', {'employee': employee})


def updated(request):
    employeeid = request.POST.get('employeeid', '')
    employeeusername = request.POST.get('employeeusername', '')
    employeename = request.POST.get('employeename', '')
    employeemail = request.POST.get('employeeemail', '')
    employeephone = request.POST.get('employeephone', '')
    employeeadhar = request.POST.get('employeeaadhar', '')
    employeeaddress = request.POST.get('employeeaddress', '')
    employeedob = request.POST.get('employeedob', '')
    employeesalary = request.POST.get('employeesalary', '')
    employeedesignation = request.POST.get('employeedesignation', '')
    employeeavailability = request.POST.get('availability', 'True')
    e = Employee.objects.get(employee_id=employeeid)
    user = User.objects.get(username=e.employee_username)
    e.employee_username = employeeusername
    e.employee_name = employeename
    e.employee_email = employeemail
    e.employee_phone_no = employeephone
    e.employee_aadhar_no = employeeadhar
    e.employee_address = employeeaddress
    e.employee_dob = employeedob
    e.employee_salary = employeesalary
    e.employee_designation = employeedesignation
    e.check_availability = employeeavailability
    e.save()
    user.username = employeeusername
    user.email = employeemail
    user.save()
    return render(request, 'adminhome.html', {"username": request.user.username})


def viewcars(request):
    cars = Car.objects.all()
    return render(request, 'viewcar.html', {'cars': cars})


def viewcustomer(request):
    customer = Customer.objects.all()
    return render(request, 'viewcustomers.html', {'customer': customer})


class EmployeeListView(generic.ListView):
    model = Employee
