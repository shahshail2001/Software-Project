from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from employee_login.models import Employee


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
    s = Employee(employee_id=None, employee_username=username, employee_password=password, employee_name=employeename,
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
    if adminusername == "shail165" and adminpassword == "shail123":
        return render(request, 'adminhome.html')
    if adminusername == "harsh" and adminpassword == "harsh10":
        return render(request, 'adminhome.html')
    else:
        return render(request, 'unsuccessfulllogin.html')


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


class EmployeeListView(generic.ListView):
    model = Employee
